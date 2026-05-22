**Assembly:** Sandbox.Common.dll

```csharp
public struct MyDetectedEntityInfo
```

Describes detected entity info

## Fields

|Member|Description|
|---|---|
|[BoundingBox](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@BoundingBox)|The entity's world-aligned bounding box|
|[EntityId](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@EntityId)|The entity's EntityId|
|[HitPosition](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@HitPosition)|Position where the raycast hit the entity. (can be null if the sensor didn't use a raycast)|
|[Name](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@Name)|The entity's display name if it is friendly, or a generic descriptor if it is not|
|[Orientation](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@Orientation)|The entity's absolute orientation at the time it was detected|
|[Relationship](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@Relationship)|Relationship between the entity and the owner of the sensor|
|[TimeStamp](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@TimeStamp)|Time when the entity was detected. This field counts milliseconds, compensated for simspeed|
|[Type](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@Type)|Enum describing the type of entity|
|[Velocity](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@Velocity)|The entity's absolute velocity at the time it was detected|

## Properties

|Member|Description|
|---|---|
|[Position](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@Position)|The entity's position (center of the Bounding Box)|

## Constructors

|Member|Description|
|---|---|
|[MyDetectedEntityInfo(long, string, MyDetectedEntityType, Vector3D?, MatrixD, Vector3, MyRelationsBetweenPlayerAndBlock, BoundingBoxD, long)](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@.ctor)||

## Methods

|Member|Description|
|---|---|
|[IsEmpty()](Sandbox.ModAPI.Ingame.MyDetectedEntityInfo@IsEmpty)|Determines if this structure is empty; meaning it does not contain any meaningful data|

