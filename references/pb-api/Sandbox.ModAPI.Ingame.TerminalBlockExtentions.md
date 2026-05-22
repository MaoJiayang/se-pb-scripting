**Assembly:** Sandbox.Common.dll

```csharp
public abstract sealed class TerminalBlockExtentions
```

Class having some sugar extensions. Written by Kalvin Osborne, AKA Night Lone.

## Methods

|Member|Description|
|---|---|
|[static ApplyAction(this IMyTerminalBlock, string)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@ApplyAction)|Finds action by [GetActionWithName(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetActionWithName) and calls [Apply(IMyCubeBlock)](Sandbox.ModAPI.Interfaces.ITerminalAction@Apply) |
|[static ApplyAction(this IMyTerminalBlock, string, List<TerminalActionParameter>)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@ApplyAction)|Finds action by [GetActionWithName(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetActionWithName) and calls [Apply(IMyCubeBlock, ListReader<TerminalActionParameter>)](Sandbox.ModAPI.Interfaces.ITerminalAction@Apply) |
|[static GetId(this IMyTerminalBlock)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@GetId)|Get EntityId of block|
|[static HasAction(this IMyTerminalBlock, string)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@HasAction)|Searches for terminal action with name|
|[static GetInventory(this IMyTerminalBlock, int)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@GetInventory)|_**Obsolete:** Use the GetInventoryBase method._<br /><br />Obsolete|
|[static GetInventoryCount(this IMyTerminalBlock)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@GetInventoryCount)|_**Obsolete:** Use the InventoryCount property._<br /><br />Obsolete|
|[static GetUseConveyorSystem(this IMyTerminalBlock)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@GetUseConveyorSystem)|_**Obsolete:** Use the blocks themselves, this method is no longer reliable_<br /><br />Obsolete|
|[static HasInventory(this IMyTerminalBlock)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@HasInventory)|_**Obsolete:** Use the HasInventory property._<br /><br />Obsolete|
|[static SetUseConveyorSystem(this IMyTerminalBlock, bool)](Sandbox.ModAPI.Ingame.TerminalBlockExtentions@SetUseConveyorSystem)|_**Obsolete:** Use the blocks themselves, this method is no longer reliable_<br /><br />Obsolete|

