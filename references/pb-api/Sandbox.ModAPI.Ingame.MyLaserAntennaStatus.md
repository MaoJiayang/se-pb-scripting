**Assembly:** Sandbox.Common.dll

```csharp
public enum MyLaserAntennaStatus
```

Describes the current status of a laser antenna.

## Fields

|Member|Description|
|---|---|
|Connected|Currently connected to a laser antenna.|
|Connecting|Currently connecting to a laser antenna.|
|Idle|Not doing anything and not connected.|
|OutOfRange|The target antenna is out of range.|
|RotatingToTarget|Currently rotating towards the currently selected target.|
|SearchingTargetForAntenna|Currently searching for a laser antenna at the target.|

