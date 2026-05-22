**Assembly:** VRage.Math.dll

```csharp
public class BoundingFrustumD: IEquatable<BoundingFrustumD>
```

Defines a frustum and helps determine whether forms intersect with it.

## Fields

|Member|Description|
|---|---|
|[static CornerCount](VRageMath.BoundingFrustumD@CornerCount)|Specifies the total number of corners (8) in the BoundingFrustumD.|

## Properties

|Member|Description|
|---|---|
|[Bottom](VRageMath.BoundingFrustumD@Bottom)|Gets the bottom plane of the BoundingFrustumD.|
|[Far](VRageMath.BoundingFrustumD@Far)|Gets the far plane of the BoundingFrustumD.|
|[Item](VRageMath.BoundingFrustumD@Item)||
|[Left](VRageMath.BoundingFrustumD@Left)|Gets the left plane of the BoundingFrustumD.|
|[Matrix](VRageMath.BoundingFrustumD@Matrix)|Gets or sets the Matrix that describes this bounding frustum.|
|[Near](VRageMath.BoundingFrustumD@Near)|Gets the near plane of the BoundingFrustumD.|
|[Right](VRageMath.BoundingFrustumD@Right)|Gets the right plane of the BoundingFrustumD.|
|[Top](VRageMath.BoundingFrustumD@Top)|Gets the top plane of the BoundingFrustumD.|

## Constructors

|Member|Description|
|---|---|
|[BoundingFrustumD()](VRageMath.BoundingFrustumD@.ctor)||
|[BoundingFrustumD(MatrixD)](VRageMath.BoundingFrustumD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[Contains(BoundingBoxD)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified BoundingBoxD.|
|[Contains(ref BoundingBoxD, out ContainmentType)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified BoundingBoxD.|
|[Contains(BoundingFrustumD)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified BoundingFrustumD.|
|[Contains(Vector3D)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified point.|
|[Contains(ref Vector3D, out ContainmentType)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified point.|
|[Contains(BoundingSphereD)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified BoundingSphere.|
|[Contains(ref BoundingSphereD, out ContainmentType)](VRageMath.BoundingFrustumD@Contains)|Checks whether the current BoundingFrustumD contains the specified BoundingSphere.|
|[Equals(BoundingFrustumD)](VRageMath.BoundingFrustumD@Equals)|Determines whether the specified BoundingFrustumD is equal to the current BoundingFrustumD.|
|[Equals(object)](VRageMath.BoundingFrustumD@Equals)|Determines whether the specified Object is equal to the BoundingFrustumD.|
|[GetCorners()](VRageMath.BoundingFrustumD@GetCorners)|Gets an array of points that make up the corners of the BoundingFrustumD. ALLOCATION!|
|[GetCorners(Vector3D[])](VRageMath.BoundingFrustumD@GetCorners)|Gets an array of points that make up the corners of the BoundingFrustumD.|
|[GetCornersUnsafe(*Vector3D)](VRageMath.BoundingFrustumD@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingFrustumD@GetHashCode)|Gets the hash code for this instance.|
|[Intersects(BoundingBoxD)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects the specified BoundingBoxD.|
|[Intersects(ref BoundingBoxD, out bool)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects a BoundingBoxD.|
|[Intersects(BoundingFrustumD)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects the specified BoundingFrustumD.|
|[Intersects(PlaneD)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects the specified Plane.|
|[Intersects(ref PlaneD, out PlaneIntersectionType)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects a Plane.|
|[Intersects(RayD)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects the specified Ray.|
|[Intersects(ref RayD, out double?)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects a Ray.|
|[Intersects(BoundingSphereD)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects the specified BoundingSphere.|
|[Intersects(ref BoundingSphereD, out bool)](VRageMath.BoundingFrustumD@Intersects)|Checks whether the current BoundingFrustumD intersects a BoundingSphere.|
|[ToString()](VRageMath.BoundingFrustumD@ToString)|Returns a String that represents the current BoundingFrustumD.|

**Implements:**  
* [IEquatable<BoundingFrustumD>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

