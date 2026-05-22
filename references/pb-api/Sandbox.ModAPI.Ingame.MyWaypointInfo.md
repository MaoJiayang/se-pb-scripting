**Assembly:** Sandbox.Common.dll

```csharp
public struct MyWaypointInfo: IEquatable<MyWaypointInfo>
```

Represents a GPS coordinate

## Fields

|Member|Description|
|---|---|
|[static Empty](Sandbox.ModAPI.Ingame.MyWaypointInfo@Empty)|Returns an empty (undefined) GPS coordinate|
|[Coords](Sandbox.ModAPI.Ingame.MyWaypointInfo@Coords)|Gets the target coordinate as a [Vector3D](VRageMath.Vector3D) |
|[Name](Sandbox.ModAPI.Ingame.MyWaypointInfo@Name)|The name of this GPS coordinate|

## Constructors

|Member|Description|
|---|---|
|[MyWaypointInfo(string, double, double, double)](Sandbox.ModAPI.Ingame.MyWaypointInfo@.ctor)||
|[MyWaypointInfo(string, Vector3D)](Sandbox.ModAPI.Ingame.MyWaypointInfo@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static FindAll(string, List<MyWaypointInfo>)](Sandbox.ModAPI.Ingame.MyWaypointInfo@FindAll)|Searches for all GPS coordinates in the given text.|
|[static TryParse(string, out MyWaypointInfo)](Sandbox.ModAPI.Ingame.MyWaypointInfo@TryParse)|Attempts to parse a GPS coordinate from the given text. The text cannot contain anything but the GPS coordinate.<br /><br />A GPS coordinate has the format GPS:Name:X:Y:Z:|
|[Equals(MyWaypointInfo)](Sandbox.ModAPI.Ingame.MyWaypointInfo@Equals)|Determines whether this coordinate is the same as another. Uses 0.0001 as the epsilon to counter floating point inaccuracies.|
|[Equals(MyWaypointInfo, double)](Sandbox.ModAPI.Ingame.MyWaypointInfo@Equals)|Determines whether this coordinate is the same as another. Uses 0.0001 as the epsilon to counter floating point inaccuracies.|
|[Equals(object)](Sandbox.ModAPI.Ingame.MyWaypointInfo@Equals)|Determines whether this coordinate is the same as another. Uses 0.0001 as the epsilon to counter floating point inaccuracies.|
|[GetHashCode()](Sandbox.ModAPI.Ingame.MyWaypointInfo@GetHashCode)|Gets the hashcode of this coordinate|
|[IsEmpty()](Sandbox.ModAPI.Ingame.MyWaypointInfo@IsEmpty)|Determines whether this coordinate is empty (undefined)|
|[ToString()](Sandbox.ModAPI.Ingame.MyWaypointInfo@ToString)|Converts this GPS coordinate to its string equivalent|

**Implements:**  
* [IEquatable<MyWaypointInfo>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

