---
name: se-pb-scripting
description: "Space Engineers 可编程方块脚本开发技能。用于：编写 SE PB 脚本、查阅 SE PB API、基于 MDK2 框架初始化新项目、理解 SE 脚本限制与最佳实践、调试 SE 脚本。触发词：SE、Space Engineers、可编程方块、PB script、MDK2、IMyThrust、IMyGyro、GridTerminalSystem 等 SE API。"
---

# Space Engineers 可编程方块脚本开发

本 Skill 适用于所有 SE PB 脚本相关工作。**详细 API 参考和初始化说明见 references/ 目录**，下面仅提供核心约束和快速入口。

## references/ 目录说明

| 路径 | 内容 |
|------|------|
| [references/se-gotchas.md](./references/se-gotchas.md) | 枚举速查、VRageMath 代码片段、方块查找模式、踩坑注意事项 |
| [references/project-init.md](./references/project-init.md) | MDK2 项目初始化、打包、配置详细说明 |
| [references/se-patterns.md](./references/se-patterns.md) | 参数管理器范式骨架代码、PID/CircularQueue/MovingAverageQueue 用法 |
| `references/pb-api/` | 所有 PB 可用接口的完整类型文档（每个接口一个 .md 文件） |

### 查找接口文档

需要某个接口的完整成员列表时，直接在 `references/pb-api/` 中搜索对应文件名，例如：
- `Sandbox.ModAPI.Ingame.IMyThrust.md` → 推进器接口
- `VRageMath.Vector3D.md` → Vector3D 类
- `List-Of-Terminal-Properties-And-Actions.md` → 所有终端方块属性与动作完整清单

### pb-api/ 目录缺失时

如果 `references/pb-api/` 为空或不存在，**在继续之前告知用户需要先运行同步脚本**：

```
需要先同步 SE API 文档，请在 skill 仓库根目录执行：
    python scripts/sync-pb-api.py
（首次运行会自动 clone malforge/malforge.github.io，约需几分钟）
```

同步完成后再继续任务。

---

## 第一步：项目初始化检查

**每次开始工作前必须确认**当前项目已通过 MDK2 初始化，判断依据（同时满足）：

1. 工作区存在 `mdk.ini`（含 `type=programmableblock`）
2. `*.csproj` 中引用了 `Mal.Mdk2.PbAnalyzers`、`Mal.Mdk2.PbPackager`、`Mal.Mdk2.References`
3. `Program.cs` 存在且主类继承自 `MyGridProgram`

**未初始化时**：参考 [references/project-init.md](./references/project-init.md) 执行初始化命令。

---

## SE PB 脚本关键约束

- **语言版本**：C# 6（无模式匹配、元组、本地函数等 C# 7+ 特性）
- **命名空间**：必须为 `IngameScript`，打包时被剥离
- **指令上限**：每次运行约 50,000 个 code junctions（方法调用、条件、循环等）；脚本字符上限 100,000
- **禁用**：`System.IO`、`System.Net`、`System.Reflection`、unsafe、静态构造函数
- **入口**：继承 `MyGridProgram`，实现 `Main(string argument, UpdateType updateSource)`

### 内置变量（来自 MyGridProgram）

| 变量 | 类型 | 说明 |
|------|------|------|
| `GridTerminalSystem` | `IMyGridTerminalSystem` | 同构造体内所有方块 |
| `Me` | `IMyProgrammableBlock` | PB 自身 |
| `Echo` | `Action<string>` | 输出到 PB 详情区 |
| `Runtime` | `IMyGridProgramRuntimeInfo` | 时间差、指令计数、更新频率 |
| `Storage` | `string` | 跨会话持久化 |
| `IGC` | `IMyIntergridCommunicationSystem` | 跨网格通信 |

### 脚本骨架

```csharp
namespace IngameScript
{
    partial class Program : MyGridProgram
    {
        public Program()
        {
            Runtime.UpdateFrequency = UpdateFrequency.Update10;
        }

        public void Save() { Storage = "..."; }

        public void Main(string argument, UpdateType updateSource)
        {
            Echo("running");
        }
    }
}
```

详细陷阱与代码模式见 [references/se-gotchas.md](./references/se-gotchas.md)。

---

## 参数管理器范式 & 通用工具

**新建项目或添加可调参数时**，参考 [references/se-patterns.md](./references/se-patterns.md)：

- **参数管理器**：将可调超参数集中在一个类中，自动读写 `Me.CustomData`（`key = value` 格式，支持注释）。新参数：声明属性 → 在 `注册所有参数()` 中注册委托，两步完成。
- **PID / PID3**：单轴/三轴 PID，支持输出限幅与 Back-calculation 抗饱和。
- **CircularQueue\<T\>**：定容环形缓冲区，O(1) 插入和按龄索引。
- **MovingAverageQueue\<T\>**：继承 CircularQueue，O(1) 滑动均值，委托支持任意类型。
