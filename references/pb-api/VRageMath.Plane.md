**Assembly:** VRage.Math.dll

```csharp
public struct Plane: IEquatable<Plane>
```

Defines a plane.

## Fields

|Member|Description|
|---|---|
|[D](VRageMath.Plane@D)|The distance of the Plane along its normal from the origin. Note: Be careful! The distance is signed and is the opposite of what people usually expect. If you look closely at the plane equation: (n dot P) - D = 0, you'll realize that D = - (n dot P) (that is, negative instead of positive)|
|[Normal](VRageMath.Plane@Normal)|The normal vector of the Plane.|

## Constructors

|Member|Description|
|---|---|
|[Plane(float, float, float, float)](VRageMath.Plane@.ctor)||
|[Plane(Vector3, float)](VRageMath.Plane@.ctor)||
|[Plane(Vector3, Vector3)](VRageMath.Plane@.ctor)||
|[Plane(Vector4)](VRageMath.Plane@.ctor)||
|[Plane(Vector3, Vector3, Vector3)](VRageMath.Plane@.ctor)||
|[Plane(ref Vector3, ref Vector3, ref Vector3)](VRageMath.Plane@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Normalize(Plane)](VRageMath.Plane@Normalize)|Changes the coefficients of the Normal vector of a Plane to make it of unit length.|
|[static Normalize(ref Plane, out Plane)](VRageMath.Plane@Normalize)|Changes the coefficients of the Normal vector of a Plane to make it of unit length.|
|[static Transform(Plane, Matrix)](VRageMath.Plane@Transform)|Transforms a normalized Plane by a Matrix.|
|[static Transform(ref Plane, ref Matrix, out Plane)](VRageMath.Plane@Transform)|Transforms a normalized Plane by a Matrix.|
|[Dot(Vector4)](VRageMath.Plane@Dot)|Calculates the dot product of a specified Vector4 and this Plane.|
|[Dot(ref Vector4, out float)](VRageMath.Plane@Dot)|Calculates the dot product of a specified Vector4 and this Plane.|
|[DotCoordinate(Vector3)](VRageMath.Plane@DotCoordinate)|Returns the dot product of a specified Vector3 and the Normal vector of this Plane plus the distance (D) value of the Plane.|
|[DotCoordinate(ref Vector3, out float)](VRageMath.Plane@DotCoordinate)|Returns the dot product of a specified Vector3 and the Normal vector of this Plane plus the distance (D) value of the Plane.|
|[DotNormal(Vector3D)](VRageMath.Plane@DotNormal)|Returns the dot product of a specified Vector3 and the Normal vector of this Plane.|
|[DotNormal(ref Vector3, out float)](VRageMath.Plane@DotNormal)|Returns the dot product of a specified Vector3 and the Normal vector of this Plane.|
|[Equals(Plane)](VRageMath.Plane@Equals)|Determines whether the specified Plane is equal to the Plane.|
|[Equals(object)](VRageMath.Plane@Equals)|Determines whether the specified Object is equal to the Plane.|
|[GetHashCode()](VRageMath.Plane@GetHashCode)|Gets the hash code for this object.|
|[Intersection(ref Vector3D, ref Vector3D)](VRageMath.Plane@Intersection)|Gets intersection point in Plane.|
|[Intersects(BoundingBox)](VRageMath.Plane@Intersects)|Checks whether the current Plane intersects a specified BoundingBox.|
|[Intersects(ref BoundingBox, out PlaneIntersectionType)](VRageMath.Plane@Intersects)|Checks whether the current Plane intersects a BoundingBox.|
|[Intersects(BoundingFrustum)](VRageMath.Plane@Intersects)|Checks whether the current Plane intersects a specified BoundingFrustum.|
|[Intersects(BoundingSphere)](VRageMath.Plane@Intersects)|Checks whether the current Plane intersects a specified BoundingSphere.|
|[Intersects(ref BoundingSphere, out PlaneIntersectionType)](VRageMath.Plane@Intersects)|Checks whether the current Plane intersects a BoundingSphere.|
|[Normalize()](VRageMath.Plane@Normalize)|Changes the coefficients of the Normal vector of this Plane to make it of unit length.|
|[RandomPoint()](VRageMath.Plane@RandomPoint)||
|[ToString()](VRageMath.Plane@ToString)|Returns a String that represents the current Plane.|

**Implements:**  
* [IEquatable<Plane>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

