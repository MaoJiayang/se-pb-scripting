**Assembly:** Sandbox.Common.dll

```csharp
public enum UpdateType
```

Enum describes what source triggered the script to run.

## Fields

|Member|Description|
|---|---|
|IGC|Script run by intergrid communication system.|
|Mod|Script run by a mod.|
|None|None|
|Once|Script is updating once before the tick.|
|Script|Script run by another programmable block.|
|Terminal|Script run by user in the terminal.|
|Trigger|Script run by a block such as timer, sensor.|
|Update1|Script is updating every tick.|
|Update10|Script is updating every 10th tick.|
|Update100|Script is updating every 100th tick.|

