**Assembly:** VRage.Math.dll

```csharp
public struct BoundingBox2: IEquatable<BoundingBox2>
```

Defines an axis-aligned box-shaped 3D volume.

## Fields

|Member|Description|
|---|---|
|[Max](VRageMath.BoundingBox2@Max)|The maximum point the BoundingBox2 contains.|
|[Min](VRageMath.BoundingBox2@Min)|The minimum point the BoundingBox2 contains.|

## Properties

|Member|Description|
|---|---|
|[Center](VRageMath.BoundingBox2@Center)|Calculates center|
|[Extents](VRageMath.BoundingBox2@Extents)||
|[HalfExtents](VRageMath.BoundingBox2@HalfExtents)||
|[Height](VRageMath.BoundingBox2@Height)||
|[Size](VRageMath.BoundingBox2@Size)|Size|
|[Width](VRageMath.BoundingBox2@Width)||

## Constructors

|Member|Description|
|---|---|
|[BoundingBox2(Vector2, Vector2)](VRageMath.BoundingBox2@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateFromHalfExtent(Vector2, float)](VRageMath.BoundingBox2@CreateFromHalfExtent)||
|[static CreateFromHalfExtent(Vector2, Vector2)](VRageMath.BoundingBox2@CreateFromHalfExtent)||
|[static CreateFromPoints(IEnumerable<Vector2>)](VRageMath.BoundingBox2@CreateFromPoints)|Creates the smallest BoundingBox2 that will contain a group of points.|
|[static CreateInvalid()](VRageMath.BoundingBox2@CreateInvalid)||
|[static CreateMerged(BoundingBox2, BoundingBox2)](VRageMath.BoundingBox2@CreateMerged)|Creates the smallest BoundingBox2 that contains the two specified BoundingBox2 instances.|
|[static CreateMerged(ref BoundingBox2, ref BoundingBox2, out BoundingBox2)](VRageMath.BoundingBox2@CreateMerged)|Creates the smallest BoundingBox2 that contains the two specified BoundingBox2 instances.|
|[Area()](VRageMath.BoundingBox2@Area)||
|[Contains(BoundingBox2)](VRageMath.BoundingBox2@Contains)|Tests whether the BoundingBox2 contains another BoundingBox2.|
|[Contains(ref BoundingBox2, out ContainmentType)](VRageMath.BoundingBox2@Contains)|Tests whether the BoundingBox2 contains a BoundingBox2.|
|[Contains(Vector2)](VRageMath.BoundingBox2@Contains)|Tests whether the BoundingBox2 contains a point.|
|[Contains(ref Vector2, out ContainmentType)](VRageMath.BoundingBox2@Contains)|Tests whether the BoundingBox2 contains a point.|
|[Distance(Vector2)](VRageMath.BoundingBox2@Distance)||
|[Equals(BoundingBox2)](VRageMath.BoundingBox2@Equals)|Determines whether two instances of BoundingBox2 are equal.|
|[Equals(object)](VRageMath.BoundingBox2@Equals)|Determines whether two instances of BoundingBox2 are equal.|
|[GetCorners()](VRageMath.BoundingBox2@GetCorners)|Gets an array of points that make up the corners of the BoundingBox2.|
|[GetCorners(Vector2[])](VRageMath.BoundingBox2@GetCorners)|Gets the array of points that make up the corners of the BoundingBox2.|
|[GetCornersUnsafe(*Vector2)](VRageMath.BoundingBox2@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingBox2@GetHashCode)|Gets the hash code for this instance.|
|[GetIncluded(Vector2)](VRageMath.BoundingBox2@GetIncluded)||
|[Include(ref Vector2)](VRageMath.BoundingBox2@Include)|return expanded aabb (abb include point)|
|[Include(Vector2)](VRageMath.BoundingBox2@Include)||
|[Include(Vector2, Vector2, Vector2)](VRageMath.BoundingBox2@Include)||
|[Include(ref Vector2, ref Vector2, ref Vector2)](VRageMath.BoundingBox2@Include)||
|[Include(ref BoundingBox2)](VRageMath.BoundingBox2@Include)|return expanded aabb (abb include point)|
|[Include(BoundingBox2)](VRageMath.BoundingBox2@Include)||
|[Inflate(float)](VRageMath.BoundingBox2@Inflate)||
|[InflateToMinimum(Vector2)](VRageMath.BoundingBox2@InflateToMinimum)||
|[Intersect(BoundingBox2)](VRageMath.BoundingBox2@Intersect)|Returns bounding box which is intersection of this and box Result is invalid box when there's no intersection (Min > Max)|
|[Intersects(BoundingBox2)](VRageMath.BoundingBox2@Intersects)|Checks whether the current BoundingBox2 intersects another BoundingBox2.|
|[Intersects(ref BoundingBox2)](VRageMath.BoundingBox2@Intersects)||
|[Intersects(ref BoundingBox2, out bool)](VRageMath.BoundingBox2@Intersects)|Checks whether the current BoundingBox2 intersects another BoundingBox2.|
|[Perimeter()](VRageMath.BoundingBox2@Perimeter)||
|[Scale(Vector2)](VRageMath.BoundingBox2@Scale)||
|[ToString()](VRageMath.BoundingBox2@ToString)|Returns a String that represents the current BoundingBox2.|
|[Translate(Vector2)](VRageMath.BoundingBox2@Translate)|Translate|

**Implements:**  
* [IEquatable<BoundingBox2>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

