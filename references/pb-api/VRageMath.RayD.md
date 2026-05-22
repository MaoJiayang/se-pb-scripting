**Assembly:** VRage.Math.dll

```csharp
public struct RayD: IEquatable<RayD>
```

Defines a ray.

## Fields

|Member|Description|
|---|---|
|[Direction](VRageMath.RayD@Direction)|Unit vector specifying the direction the Ray is pointing.|
|[Position](VRageMath.RayD@Position)|Specifies the starting point of the Ray.|

## Constructors

|Member|Description|
|---|---|
|[RayD(Vector3D, Vector3D)](VRageMath.RayD@.ctor)||
|[RayD(ref Vector3D, ref Vector3D)](VRageMath.RayD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[Equals(RayD)](VRageMath.RayD@Equals)|Determines whether the specified Ray is equal to the current Ray.|
|[Equals(object)](VRageMath.RayD@Equals)|Determines whether two instances of Ray are equal.|
|[GetHashCode()](VRageMath.RayD@GetHashCode)|Gets the hash code for this instance.|
|[Intersects(BoundingBoxD)](VRageMath.RayD@Intersects)|Checks whether the Ray intersects a specified BoundingBox.|
|[Intersects(ref BoundingBoxD, out double?)](VRageMath.RayD@Intersects)|Checks whether the current Ray intersects a BoundingBox.|
|[Intersects(BoundingFrustumD)](VRageMath.RayD@Intersects)|Checks whether the Ray intersects a specified BoundingFrustum.|
|[Intersects(PlaneD)](VRageMath.RayD@Intersects)|Determines whether this Ray intersects a specified Plane.|
|[Intersects(ref PlaneD, out double?)](VRageMath.RayD@Intersects)|Determines whether this Ray intersects a specified Plane.|
|[Intersects(BoundingSphereD)](VRageMath.RayD@Intersects)|Checks whether the Ray intersects a specified BoundingSphere.|
|[Intersects(ref BoundingSphere, out double?)](VRageMath.RayD@Intersects)|Checks whether the current Ray intersects a BoundingSphere.|
|[ToString()](VRageMath.RayD@ToString)|Returns a String that represents the current Ray.|

**Implements:**  
* [IEquatable<RayD>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

