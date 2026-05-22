**Assembly:** VRage.Math.dll

```csharp
public struct BoundingBoxD: IEquatable<BoundingBoxD>
```

Defines an axis-aligned box-shaped 3D volume.

## Fields

|Member|Description|
|---|---|
|[static Comparer](VRageMath.BoundingBoxD@Comparer)||
|[static NUMBER_OF_CORNERS](VRageMath.BoundingBoxD@NUMBER_OF_CORNERS)|Number of corners of the BB|
|[Max](VRageMath.BoundingBoxD@Max)|The maximum point the BoundingBox contains.|
|[Min](VRageMath.BoundingBoxD@Min)|The minimum point the BoundingBox contains.|

## Properties

|Member|Description|
|---|---|
|[Center](VRageMath.BoundingBoxD@Center)|Calculates center|
|[Extents](VRageMath.BoundingBoxD@Extents)||
|[HalfExtents](VRageMath.BoundingBoxD@HalfExtents)||
|[Matrix](VRageMath.BoundingBoxD@Matrix)|Matrix of AABB, respecting center and size|
|[Perimeter](VRageMath.BoundingBoxD@Perimeter)|return perimeter of edges|
|[Size](VRageMath.BoundingBoxD@Size)|Size|
|[SurfaceArea](VRageMath.BoundingBoxD@SurfaceArea)||
|[Valid](VRageMath.BoundingBoxD@Valid)||
|[Volume](VRageMath.BoundingBoxD@Volume)||

## Constructors

