**Assembly:** Sandbox.Common.dll

```csharp
public interface IUserCustomizableTerminalAction
```

Describes terminal action that allows capturing custom arguments and setting toolbar icon title

## Properties

|Member|Description|
|---|---|
|[Parameters](Sandbox.ModAPI.Ingame.IUserCustomizableTerminalAction@Parameters)|Collection of [TerminalActionParameter](Sandbox.ModAPI.Ingame.TerminalActionParameter) that are associated with a toolbar item|

## Methods

|Member|Description|
|---|---|
|[FetchAllBlocks(List<IMyTerminalBlock>)](Sandbox.ModAPI.Ingame.IUserCustomizableTerminalAction@FetchAllBlocks)|Gets all blocks the action is associated with|
|[GetBlock()](Sandbox.ModAPI.Ingame.IUserCustomizableTerminalAction@GetBlock)|Gets the block the action is associated with|
|[SetCustomIconTitle(string)](Sandbox.ModAPI.Ingame.IUserCustomizableTerminalAction@SetCustomIconTitle)|Sets custom title for toolbar icon|

