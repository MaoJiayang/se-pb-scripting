**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyGridTerminalSystem
```

Describes terminal system (PB scripting interface)

## Methods

|Member|Description|
|---|---|
|[CanAccess(IMyTerminalBlock, MyTerminalAccessScope)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@CanAccess)|Checks if the grid terminal system can still access the given [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock) . A block is no longer accessible if it's destroyed, detached, it's ownership has changed or is otherwise disconnected from this grid terminal system.|
|[CanAccess(IMyCubeGrid, MyTerminalAccessScope)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@CanAccess)|Checks if the grid terminal system can still access the given [IMyCubeGrid](VRage.Game.ModAPI.Ingame.IMyCubeGrid) . A grid is no longer accessible if it's destroyed, detached, it's ownership has changed or is otherwise disconnected from this grid terminal system.|
|[GetBlockGroups(List<IMyBlockGroup>, Func<IMyBlockGroup, bool>)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlockGroups)|Fills the provided list with the block groups reachable by this grid terminal system.|
|[GetBlockGroupWithName(string)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlockGroupWithName)|Returns the first block group found with the given name. Will return`null`if no block group with that name can be found.|
|[GetBlocks(List<IMyTerminalBlock>)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlocks)|Fills the provided list with all the blocks reachable by this grid terminal system. This means all blocks on the same grid, or connected via rotors, pistons or connectors.|
|[GetBlocksOfType<T>(List<IMyTerminalBlock>, Func<IMyTerminalBlock, bool>)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlocksOfType{T})||
|[GetBlocksOfType<T>(List<T>, Func<T, bool>)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlocksOfType{T})||
|[GetBlockWithId(long)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlockWithId)|Attempts to retrieve the block with the given entity ID.|
|[GetBlockWithName(string)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@GetBlockWithName)|Returns the first block found with the given name.|
|[SearchBlocksOfName(string, List<IMyTerminalBlock>, Func<IMyTerminalBlock, bool>)](Sandbox.ModAPI.Ingame.IMyGridTerminalSystem@SearchBlocksOfName)|Fills the provided list with the blocks reachable by this grid terminal system. This means all blocks on the same grid, or connected via rotors, pistons or connectors.|

