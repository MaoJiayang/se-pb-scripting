**Assembly:** VRage.Math.dll

```csharp
public struct BoundingBox2D: IEquatable<BoundingBox2D>
```

Defines an axis-aligned box-shaped 2D volume.

## Fields

|Member|Description|
|---|---|
|[static CornerCount](VRageMath.BoundingBox2D@CornerCount)|Specifies the total number of corners (8) in the BoundingBox2D.|
|[Max](VRageMath.BoundingBox2D@Max)|The maximum point the BoundingBox2D contains.|
|[Min](VRageMath.BoundingBox2D@Min)|The minimum point the BoundingBox2D contains.|

## Properties

|Member|Description|
|---|---|
|[Center](VRageMath.BoundingBox2D@Center)|Calculates center|
|[Extents](VRageMath.BoundingBox2D@Extents)||
|[HalfExtents](VRageMath.BoundingBox2D@HalfExtents)||
|[Height](VRageMath.BoundingBox2D@Height)||
|[Size](VRageMath.BoundingBox2D@Size)|Size|
|[Width](VRageMath.BoundingBox2D@Width)||

## Constructors

|Member|Description|
|---|---|
|[BoundingBox2D(Vector2D, Vector2D)](VRageMath.BoundingBox2D@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateFromHalfExtent(Vector2D, double)](VRageMath.BoundingBox2D@CreateFromHalfExtent)||
|[static CreateFromHalfExtent(Vector2D, Vector2D)](VRageMath.BoundingBox2D@CreateFromHalfExtent)||
|[static CreateFromPoints(IEnumerable<Vector2D>)](VRageMath.BoundingBox2D@CreateFromPoints)|Creates the smallest BoundingBox2D that will contain a group of points.|
|[static CreateInvalid()](VRageMath.BoundingBox2D@CreateInvalid)||
|[static CreateMerged(BoundingBox2D, BoundingBox2D)](VRageMath.BoundingBox2D@CreateMerged)|Creates the smallest BoundingBox2D that contains the two specified BoundingBox2D instances.|
|[static CreateMerged(ref BoundingBox2D, ref BoundingBox2D, out BoundingBox2D)](VRageMath.BoundingBox2D@CreateMerged)|Creates the smallest BoundingBox2D that contains the two specified BoundingBox2D instances.|
|[Area()](VRageMath.BoundingBox2D@Area)||
|[Contains(BoundingBox2D)](VRageMath.BoundingBox2D@Contains)|Tests whether the BoundingBox2D contains another BoundingBox2D.|
|[Contains(ref BoundingBox2D, out ContainmentType)](VRageMath.BoundingBox2D@Contains)|Tests whether the BoundingBox2D contains a BoundingBox2D.|
|[Contains(Vector2D)](VRageMath.BoundingBox2D@Contains)|Tests whether the BoundingBox2D contains a point.|
|[Contains(ref Vector2D, out ContainmentType)](VRageMath.BoundingBox2D@Contains)|Tests whether the BoundingBox2D contains a point.|
|[Distance(Vector2D)](VRageMath.BoundingBox2D@Distance)||
|[Equals(BoundingBox2D)](VRageMath.BoundingBox2D@Equals)|Determines whether two instances of BoundingBox2D are equal.|
|[Equals(object)](VRageMath.BoundingBox2D@Equals)|Determines whether two instances of BoundingBox2D are equal.|
|[GetCorners()](VRageMath.BoundingBox2D@GetCorners)|Gets an array of points that make up the corners of the BoundingBox2D.|
|[GetCorners(Vector2D[])](VRageMath.BoundingBox2D@GetCorners)|Gets the array of points that make up the corners of the BoundingBox2D.|
|[GetCornersUnsafe(*Vector2D)](VRageMath.BoundingBox2D@GetCornersUnsafe)||
|[GetHashCode()](VRageMath.BoundingBox2D@GetHashCode)|Gets the hash code for this instance.|
|[GetIncluded(Vector2D)](VRageMath.BoundingBox2D@GetIncluded)||
|[Include(ref Vector2D)](VRageMath.BoundingBox2D@Include)|return expanded aabb (abb include point)|
|[Include(Vector2D)](VRageMath.BoundingBox2D@Include)||
|[Include(Vector2D, Vector2D, Vector2D)](VRageMath.BoundingBox2D@Include)||
|[Include(ref Vector2D, ref Vector2D, ref Vector2D)](VRageMath.BoundingBox2D@Include)||
|[Include(ref BoundingBox2D)](VRageMath.BoundingBox2D@Include)|return expanded aabb (abb include point)|
|[Include(BoundingBox2D)](VRageMath.BoundingBox2D@Include)||
|[Inflate(double)](VRageMath.BoundingBox2D@Inflate)||
|[InflateToMinimum(Vector2D)](VRageMath.BoundingBox2D@InflateToMinimum)||
|[Intersect(BoundingBox2D)](VRageMath.BoundingBox2D@Intersect)|Returns bounding box which is intersection of this and box It's called 'Prunik' Result is invalid box when there's no intersection (Min > Max)|
|[Intersects(BoundingBox2D)](VRageMath.BoundingBox2D@Intersects)|Checks whether the current BoundingBox2D intersects another BoundingBox2D.|
|[Intersects(ref BoundingBox2D)](VRageMath.BoundingBox2D@Intersects)||
|[Intersects(ref BoundingBox2D, out bool)](VRageMath.BoundingBox2D@Intersects)|Checks whether the current BoundingBox2D intersects another BoundingBox2D.|
|[Perimeter()](VRageMath.BoundingBox2D@Perimeter)||
|[Scale(Vector2D)](VRageMath.BoundingBox2D@Scale)||
|[ToString()](VRageMath.BoundingBox2D@ToString)|Returns a String that represents the current BoundingBox2D.|
|[Translate(Vector2D)](VRageMath.BoundingBox2D@Translate)|Translate|

**Implements:**  
* [IEquatable<BoundingBox2D>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

