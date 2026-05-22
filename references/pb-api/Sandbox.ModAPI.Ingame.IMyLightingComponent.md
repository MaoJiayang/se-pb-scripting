**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyLightingComponent
```

Describes a lighting Component (PB scripting interface).

## Properties

|Member|Description|
|---|---|
|[BlinkIntervalSeconds](Sandbox.ModAPI.Ingame.IMyLightingComponent@BlinkIntervalSeconds)|Gets or sets the blinking interval of this light (in seconds).|
|[BlinkLength](Sandbox.ModAPI.Ingame.IMyLightingComponent@BlinkLength)|Gets or sets how much of the blinking interval should be spent with the light on, as a value between 0 and 1.|
|[BlinkOffset](Sandbox.ModAPI.Ingame.IMyLightingComponent@BlinkOffset)|Adds an offset to the blinking interval, as a value between 0 and 1.|
|[Color](Sandbox.ModAPI.Ingame.IMyLightingComponent@Color)|Gets or sets the color of the light.|
|[Falloff](Sandbox.ModAPI.Ingame.IMyLightingComponent@Falloff)|Gets or sets the current falloff of the light.|
|[Intensity](Sandbox.ModAPI.Ingame.IMyLightingComponent@Intensity)|Gets or sets the current intensity of the light.|
|[Radius](Sandbox.ModAPI.Ingame.IMyLightingComponent@Radius)|Gets or sets the basic radius of the light.|

