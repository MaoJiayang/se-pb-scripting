**Assembly:** Sandbox.Common.dll

```csharp
public enum UpdateFrequency
```

Flags set how often the script will run itself.

## Fields

|Member|Description|
|---|---|
|None|Does not run autonomously.|
|Once|Run once before the next tick. Flag is un-set automatically after the update|
|Update1|Run every game tick.|
|Update10|Run every 10th game tick.|
|Update100|Run every 100th game tick.|

