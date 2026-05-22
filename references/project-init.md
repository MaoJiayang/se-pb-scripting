# MDK2 SE PB 项目初始化

## 前置：安装 MDK2 模板（首次使用一次性操作）

```powershell
dotnet new install Mal.Mdk2.Templates
```

验证是否安装（输出中应有 `mdk2pbscript`）：

```powershell
dotnet new list | Select-String mdk2
```

---

## 新建项目（一条命令完成）

```powershell
dotnet new mdk2pbscript -n <项目名> -o <项目名>
```

执行后会在 `<项目名>/` 目录下生成完整的空项目，包含：

| 文件 | 说明 |
|------|------|
| `<项目名>.csproj` | 已配置 MDK2 包引用，无需手动修改 |
| `<项目名>.mdk.ini` | 项目级配置（提交到 git）|
| `<项目名>.mdk.local.ini` | 本机输出路径配置（**不要提交到 git**）|
| `Program.cs` | 继承 MyGridProgram 的空脚本骨架 |
| `Instructions.readme` | 内容会被注入到发布脚本的开头 |

---

## 必填配置：本机输出路径

编辑 `*.mdk.local.ini`，填写 SE 存档中 IngameScripts 的路径：

```ini
[mdk]
outputpath=C:\Users\<用户名>\AppData\Roaming\SpaceEngineers\IngameScripts\local
```

---

## mdk.ini 常用选项

```ini
[mdk]
type=programmableblock      ; 不要改

; 压缩级别（影响发布脚本的字符数）
; none | trim | stripcomments | lite | full
minify=none

; 排除文件（glob 格式）
ignores=obj/**/*,MDK/**/*,**/*.debug.cs

; 允许的命名空间（打包时被剥离）
namespaces=IngameScript
```

---

## Instructions.readme

项目根目录下的 `Instructions.readme` 中的文字会被**注入到发布脚本的开头**（即创意工坊脚本的顶部注释）。不需要时直接删除此文件即可。

---

## 构建 / 发布

```powershell
dotnet build -c Release
```

VS Code 中也可以用 `Ctrl+Shift+B` → 选择发布任务。

---

## 推荐的 .gitignore（SE 项目）

```gitignore
bin/
obj/
.vs/
*.user
*.mdk.local.ini
thumb.png
```

`*.mdk.local.ini` 包含本机路径，务必加入 .gitignore，不要提交。
