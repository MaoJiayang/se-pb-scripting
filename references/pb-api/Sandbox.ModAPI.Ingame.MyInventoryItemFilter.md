**Assembly:** Sandbox.Common.dll

```csharp
public struct MyInventoryItemFilter
```

Implements inventory item filter

## Fields

|Member|Description|
|---|---|
|[AllSubTypes](Sandbox.ModAPI.Ingame.MyInventoryItemFilter@AllSubTypes)|Determines whether all subtypes of the given item ID should pass this filter check.|
|[ItemId](Sandbox.ModAPI.Ingame.MyInventoryItemFilter@ItemId)|Specifies an item to filter. Set [AllSubTypes](Sandbox.ModAPI.Ingame.MyInventoryItemFilter@AllSubTypes) to true to only check the main type part of this ID.|

## Properties

|Member|Description|
|---|---|
|[ItemType](Sandbox.ModAPI.Ingame.MyInventoryItemFilter@ItemType)||

## Constructors

|Member|Description|
|---|---|
|[MyInventoryItemFilter(string, bool)](Sandbox.ModAPI.Ingame.MyInventoryItemFilter@.ctor)||
|[MyInventoryItemFilter(MyDefinitionId, bool)](Sandbox.ModAPI.Ingame.MyInventoryItemFilter@.ctor)||

