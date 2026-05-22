# SE PB 脚本开发范式

## 一、参数管理器范式

### 设计理念

所有可调超参数集中在一个 `参数管理器` 类中：

- 属性层：C# 属性定义参数（携带默认值 + XML 注释）
- 注册层：委托系统将每个属性绑定到 `key = value` 的序列化格式
- 持久化：构造函数自动读取 `Me.CustomData`，首次运行时写入带注释的默认配置
- 格式容忍：忽略空行和 `//`、`#` 开头的注释行；未知 key 自动跳过

CustomData 示例格式：
```
// 参数配置文件
// 不要修改任何参数，除非你知道以下三件事：
// 是什么，如何工作，可能的影响

// 接近引爆距离阈值(米)
引爆距离阈值 = 5

// 视线角速度PID P系数
方向制导_Kp = 16
```

### 骨架代码

```csharp
using System;
using System.Collections.Generic;
using System.Text;
using Sandbox.ModAPI.Ingame;
using VRageMath;

namespace IngameScript
{
    /// <summary>
    /// 项目参数管理器 —— 所有超参数的单一来源
    /// </summary>
    public class 参数管理器
    {
        // ── 1. 在这里声明所有参数属性，设好默认值，写 XML 注释 ──────────────

        #region 示例参数
        /// <summary>最大速度限制(m/s)</summary>
        public float 最大速度 { get; set; } = 100f;

        /// <summary>更新间隔(ticks)</summary>
        public int 更新间隔 { get; set; } = 10;
        #endregion

        // ── 2. 委托注册系统（框架层，通常不需要改动）────────────────────────

        private Dictionary<string, 参数描述符> 参数注册表;

        /// <summary>
        /// 注册所有参数到注册表。
        /// 添加新参数：在此方法末尾调用 注册参数()。
        /// </summary>
        private void 注册所有参数()
        {
            参数注册表 = new Dictionary<string, 参数描述符>();

            // 格式：注册参数("key", () => 属性.ToString(), v => { /* 解析并赋值 */ }, "描述文字");
            注册参数("最大速度",
                () => 最大速度.ToString(),
                v => { float val; if (float.TryParse(v, out val)) 最大速度 = val; },
                "最大速度限制(m/s)");

            注册参数("更新间隔",
                () => 更新间隔.ToString(),
                v => { int val; if (int.TryParse(v, out val)) 更新间隔 = val; },
                "更新间隔(ticks)");

            // 带 空值时隐藏=true 的参数：值为空/null 时不写入 CustomData
            // 注册参数("可选参数",
            //     获取值: () => 可选参数 ?? "",
            //     设置值: v => 可选参数 = v.Trim(),
            //     描述: "留空则不生效",
            //     空值时隐藏: true);
        }

        // ── 3. 构造函数（框架层，通常不需要改动）───────────────────────────

        /// <summary>从 PB 方块的 CustomData 加载参数；若为空则写入默认配置。</summary>
        public 参数管理器(IMyTerminalBlock block)
        {
            注册所有参数();
            string cd = block.CustomData;
            if (!string.IsNullOrWhiteSpace(cd))
            {
                解析配置字符串(cd);
                block.CustomData = 生成配置字符串(); // 补全新增参数
            }
            else
                block.CustomData = 生成配置字符串(); // 首次运行写入默认值
        }

        /// <summary>直接从字符串加载参数（用于 IGC / Storage 等场景）。</summary>
        public 参数管理器(string 配置字符串)
        {
            注册所有参数();
            解析配置字符串(配置字符串);
        }

        // ── 4. 序列化 / 反序列化（框架层，通常不需要改动）─────────────────

        private void 解析配置字符串(string 配置字符串)
        {
            if (string.IsNullOrWhiteSpace(配置字符串)) return;
            foreach (string 行 in 配置字符串.Split('\n'))
            {
                string s = 行.Trim();
                if (string.IsNullOrEmpty(s) || s.StartsWith("//") || s.StartsWith("#")) continue;
                string[] kv = s.Split('=');
                if (kv.Length != 2) continue;
                string key = kv[0].Trim(), val = kv[1].Trim();
                if (参数注册表.ContainsKey(key))
                {
                    try { 参数注册表[key].设置值(val); } catch { /* 解析失败保持默认值 */ }
                }
            }
        }

        public string 生成配置字符串()
        {
            var sb = new StringBuilder();
            sb.AppendLine("// 参数配置文件");
            sb.AppendLine("// 不要修改任何参数，除非你知道以下三件事：");
            sb.AppendLine("// 是什么，如何工作，可能的影响");
            foreach (var kvp in 参数注册表)
            {
                string val = kvp.Value.获取值();
                if (kvp.Value.空值时隐藏 && string.IsNullOrWhiteSpace(val)) continue;
                if (!string.IsNullOrEmpty(kvp.Value.描述))
                    sb.AppendLine($"// {kvp.Value.描述}");
                sb.AppendLine($"{kvp.Key} = {val}");
                sb.AppendLine();
            }
            return sb.ToString();
        }

        private void 注册参数(string 参数名, Func<string> 获取值, Action<string> 设置值,
                              string 描述 = "", bool 空值时隐藏 = false)
        {
            参数注册表[参数名] = new 参数描述符(获取值, 设置值, 描述, 空值时隐藏);
        }

        // ── 5. 类型辅助方法（按需添加）──────────────────────────────────────

        protected string 格式化Vector3D(Vector3D v) => $"{v.X}, {v.Y}, {v.Z}";

        protected Vector3D? 解析Vector3D(string s)
        {
            if (string.IsNullOrWhiteSpace(s)) return null;
            try
            {
                var p = s.Split(',');
                if (p.Length == 3)
                    return new Vector3D(double.Parse(p[0].Trim()),
                                        double.Parse(p[1].Trim()),
                                        double.Parse(p[2].Trim()));
            }
            catch { }
            return null;
        }

        protected string 格式化角度(double 弧度) => (弧度 * 180.0 / Math.PI).ToString();

        protected double 解析角度(string 度数)
        {
            double d;
            return double.TryParse(度数, out d) ? d * Math.PI / 180.0 : 0;
        }

        protected string 格式化枚举<T>(T 值) => 值.ToString();

        protected T 解析枚举<T>(string s, T 默认值) where T : struct
        {
            T result;
            return Enum.TryParse(s, out result) ? result : 默认值;
        }
    }

    /// <summary>参数描述符：持有读/写委托、描述文字、空值时是否隐藏。</summary>
    public class 参数描述符
    {
        public Func<string> 获取值 { get; }
        public Action<string> 设置值 { get; }
        public string 描述 { get; }
        public bool 空值时隐藏 { get; }

        public 参数描述符(Func<string> 获取值, Action<string> 设置值,
                          string 描述 = "", bool 空值时隐藏 = false)
        {
            this.获取值 = 获取值;
            this.设置值 = 设置值;
            this.描述 = 描述;
            this.空值时隐藏 = 空值时隐藏;
        }
    }
}
```

