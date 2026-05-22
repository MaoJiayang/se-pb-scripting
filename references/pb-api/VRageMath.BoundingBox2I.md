**Assembly:** VRage.Math.dll

```csharp
public struct BoundingBox2I: IEquatable<BoundingBox2I>
```

Defines an axis-aligned box-shaped 3D volume.

## Fields

|Member|Description|
|---|---|
|[Max](VRageMath.BoundingBox2I@Max)|The maximum point the BoundingBox2I contains.|
|[Min](VRageMath.BoundingBox2I@Min)|The minimum point the BoundingBox2I contains.|

## Properties

|Member|Description|
|---|---|
|[Center](VRageMath.BoundingBox2I@Center)|Calculates center|
|[Extents](VRageMath.BoundingBox2I@Extents)||
|[HalfExtents](VRageMath.BoundingBox2I@HalfExtents)||
|[Height](VRageMath.BoundingBox2I@Height)||
|[Size](VRageMath.BoundingBox2I@Size)|Size|
|[Width](VRageMath.BoundingBox2I@Width)||

## Constructors

|Member|Description|
|---|---|
|[BoundingBox2I(Vector2I, Vector2I)](VRageMath.BoundingBox2I@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateFromHalfExtent(Vector2I, int)](VRageMath.BoundingBox2I@CreateFromHalfExtent)||
|[static CreateFromHalfExtent(Vector2I, Vector2I)](VRageMath.BoundingBox2I@CreateFromHalfExtent)||
|[static CreateFromPoints(IEnumerable<Vector2I>)](VRageMath.BoundingBox2I@CreateFromPoints)|Creates the smallest BoundingBox2I that will contain a group of points.|
|[static CreateInvalid()](VRageMath.BoundingBox2I@CreateInvalid)||
|[static CreateMerged(BoundingBox2I, BoundingBox2I)](VRageMath.BoundingBox2I@CreateMerged)|Creates the smallest BoundingBox2I that contains the two specified BoundingBox2I instances.|
|[static CreateMerged(ref BoundingBox2I, ref BoundingBox2I, out BoundingBox2I)](VRageMath.BoundingBox2I@CreateMerged)|Creates the smallest BoundingBox2I that contains the two specified BoundingBox2I instances.|
|[Area()](VRageMath.BoundingBox2I@Area)||
|[Contains(BoundingBox2I)](VRageMath.BoundingBox2I@Contains)|Tests whether the BoundingBox2I contains another BoundingBox2I.|
|[Contains(ref BoundingBox2I, out ContainmentType)](VRageMath.BoundingBox2I@Contains)|Tests whether the BoundingBox2I contains a BoundingBox2I.|
|[Contains(Vector2I)](VRageMath.BoundingBox2I@Contains)|Tests whether the BoundingBox2I contains a point.|
|[Contains(ref Vector2I, out ContainmentType)](VRageMath.BoundingBox2I@Contains)|Tests whether the BoundingBox2I contains a point.|
|[Equals(BoundingBox2I)](VRageMath.BoundingBox2I@Equals)|Determines whether two instances of BoundingBox2I are equal.|
|[Equals(object)](VRageMath.BoundingBox2I@Equals)|Determines whether two instances of BoundingBox2I are equal.|
|[GetCorners()](VRageMath.BoundingBox2I@GetCorners)|Gets an array of points that make up the corners of the BoundingBox2I.|
|[GetCorners(Vector2I[])](VRageMath.BoundingBox2I@GetCorners)|Gets the array of points that make up the corners of the BoundingBox2I.|
|[GetCornersUnsafe(*Vector2I)](VRageMath.BoundingBox2I@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingBox2I@GetHashCode)|Gets the hash code for this instance.|
|[GetIncluded(Vector2I)](VRageMath.BoundingBox2I@GetIncluded)||
|[Include(ref Vector2I)](VRageMath.BoundingBox2I@Include)|return expanded aabb (abb include point)|
|[Include(Vector2I)](VRageMath.BoundingBox2I@Include)||
|[Include(Vector2I, Vector2I, Vector2I)](VRageMath.BoundingBox2I@Include)||
|[Include(ref Vector2I, ref Vector2I, ref Vector2I)](VRageMath.BoundingBox2I@Include)||
|[Include(ref BoundingBox2I)](VRageMath.BoundingBox2I@Include)|return expanded aabb (abb include point)|
|[Include(BoundingBox2I)](VRageMath.BoundingBox2I@Include)||
|[Inflate(int)](VRageMath.BoundingBox2I@Inflate)||
|[InflateToMinimum(Vector2I)](VRageMath.BoundingBox2I@InflateToMinimum)||
|[Intersect(BoundingBox2I)](VRageMath.BoundingBox2I@Intersect)|Returns bounding box which is intersection of this and box It's called 'Prunik' Result is invalid box when there's no intersection (Min > Max)|
|[Intersects(BoundingBox2I)](VRageMath.BoundingBox2I@Intersects)|Checks whether the current BoundingBox2I intersects another BoundingBox2I.|
|[Intersects(ref BoundingBox2I)](VRageMath.BoundingBox2I@Intersects)||
|[Intersects(ref BoundingBox2I, out bool)](VRageMath.BoundingBox2I@Intersects)|Checks whether the current BoundingBox2I intersects another BoundingBox2I.|
|[Perimeter()](VRageMath.BoundingBox2I@Perimeter)||
|[Scale(Vector2I)](VRageMath.BoundingBox2I@Scale)||
|[ToString()](VRageMath.BoundingBox2I@ToString)|Returns a String that represents the current BoundingBox2I.|
|[Translate(Vector2I)](VRageMath.BoundingBox2I@Translate)|Translate|

**Implements:**  
* [IEquatable<BoundingBox2I>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

