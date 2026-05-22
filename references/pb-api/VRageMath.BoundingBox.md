**Assembly:** VRage.Math.dll

```csharp
public struct BoundingBox: IEquatable<BoundingBox>
```

Defines an axis-aligned box-shaped 3D volume.

## Fields

|Member|Description|
|---|---|
|[static Comparer](VRageMath.BoundingBox@Comparer)||
|[static CornerCount](VRageMath.BoundingBox@CornerCount)|Specifies the total number of corners (8) in the BoundingBox.|
|[static Invalid](VRageMath.BoundingBox@Invalid)||
|[Max](VRageMath.BoundingBox@Max)|The maximum point the BoundingBox contains.|
|[Min](VRageMath.BoundingBox@Min)|The minimum point the BoundingBox contains.|

## Properties

|Member|Description|
|---|---|
|[Center](VRageMath.BoundingBox@Center)|Calculates center|
|[Corners](VRageMath.BoundingBox@Corners)||
|[Depth](VRageMath.BoundingBox@Depth)||
|[Extents](VRageMath.BoundingBox@Extents)||
|[HalfExtents](VRageMath.BoundingBox@HalfExtents)||
|[Height](VRageMath.BoundingBox@Height)||
|[Matrix](VRageMath.BoundingBox@Matrix)|Matrix of AABB, respecting center and size|
|[Perimeter](VRageMath.BoundingBox@Perimeter)|return perimeter of edges|
|[Size](VRageMath.BoundingBox@Size)|Size|
|[Width](VRageMath.BoundingBox@Width)||

## Constructors

