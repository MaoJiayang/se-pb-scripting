# SE PB 脚本 — 枚举速查、代码模式与踩坑注意事项

## 枚举速查

### UpdateFrequency / UpdateType

```csharp
// 在构造函数中设置自动更新频率
Runtime.UpdateFrequency = UpdateFrequency.Update10;  // 约 167ms 一次

UpdateFrequency.Update1    // 每 tick（约 16.7ms）
UpdateFrequency.Update10   // 每 10 ticks（约 167ms）
UpdateFrequency.Update100  // 每 100 ticks（约 1.67s）
UpdateFrequency.Once       // 下次 Main 调用后自动清除

// Main(string argument, UpdateType updateSource) 的 updateSource 参数
UpdateType.Update1 / Update10 / Update100 / Once
UpdateType.Terminal     // 终端按钮/工具栏触发
UpdateType.Trigger      // Timer / Sensor 触发
UpdateType.IGC          // 跨网格通信触发
```

### 探测与状态相关枚举

```csharp
// 探测实体类型（MyDetectedEntityType）
MyDetectedEntityType.LargeGrid / SmallGrid
MyDetectedEntityType.FloatingObject / Planet
MyDetectedEntityType.CharacterHuman / CharacterOther

// 我方关系（MyRelationsBetweenPlayerAndBlock）
MyRelationsBetweenPlayerAndBlock.Owner
MyRelationsBetweenPlayerAndBlock.FactionShare
MyRelationsBetweenPlayerAndBlock.Neutral
MyRelationsBetweenPlayerAndBlock.Enemies

// 着陆轮状态（LandingGearMode）
LandingGearMode.Locked / ReadyToLock / Unlocked

// 连接器状态（MyShipConnectorStatus）
MyShipConnectorStatus.Connected / Connectable / Unconnected
```

---

## VRageMath 代码模式

### Vector3D

```csharp
// 静态常量
Vector3D.Zero / One / Forward / Backward / Up / Down / Left / Right

// 常用操作
Vector3D.Normalize(v)                    // 归一化（返回新向量）
Vector3D.Dot(a, b)                       // 点积（double）
Vector3D.Cross(a, b)                     // 叉积（返回新向量）
Vector3D.Distance(a, b)                  // 两点距离
Vector3D.TransformNormal(v, matrix)      // 法向量变换（忽略平移）

// 世界坐标方向 → 飞船本地坐标方向（常用于控制逻辑）
Vector3D localDir = Vector3D.TransformNormal(worldDir, MatrixD.Transpose(cockpit.WorldMatrix));
```

### MatrixD

```csharp
// 从方块 WorldMatrix 读取朝向（世界坐标系单位方向向量）
matrix.Forward / Backward / Up / Down / Left / Right
matrix.Translation   // 世界坐标位置

// 矩阵运算
MatrixD.Invert(matrix)      // 逆矩阵（开销较大）
MatrixD.Transpose(matrix)   // 转置（纯旋转矩阵的逆 = 转置，更快）
```

### Quaternion

```csharp
Quaternion.CreateFromRotationMatrix(matrix)
Quaternion.CreateFromAxisAngle(axis, angle)
Quaternion.Slerp(q1, q2, t)   // 球面线性插值
```

---

## 方块查找代码模式

```csharp
// 按名称查找并转型（找不到返回 null，需 null 检查）
var gyro = GridTerminalSystem.GetBlockWithName("陀螺仪") as IMyGyro;

// 按类型批量获取（在构造函数中缓存，不要每 tick 调用）
var thrusters = new List<IMyThrust>();
GridTerminalSystem.GetBlocksOfType(thrusters, t => t.IsSameConstructAs(Me));

// 按方块组获取
var group = GridTerminalSystem.GetBlockGroupWithName("推进器组");
var blocks = new List<IMyThrust>();
group?.GetBlocksOfType(blocks);

// 按 CustomData 标记过滤（适合多脚本共存场景）
var myBlocks = new List<IMyTerminalBlock>();
GridTerminalSystem.GetBlocksOfType(myBlocks, b =>
    b.IsSameConstructAs(Me) && b.CustomData.Contains("[TAG]"));
```

---

## 踩坑注意事项

### 性能

- `GetBlocksOfType` 有遍历开销，**务必在构造函数中缓存**，不要在 `Main()` 里每 tick 调用
- 每次运行 code junctions（方法调用、条件、循环等）上限约 **50,000**，超出脚本立即终止；用 `Runtime.CurrentInstructionCount` 监控
- 另有脚本字符上限 **100,000**（针对压缩后的内容；`mdk.ini` 里设置 `minify=full` 可显著节省字符，让更多逻辑塞进同等上限）
- 字符串拼接（`+`）在循环中会产生大量分配，优先用 `StringBuilder`

### 子网格过滤

- 活塞头、转子头属于不同构造体（子网格），`GetBlocksOfType` 会包含它们
- 用 `block.IsSameConstructAs(Me)` 过滤，确保只操作本构造体的方块

### 探测结果

- `MyDetectedEntityInfo.IsEmpty()` **使用前必须检查**，否则访问空结果成员会异常
- 摄像机 `Raycast` 返回的 `HitPosition` 仅射线模式有效，纯探测模式下可能为 null

### 陀螺仪坐标系 ⚠️

- `IMyGyro` 的 `Pitch`、`Yaw`、`Roll` 是**陀螺仪自身坐标系**，不是世界坐标系
- 需要先将世界坐标系的目标角速度转换到陀螺仪局部坐标系再写入：

```csharp
// 将世界坐标系角速度 worldOmega 写入陀螺仪
Vector3D local = Vector3D.TransformNormal(worldOmega, MatrixD.Transpose(gyro.WorldMatrix));
gyro.Pitch = (float)-local.X;
gyro.Yaw   = (float)-local.Y;
gyro.Roll  = (float)-local.Z;
```

### IGC 跨网格通信

- 必须先 `RegisterBroadcastListener(tag)` 才能收到广播
- 每次 `Main` 调用中用 `listener.HasPendingMessage` 轮询，SE 不支持事件回调
- 单播地址通过 `IGC.Me` 获取（`long` 类型）

### 其他

- C# **语言版本为 6**，不能用模式匹配、元组、本地函数、`is` 类型匹配等 C# 7+ 特性
- 禁用 `System.IO`、`System.Net`、`System.Reflection`、`unsafe` 代码
- `Storage` 字段存储在 PB 方块的状态里：随世界存档保存（游戏加载时恢复），也随蓝图一起转移（复制/粘贴飞船时携带）；脚本重编译前 `Save()` 会被自动调用，因此 Storage **也在重编译后持久**