|Member|Description|
|---|---|
|[BoundingBoxD(Vector3D, Vector3D)](VRageMath.BoundingBoxD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateFromPoints(IEnumerable<Vector3D>)](VRageMath.BoundingBoxD@CreateFromPoints)|Creates the smallest BoundingBox that will contain a group of points.|
|[static CreateFromSphere(BoundingSphereD)](VRageMath.BoundingBoxD@CreateFromSphere)|Creates the smallest BoundingBox that will contain the specified BoundingSphere.|
|[static CreateFromSphere(ref BoundingSphereD, out BoundingBoxD)](VRageMath.BoundingBoxD@CreateFromSphere)|Creates the smallest BoundingBox that will contain the specified BoundingSphere.|
|[static CreateInvalid()](VRageMath.BoundingBoxD@CreateInvalid)||
|[static CreateMerged(BoundingBoxD, BoundingBoxD)](VRageMath.BoundingBoxD@CreateMerged)|Creates the smallest BoundingBox that contains the two specified BoundingBox instances.|
|[static CreateMerged(ref BoundingBoxD, ref BoundingBoxD, out BoundingBoxD)](VRageMath.BoundingBoxD@CreateMerged)|Creates the smallest BoundingBox that contains the two specified BoundingBox instances.|
|[AssertIsValid()](VRageMath.BoundingBoxD@AssertIsValid)||
|[Centerize(Vector3D)](VRageMath.BoundingBoxD@Centerize)||
|[Contains(BoundingBoxD)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains another BoundingBox.|
|[Contains(ref BoundingBoxD, out ContainmentType)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains a BoundingBox.|
|[Contains(BoundingFrustumD)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains a BoundingFrustum.|
|[Contains(Vector3D)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains a point.|
|[Contains(ref Vector3D, out ContainmentType)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains a point.|
|[Contains(BoundingSphereD)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains a BoundingSphere.|
|[Contains(ref BoundingSphereD, out ContainmentType)](VRageMath.BoundingBoxD@Contains)|Tests whether the BoundingBox contains a BoundingSphere.|
|[Distance(Vector3D)](VRageMath.BoundingBoxD@Distance)||
|[Distance(ref BoundingBoxD)](VRageMath.BoundingBoxD@Distance)||
|[DistanceSquared(Vector3D)](VRageMath.BoundingBoxD@DistanceSquared)||
|[DistanceSquared(ref Vector3D)](VRageMath.BoundingBoxD@DistanceSquared)||
|[DistanceSquared(ref BoundingBoxD)](VRageMath.BoundingBoxD@DistanceSquared)||
|[Equals(BoundingBoxD)](VRageMath.BoundingBoxD@Equals)|Determines whether two instances of BoundingBox are equal.|
|[Equals(object)](VRageMath.BoundingBoxD@Equals)|Determines whether two instances of BoundingBox are equal.|
|[Equals(BoundingBoxD, double)](VRageMath.BoundingBoxD@Equals)||
|[GetCorner(int)](VRageMath.BoundingBoxD@GetCorner)|Gets corner of the BB by index|
|[GetCornersUnsafe(*Vector3D)](VRageMath.BoundingBoxD@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingBoxD@GetHashCode)|Gets the hash code for this instance.|
|[GetInflated(double)](VRageMath.BoundingBoxD@GetInflated)||
|[GetInflated(Vector3)](VRageMath.BoundingBoxD@GetInflated)||
|[GetInflated(Vector3D)](VRageMath.BoundingBoxD@GetInflated)||
|[Include(ref Vector3D)](VRageMath.BoundingBoxD@Include)|return expanded aabb (aabb include point)|
|[Include(Vector3D)](VRageMath.BoundingBoxD@Include)||
|[Include(Vector3D, Vector3D, Vector3D)](VRageMath.BoundingBoxD@Include)||
|[Include(ref Vector3D, ref Vector3D, ref Vector3D)](VRageMath.BoundingBoxD@Include)||
|[Include(ref BoundingBoxD)](VRageMath.BoundingBoxD@Include)|return expanded aabb (aabb include aabb)|
|[Include(BoundingBoxD)](VRageMath.BoundingBoxD@Include)||
|[Include(ref LineD)](VRageMath.BoundingBoxD@Include)||
|[Include(BoundingSphereD)](VRageMath.BoundingBoxD@Include)||
|[Include(ref BoundingSphereD)](VRageMath.BoundingBoxD@Include)||
|[Include(ref BoundingFrustumD)](VRageMath.BoundingBoxD@Include)||
|[Inflate(double)](VRageMath.BoundingBoxD@Inflate)||
|[Inflate(Vector3D)](VRageMath.BoundingBoxD@Inflate)||
|[InflateToMinimum(Vector3D)](VRageMath.BoundingBoxD@InflateToMinimum)||
|[InflateToMinimum(double)](VRageMath.BoundingBoxD@InflateToMinimum)||
|[Intersect(BoundingBoxD)](VRageMath.BoundingBoxD@Intersect)|Returns bounding box which is intersection of this and box Result is invalid box when there's no intersection (Min > Max)|
|[Intersect(ref LineD, out LineD)](VRageMath.BoundingBoxD@Intersect)||
|[Intersect(ref LineD, out double, out double)](VRageMath.BoundingBoxD@Intersect)||
|[Intersect(ref RayD, out double, out double)](VRageMath.BoundingBoxD@Intersect)||
|[Intersects(BoundingBoxD)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects another BoundingBox.|
|[Intersects(ref BoundingBoxD)](VRageMath.BoundingBoxD@Intersects)||
|[Intersects(ref BoundingBoxD, out bool)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects another BoundingBox.|
|[Intersects(ref BoundingBox, out bool)](VRageMath.BoundingBoxD@Intersects)||
|[Intersects(BoundingFrustumD)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a BoundingFrustum.|
|[Intersects(PlaneD)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a Plane.|
|[Intersects(ref PlaneD, out PlaneIntersectionType)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a Plane.|
|[Intersects(ref LineD)](VRageMath.BoundingBoxD@Intersects)||
|[Intersects(ref LineD, out double)](VRageMath.BoundingBoxD@Intersects)||
|[Intersects(Ray)](VRageMath.BoundingBoxD@Intersects)||
|[Intersects(RayD)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a Ray.|
|[Intersects(ref RayD, out double?)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a Ray.|
|[Intersects(BoundingSphereD)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a BoundingSphere.|
|[Intersects(ref BoundingSphereD, out bool)](VRageMath.BoundingBoxD@Intersects)|Checks whether the current BoundingBox intersects a BoundingSphere.|
|[Intersects(ref BoundingSphereD)](VRageMath.BoundingBoxD@Intersects)||
|[IntersectsTriangle(Vector3D, Vector3D, Vector3D)](VRageMath.BoundingBoxD@IntersectsTriangle)||
|[IntersectsTriangle(ref Vector3D, ref Vector3D, ref Vector3D)](VRageMath.BoundingBoxD@IntersectsTriangle)||
|[ProjectedArea(Vector3D)](VRageMath.BoundingBoxD@ProjectedArea)||
|[Round(int)](VRageMath.BoundingBoxD@Round)||
|[Round()](VRageMath.BoundingBoxD@Round)||
|[ToString()](VRageMath.BoundingBoxD@ToString)|Returns a String that represents the current BoundingBox.|
|[TransformFast(MatrixD)](VRageMath.BoundingBoxD@TransformFast)|Transform this AABB by matrix. Matrix has to be only rotation and translation.|
|[TransformFast(ref MatrixD)](VRageMath.BoundingBoxD@TransformFast)|Transform this AABB by matrix. Matrix has to be only rotation and translation.|
|[TransformFast(ref MatrixD, ref BoundingBoxD)](VRageMath.BoundingBoxD@TransformFast)|Transform this AABB by matrix. Matrix has to be only rotation and translation.|
|[TransformSlow(MatrixD)](VRageMath.BoundingBoxD@TransformSlow)|Transform this AABB by matrix.|
|[TransformSlow(ref MatrixD)](VRageMath.BoundingBoxD@TransformSlow)|Transform this AABB by matrix.|
|[Translate(MatrixD)](VRageMath.BoundingBoxD@Translate)|Translate|
|[Translate(Vector3D)](VRageMath.BoundingBoxD@Translate)|Translate|
|[GetCorners()](VRageMath.BoundingBoxD@GetCorners)|_**Obsolete:** Use GetCornersUnsafe or GetCorner._<br /><br />Gets an array of points that make up the corners of the BoundingBox. ALLOCATION!|
|[GetCorners(Vector3D[])](VRageMath.BoundingBoxD@GetCorners)|_**Obsolete:** Use GetCornersUnsafe or GetCorner._<br /><br />Gets the array of points that make up the corners of the BoundingBox.|

**Implements:**  
* [IEquatable<BoundingBoxD>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