### 如何添加新参数（步骤）

1. **声明属性**（在对应 `#region` 中）：
   ```csharp
   /// <summary>描述文字</summary>
   public double 新参数 { get; set; } = 默认值;
   ```

2. **注册委托**（在 `注册所有参数()` 末尾）：
   ```csharp
   注册参数("新参数",
       () => 新参数.ToString(),
       v => { double val; if (double.TryParse(v, out val)) 新参数 = val; },
       "描述文字(单位)");
   ```

3. **自定义类型**：在辅助方法区添加 `格式化XXX()` / `解析XXX()`，参照 `格式化Vector3D` 的模式。

### 在 Program.cs 中的用法

```csharp
参数管理器 参数;

public Program()
{
    参数 = new 参数管理器(Me);   // 读取 CustomData，首次运行写入默认值
    Runtime.UpdateFrequency = UpdateFrequency.Update10;
}

public void Main(string argument, UpdateType updateSource)
{
    // 直接访问属性
    float v = 参数.最大速度;
}
```

---

## 二、通用工具类

> 将以下代码复制到新项目的 `Utils.cs`（或任意 .cs 文件）中即可使用，无需修改。

### PID / PID3 实现

```csharp
using System;
using VRageMath;

namespace IngameScript
{
    /// <summary>
    /// 单轴 PID 控制器，支持输出限幅与 Back-calculation 抗积分饱和。
    /// </summary>
    public class PID
    {
        double _kp, _ki, _kd, _dt;
        double _prevError, _integral;
        double _outputMax = double.MaxValue, _outputMin = double.MinValue;
        double _integralMax = double.MaxValue, _integralMin = double.MinValue;
        bool _useBackCalc = false;
        double _backCalcFactor = 0.1;

        public PID(double kp, double ki, double kd, double dt)
        { _kp = kp; _ki = ki; _kd = kd; _dt = dt; }

        /// <summary>设置输出上下限，同时自动启用 Back-calculation 抗饱和。</summary>
        public void SetOutputLimits(double min, double max)
        { _outputMin = min; _outputMax = max; _useBackCalc = true; }

        public void SetIntegralLimits(double min, double max)
        { _integralMin = min; _integralMax = max; }

        public void SetBackCalculationFactor(double factor)
        { _backCalcFactor = factor; }

        public double GetOutput(double error)
        {
            _integral += error * _dt;
            if (_integral > _integralMax) _integral = _integralMax;
            if (_integral < _integralMin) _integral = _integralMin;

            double derivative = (error - _prevError) / _dt;
            _prevError = error;

            double output = _kp * error + _ki * _integral + _kd * derivative;

            if (_useBackCalc)
            {
                double raw = output;
                if (output > _outputMax) output = _outputMax;
                else if (output < _outputMin) output = _outputMin;

                if (output != raw && Math.Abs(_ki) > 1e-10)
                {
                    _integral += (output - raw) * _backCalcFactor / _ki;
                    if (_integral > _integralMax) _integral = _integralMax;
                    if (_integral < _integralMin) _integral = _integralMin;
                }
            }

            if (double.IsNaN(output) || double.IsInfinity(output)) Reset();
            return output;
        }

        public void Reset() { _prevError = 0; _integral = 0; }
    }

    /// <summary>
    /// 三轴 PID，各轴独立控制，输入/输出均为 Vector3D。
    /// </summary>
    public class PID3
    {
        readonly PID _x, _y, _z;

        public PID3(double kp, double ki, double kd, double dt)
        { _x = new PID(kp, ki, kd, dt); _y = new PID(kp, ki, kd, dt); _z = new PID(kp, ki, kd, dt); }

        public void SetOutputLimits(double min, double max)
        { _x.SetOutputLimits(min, max); _y.SetOutputLimits(min, max); _z.SetOutputLimits(min, max); }

        public void SetOutputLimits(Vector3D min, Vector3D max)
        { _x.SetOutputLimits(min.X, max.X); _y.SetOutputLimits(min.Y, max.Y); _z.SetOutputLimits(min.Z, max.Z); }

        public void SetIntegralLimits(double min, double max)
        { _x.SetIntegralLimits(min, max); _y.SetIntegralLimits(min, max); _z.SetIntegralLimits(min, max); }

        public Vector3D GetOutput(Vector3D error)
        { return new Vector3D(_x.GetOutput(error.X), _y.GetOutput(error.Y), _z.GetOutput(error.Z)); }

        public void Reset() { _x.Reset(); _y.Reset(); _z.Reset(); }

        public PID PidX => _x;
        public PID PidY => _y;
        public PID PidZ => _z;
    }
}
```