|Member|Description|
|---|---|
|[BoundingBox(Vector3, Vector3)](VRageMath.BoundingBox@.ctor)||
|[BoundingBox(BoundingBoxD)](VRageMath.BoundingBox@.ctor)||
|[BoundingBox(BoundingBoxI)](VRageMath.BoundingBox@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateFromHalfExtent(Vector3, float)](VRageMath.BoundingBox@CreateFromHalfExtent)||
|[static CreateFromHalfExtent(Vector3, Vector3)](VRageMath.BoundingBox@CreateFromHalfExtent)||
|[static CreateFromPoints(IEnumerable<Vector3>)](VRageMath.BoundingBox@CreateFromPoints)|Creates the smallest BoundingBox that will contain a group of points.|
|[static CreateFromSphere(BoundingSphere)](VRageMath.BoundingBox@CreateFromSphere)|Creates the smallest BoundingBox that will contain the specified BoundingSphere.|
|[static CreateFromSphere(ref BoundingSphere, out BoundingBox)](VRageMath.BoundingBox@CreateFromSphere)|Creates the smallest BoundingBox that will contain the specified BoundingSphere.|
|[static CreateInvalid()](VRageMath.BoundingBox@CreateInvalid)||
|[static CreateMerged(BoundingBox, BoundingBox)](VRageMath.BoundingBox@CreateMerged)|Creates the smallest BoundingBox that contains the two specified BoundingBox instances.|
|[static CreateMerged(ref BoundingBox, ref BoundingBox, out BoundingBox)](VRageMath.BoundingBox@CreateMerged)|Creates the smallest BoundingBox that contains the two specified BoundingBox instances.|
|[static IsBetween(float, float, float)](VRageMath.BoundingBox@IsBetween)||
|[Contains(BoundingBox)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains another BoundingBox.|
|[Contains(ref BoundingBox, out ContainmentType)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains a BoundingBox.|
|[Contains(BoundingFrustum)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains a BoundingFrustum.|
|[Contains(Vector3)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains a point.|
|[Contains(Vector3D)](VRageMath.BoundingBox@Contains)||
|[Contains(ref Vector3, out ContainmentType)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains a point.|
|[Contains(BoundingSphere)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains a BoundingSphere.|
|[Contains(ref BoundingSphere, out ContainmentType)](VRageMath.BoundingBox@Contains)|Tests whether the BoundingBox contains a BoundingSphere.|
|[Distance(Vector3)](VRageMath.BoundingBox@Distance)||
|[DistanceSquared(Vector3)](VRageMath.BoundingBox@DistanceSquared)||
|[Equals(BoundingBox)](VRageMath.BoundingBox@Equals)|Determines whether two instances of BoundingBox are equal.|
|[Equals(object)](VRageMath.BoundingBox@Equals)|Determines whether two instances of BoundingBox are equal.|
|[Equals(BoundingBox, float)](VRageMath.BoundingBox@Equals)||
|[GetCorners()](VRageMath.BoundingBox@GetCorners)|Gets an array of points that make up the corners of the BoundingBox. ALLOCATION!|
|[GetCorners(Vector3[])](VRageMath.BoundingBox@GetCorners)|Gets the array of points that make up the corners of the BoundingBox.|
|[GetCornersUnsafe(*Vector3)](VRageMath.BoundingBox@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingBox@GetHashCode)|Gets the hash code for this instance.|
|[GetIncluded(Vector3)](VRageMath.BoundingBox@GetIncluded)||
|[Include(ref Vector3)](VRageMath.BoundingBox@Include)|return expanded aabb (aabb include point)|
|[Include(Vector3)](VRageMath.BoundingBox@Include)||
|[Include(Vector3, Vector3, Vector3)](VRageMath.BoundingBox@Include)||
|[Include(ref Vector3, ref Vector3, ref Vector3)](VRageMath.BoundingBox@Include)||
|[Include(ref BoundingBox)](VRageMath.BoundingBox@Include)|return expanded aabb (aabb include aabb)|
|[Include(BoundingBox)](VRageMath.BoundingBox@Include)||
|[Include(ref Line)](VRageMath.BoundingBox@Include)||
|[Include(BoundingSphere)](VRageMath.BoundingBox@Include)||
|[Include(ref BoundingSphere)](VRageMath.BoundingBox@Include)||
|[Include(ref BoundingFrustum)](VRageMath.BoundingBox@Include)||
|[Inflate(float)](VRageMath.BoundingBox@Inflate)||
|[Inflate(Vector3)](VRageMath.BoundingBox@Inflate)||
|[InflateToMinimum(Vector3)](VRageMath.BoundingBox@InflateToMinimum)||
|[Intersect(BoundingBox)](VRageMath.BoundingBox@Intersect)|Returns bounding box which is intersection of this and box Result is invalid box when there's no intersection (Min > Max)|
|[Intersects(BoundingBox)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects another BoundingBox.|
|[Intersects(ref BoundingBox)](VRageMath.BoundingBox@Intersects)||
|[Intersects(ref BoundingBox, out bool)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects another BoundingBox.|
|[Intersects(BoundingFrustum)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a BoundingFrustum.|
|[Intersects(Plane)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a Plane.|
|[Intersects(ref Plane, out PlaneIntersectionType)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a Plane.|
|[Intersects(Line, out float)](VRageMath.BoundingBox@Intersects)||
|[Intersects(Ray)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a Ray.|
|[Intersects(ref Ray, out float?)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a Ray.|
|[Intersects(BoundingSphere)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a BoundingSphere.|
|[Intersects(ref BoundingSphere, out bool)](VRageMath.BoundingBox@Intersects)|Checks whether the current BoundingBox intersects a BoundingSphere.|
|[Intersects(ref BoundingSphere)](VRageMath.BoundingBox@Intersects)||
|[Intersects(ref BoundingSphereD)](VRageMath.BoundingBox@Intersects)||
|[IntersectsTriangle(Vector3, Vector3, Vector3)](VRageMath.BoundingBox@IntersectsTriangle)||
|[IntersectsTriangle(ref Vector3, ref Vector3, ref Vector3)](VRageMath.BoundingBox@IntersectsTriangle)||
|[ProjectedArea(Vector3)](VRageMath.BoundingBox@ProjectedArea)||
|[Round(int)](VRageMath.BoundingBox@Round)||
|[Round()](VRageMath.BoundingBox@Round)||
|[Scale(Vector3)](VRageMath.BoundingBox@Scale)||
|[SurfaceArea()](VRageMath.BoundingBox@SurfaceArea)||
|[ToString()](VRageMath.BoundingBox@ToString)|Returns a String that represents the current BoundingBox.|
|[Transform(Matrix)](VRageMath.BoundingBox@Transform)||
|[Transform(MatrixD)](VRageMath.BoundingBox@Transform)||
|[Transform(ref Matrix)](VRageMath.BoundingBox@Transform)||
|[Transform(ref Matrix, ref BoundingBox)](VRageMath.BoundingBox@Transform)||
|[Transform(ref MatrixD)](VRageMath.BoundingBox@Transform)||
|[Transform(ref MatrixD, ref BoundingBoxD)](VRageMath.BoundingBox@Transform)||
|[Translate(Matrix)](VRageMath.BoundingBox@Translate)|Translate|
|[Translate(Vector3)](VRageMath.BoundingBox@Translate)|Translate|
|[Volume()](VRageMath.BoundingBox@Volume)||

**Implements:**  
* [IEquatable<BoundingBox>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

