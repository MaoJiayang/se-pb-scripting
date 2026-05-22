**Assembly:** VRage.Math.dll

```csharp
public struct Ray: IEquatable<Ray>
```

Defines a ray.

## Fields

|Member|Description|
|---|---|
|[Direction](VRageMath.Ray@Direction)|Unit vector specifying the direction the Ray is pointing.|
|[Position](VRageMath.Ray@Position)|Specifies the starting point of the Ray.|

## Constructors

|Member|Description|
|---|---|
|[Ray(Vector3, Vector3)](VRageMath.Ray@.ctor)||

## Methods

|Member|Description|
|---|---|
|[Equals(Ray)](VRageMath.Ray@Equals)|Determines whether the specified Ray is equal to the current Ray.|
|[Equals(object)](VRageMath.Ray@Equals)|Determines whether two instances of Ray are equal.|
|[GetHashCode()](VRageMath.Ray@GetHashCode)|Gets the hash code for this instance.|
|[Intersects(BoundingBox)](VRageMath.Ray@Intersects)|Checks whether the Ray intersects a specified BoundingBox.|
|[Intersects(ref BoundingBox, out float?)](VRageMath.Ray@Intersects)|Checks whether the current Ray intersects a BoundingBox.|
|[Intersects(BoundingFrustum)](VRageMath.Ray@Intersects)|Checks whether the Ray intersects a specified BoundingFrustum.|
|[Intersects(Plane)](VRageMath.Ray@Intersects)|Determines whether this Ray intersects a specified Plane.|
|[Intersects(ref Plane, out float?)](VRageMath.Ray@Intersects)|Determines whether this Ray intersects a specified Plane.|
|[Intersects(BoundingSphere)](VRageMath.Ray@Intersects)|Checks whether the Ray intersects a specified BoundingSphere.|
|[Intersects(ref BoundingSphere, out float?)](VRageMath.Ray@Intersects)|Checks whether the current Ray intersects a BoundingSphere.|
|[ToString()](VRageMath.Ray@ToString)|Returns a String that represents the current Ray.|

**Implements:**  
* [IEquatable<Ray>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