#### 用法示例

```csharp
var pid = new PID(kp: 16.0, ki: 0.05, kd: 8.0, dt: 1.0 / 6.0);
pid.SetOutputLimits(-Math.PI, Math.PI); // 同时启用 Back-calculation 抗饱和
pid.SetIntegralLimits(-90, 90);

double output = pid.GetOutput(error);   // 每 tick 调用一次
pid.Reset();                            // 切换目标时重置状态

var pid3 = new PID3(kp: 5, ki: 0, kd: 0, dt: dt);
pid3.SetOutputLimits(-1, 1);
Vector3D output3 = pid3.GetOutput(errorVec);
```

---

### CircularQueue\<T\> / MovingAverageQueue\<T\> 实现

```csharp
using System;

namespace IngameScript
{
    /// <summary>
    /// 定容环形缓冲区：满时覆盖最旧元素，O(1) 插入，O(1) 按龄索引。
    /// index 0 = 最新，index Count-1 = 最旧。
    /// </summary>
    public class CircularQueue<T>
    {
        readonly T[] _items;
        int _head = -1, _size;
        readonly int _capacity;
        public bool HasError { get; private set; }

        public CircularQueue(int capacity)
        { _items = new T[capacity]; _capacity = capacity; }

        public void AddFirst(T item)
        {
            _head = (_head + 1) % _capacity;
            _items[_head] = item;
            if (_size < _capacity) _size++;
            HasError = false;
        }

        public void Clear() { _size = 0; _head = -1; HasError = false; }

        public T GetItemAt(int index)
        {
            if (index < 0 || index >= _size) { HasError = true; return default(T); }
            return _items[(_head - index + _capacity) % _capacity];
        }

        public bool TryGetItemAt(int index, out T item)
        {
            if (index < 0 || index >= _size) { item = default(T); HasError = true; return false; }
            item = _items[(_head - index + _capacity) % _capacity];
            return true;
        }

        public T First
        {
            get
            {
                if (_size == 0) { HasError = true; return default(T); }
                return _items[_head];
            }
        }

        public T Last
        {
            get
            {
                if (_size == 0) { HasError = true; return default(T); }
                return _items[(_head - (_size - 1) + _capacity) % _capacity];
            }
        }

        public bool TryGetFirst(out T item)
        {
            if (_size == 0) { item = default(T); HasError = true; return false; }
            item = _items[_head]; return true;
        }

        public bool TryGetLast(out T item)
        {
            if (_size == 0) { item = default(T); HasError = true; return false; }
            item = _items[(_head - (_size - 1) + _capacity) % _capacity]; return true;
        }

        public bool IsEmpty => _size == 0;
        public int Count => _size;
    }

    /// <summary>
    /// 滑动平均队列：O(1) 更新和查询，通过委托支持任意类型 T。
    /// </summary>
    public class MovingAverageQueue<T> : CircularQueue<T>
    {
        readonly int _capacity;
        readonly Func<T, T, T> _add, _subtract;
        readonly Func<T, int, T> _divide;
        T _sum;

        public MovingAverageQueue(int capacity,
            Func<T, T, T> add, Func<T, T, T> subtract, Func<T, int, T> divide)
            : base(capacity)
        {
            _capacity = capacity;
            _add = add; _subtract = subtract; _divide = divide;
            _sum = default(T);
        }

        public new void AddFirst(T item)
        {
            T removed = default(T);
            if (Count == _capacity) removed = GetItemAt(Count - 1);
            base.AddFirst(item);
            _sum = _subtract(_add(_sum, item), removed);
        }

        public T Sum => _sum;
        public T Average => Count > 0 ? _divide(_sum, Count) : default(T);
    }
}
```

