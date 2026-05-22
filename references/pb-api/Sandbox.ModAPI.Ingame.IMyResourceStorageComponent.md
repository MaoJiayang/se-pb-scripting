**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyResourceStorageComponent
```

Describes a resource storage entity component for scripting

## Properties

|Member|Description|
|---|---|
|[FilledRatio](Sandbox.ModAPI.Ingame.IMyResourceStorageComponent@FilledRatio)|Gets the current fill level of this storage as a value between 0 (empty) and 1 (full).|
|[ResourceCapacity](Sandbox.ModAPI.Ingame.IMyResourceStorageComponent@ResourceCapacity)|Gets the resource capacity of this tank.|

## Methods

|Member|Description|
|---|---|
|[IsResourceStorage(MyDefinitionId)](Sandbox.ModAPI.Ingame.IMyResourceStorageComponent@IsResourceStorage)|Can the storage store a specified resource?|

