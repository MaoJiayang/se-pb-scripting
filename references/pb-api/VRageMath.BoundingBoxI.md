**Assembly:** VRage.Math.dll

```csharp
public struct BoundingBoxI: IEquatable<BoundingBoxI>
```

Defines an axis-aligned box-shaped 3D volume.

## Fields

|Member|Description|
|---|---|
|[Max](VRageMath.BoundingBoxI@Max)|The maximum point the BoundingBoxI contains.|
|[Min](VRageMath.BoundingBoxI@Min)|The minimum point the BoundingBoxI contains.|

## Properties

|Member|Description|
|---|---|
|[Center](VRageMath.BoundingBoxI@Center)|Calculates center|
|[HalfExtents](VRageMath.BoundingBoxI@HalfExtents)||
|[IsValid](VRageMath.BoundingBoxI@IsValid)||
|[Perimeter](VRageMath.BoundingBoxI@Perimeter)|return perimeter of edges|
|[Size](VRageMath.BoundingBoxI@Size)|Size|

## Constructors

|Member|Description|
|---|---|
|[BoundingBoxI(BoundingBox)](VRageMath.BoundingBoxI@.ctor)||
|[BoundingBoxI(Vector3I, Vector3I)](VRageMath.BoundingBoxI@.ctor)||
|[BoundingBoxI(int, int)](VRageMath.BoundingBoxI@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateFromPoints(IEnumerable<Vector3I>)](VRageMath.BoundingBoxI@CreateFromPoints)|Creates the smallest BoundingBoxI that will contain a group of points.|
|[static CreateFromSphere(BoundingSphere)](VRageMath.BoundingBoxI@CreateFromSphere)|Creates the smallest BoundingBoxI that will contain the specified BoundingSphere.|
|[static CreateFromSphere(ref BoundingSphere, out BoundingBoxI)](VRageMath.BoundingBoxI@CreateFromSphere)|Creates the smallest BoundingBoxI that will contain the specified BoundingSphere.|
|[static CreateInvalid()](VRageMath.BoundingBoxI@CreateInvalid)||
|[static CreateMerged(BoundingBoxI, BoundingBoxI)](VRageMath.BoundingBoxI@CreateMerged)|Creates the smallest BoundingBoxI that contains the two specified BoundingBoxI instances.|
|[static CreateMerged(ref BoundingBoxI, ref BoundingBoxI, out BoundingBoxI)](VRageMath.BoundingBoxI@CreateMerged)|Creates the smallest BoundingBoxI that contains the two specified BoundingBoxI instances.|
|[static EnumeratePoints(BoundingBoxI)](VRageMath.BoundingBoxI@EnumeratePoints)|Enumerate all values in a integer interval (a cuboid). This method is an allocating version of the Vector3I_RangeIterator. This once can be used in the foreach syntax though so it's more convenient for debug routines.|
|[static IterateDifference(BoundingBoxI, BoundingBoxI)](VRageMath.BoundingBoxI@IterateDifference)|Iterate every cell contained in {left} - {right}, where we interpret {box} as the set of all distinct Vector3I points inside a 'box'. Containment is taken in a typical inclusive start, exclusive end fashion.|
|[Contains(BoundingBoxI)](VRageMath.BoundingBoxI@Contains)|Tests whether the BoundingBoxI contains another BoundingBoxI.|
|[Contains(ref BoundingBoxI, out ContainmentType)](VRageMath.BoundingBoxI@Contains)|Tests whether the BoundingBoxI contains a BoundingBoxI.|
|[Contains(Vector3I)](VRageMath.BoundingBoxI@Contains)|Tests whether the BoundingBoxI contains a point.|
|[Contains(Vector3)](VRageMath.BoundingBoxI@Contains)||
|[Contains(ref Vector3I, out ContainmentType)](VRageMath.BoundingBoxI@Contains)|Tests whether the BoundingBoxI contains a point.|
|[Distance(Vector3I)](VRageMath.BoundingBoxI@Distance)||
|[Equals(BoundingBoxI)](VRageMath.BoundingBoxI@Equals)|Determines whether two instances of BoundingBoxI are equal.|
|[Equals(object)](VRageMath.BoundingBoxI@Equals)|Determines whether two instances of BoundingBoxI are equal.|
|[GetCorners()](VRageMath.BoundingBoxI@GetCorners)|Gets an array of points that make up the corners of the BoundingBoxI.|
|[GetCorners(Vector3I[])](VRageMath.BoundingBoxI@GetCorners)|Gets the array of points that make up the corners of the BoundingBoxI.|
|[GetCornersUnsafe(*Vector3I)](VRageMath.BoundingBoxI@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingBoxI@GetHashCode)|Gets the hash code for this instance.|
|[GetIncluded(Vector3I)](VRageMath.BoundingBoxI@GetIncluded)||
|[Include(ref Vector3I)](VRageMath.BoundingBoxI@Include)|return expanded aabb (abb include point)|
|[Include(Vector3I)](VRageMath.BoundingBoxI@Include)||
|[Include(Vector3I, Vector3I, Vector3I)](VRageMath.BoundingBoxI@Include)||
|[Include(ref Vector3I, ref Vector3I, ref Vector3I)](VRageMath.BoundingBoxI@Include)||
|[Include(ref BoundingBoxI)](VRageMath.BoundingBoxI@Include)|return expanded aabb (abb include point)|
|[Include(BoundingBoxI)](VRageMath.BoundingBoxI@Include)||
|[Inflate(int)](VRageMath.BoundingBoxI@Inflate)||
|[InflateToMinimum(Vector3I)](VRageMath.BoundingBoxI@InflateToMinimum)||
|[Intersect(BoundingBoxI)](VRageMath.BoundingBoxI@Intersect)|Returns bounding box which is intersection of this and box Result is invalid box when there's no intersection (Min > Max)|
|[Intersects(BoundingBoxI)](VRageMath.BoundingBoxI@Intersects)|Checks whether the current BoundingBoxI intersects another BoundingBoxI.|
|[Intersects(ref BoundingBoxI)](VRageMath.BoundingBoxI@Intersects)||
|[Intersects(ref BoundingBoxI, out bool)](VRageMath.BoundingBoxI@Intersects)|Checks whether the current BoundingBoxI intersects another BoundingBoxI.|
|[Intersects(Plane)](VRageMath.BoundingBoxI@Intersects)|Checks whether the current BoundingBoxI intersects a Plane.|
|[Intersects(ref Plane, out PlaneIntersectionType)](VRageMath.BoundingBoxI@Intersects)|Checks whether the current BoundingBoxI intersects a Plane.|
|[Intersects(Line, out float)](VRageMath.BoundingBoxI@Intersects)||
|[Intersects(Ray)](VRageMath.BoundingBoxI@Intersects)|Checks whether the current BoundingBoxI intersects a Ray.|
|[Intersects(ref Ray, out float?)](VRageMath.BoundingBoxI@Intersects)|Checks whether the current BoundingBoxI intersects a Ray.|
|[IntersectsTriangle(Vector3I, Vector3I, Vector3I)](VRageMath.BoundingBoxI@IntersectsTriangle)||
|[IntersectsTriangle(ref Vector3I, ref Vector3I, ref Vector3I)](VRageMath.BoundingBoxI@IntersectsTriangle)||
|[IntersectWith(ref BoundingBoxI)](VRageMath.BoundingBoxI@IntersectWith)|Returns bounding box which is intersection of this and box Result is invalid box when there's no intersection (Min > Max)|
|[SurfaceArea()](VRageMath.BoundingBoxI@SurfaceArea)||
|[ToString()](VRageMath.BoundingBoxI@ToString)|Returns a String that represents the current BoundingBoxI.|
|[Translate(Vector3I)](VRageMath.BoundingBoxI@Translate)|Translate|
|[Volume()](VRageMath.BoundingBoxI@Volume)||

**Implements:**  
* [IEquatable<BoundingBoxI>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