#### 用法示例

```csharp
// CircularQueue：记录最近 12 帧位置
var history = new CircularQueue<Vector3D>(12);
history.AddFirst(currentPos);           // 最新 = index 0
Vector3D latest = history.First;
Vector3D oldest = history.Last;
Vector3D threeFramesAgo = history.GetItemAt(3);

// MovingAverageQueue：5 帧滑动平均（Vector3D）
var ma = new MovingAverageQueue<Vector3D>(
    5,
    (a, b) => a + b,
    (a, b) => a - b,
    (a, n) => a / n
);
ma.AddFirst(vec);
Vector3D avg = ma.Average;

// MovingAverageQueue：double 版本
var maD = new MovingAverageQueue<double>(
    5,
    (a, b) => a + b,
    (a, b) => a - b,
    (a, n) => a / n
);
```

> **注意**：`MovingAverageQueue<T>.AddFirst()` 用 `new` 重写了父类方法。  
> 务必通过 `MovingAverageQueue<T>` 类型引用调用，不要向上转型为 `CircularQueue<T>` 再插入，否则滑动和不会更新。

---

## 三、开发建议

- 每个项目一份 `参数管理器.cs`，框架层不改，只填 `注册所有参数()` 和属性声明。
- `PID`/`PID3`/`CircularQueue<T>`/`MovingAverageQueue<T>` 直接复制进项目的 `Utils.cs`，无需修改。
- 参数较多时用 `#region` 分块（按功能分，与注册顺序一致），便于维护。
- 添加隐藏参数（`空值时隐藏: true`）用于高级调试选项，正常配置不显示。
