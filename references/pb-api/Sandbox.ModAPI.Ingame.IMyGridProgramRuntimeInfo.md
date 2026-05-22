**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyGridProgramRuntimeInfo
```

Provides runtime info for a running grid program.

## Properties

|Member|Description|
|---|---|
|[CurrentCallChainDepth](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@CurrentCallChainDepth)|Gets the current number of nested method calls.|
|[CurrentInstructionCount](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@CurrentInstructionCount)|Gets the current number of significant instructions executed.|
|[LastRunTimeMs](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@LastRunTimeMs)|Gets the number of milliseconds it took to execute the Main method the last time it was run. This property returns no valid data neither in the constructor nor the Save method.|
|[LifetimeTicks](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@LifetimeTicks)|The number of ticks this program has been running for.|
|[MaxCallChainDepth](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@MaxCallChainDepth)|Gets the maximum number of method calls that can be nested into each other.|
|[MaxInstructionCount](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@MaxInstructionCount)|Gets the maximum number of significant instructions that can be executing during a single run, including any other programmable blocks invoked immediately.|
|[TimeSinceLastRun](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@TimeSinceLastRun)|Gets the time elapsed since the last time the Main method of this program was run. This property returns no valid data neither in the constructor nor the Save method.|
|[UpdateFrequency](Sandbox.ModAPI.Ingame.IMyGridProgramRuntimeInfo@UpdateFrequency)|Gets or sets how frequently this script will run itself|

