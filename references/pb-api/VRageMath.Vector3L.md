**Assembly:** VRage.Math.dll

```csharp
public struct Vector3L: IEquatable<Vector3L>, IComparable<Vector3L>
```

## Fields

|Member|Description|
|---|---|
|[static Backward](VRageMath.Vector3L@Backward)||
|[static Comparer](VRageMath.Vector3L@Comparer)||
|[static Down](VRageMath.Vector3L@Down)||
|[static Forward](VRageMath.Vector3L@Forward)||
|[static Left](VRageMath.Vector3L@Left)||
|[static MaxValue](VRageMath.Vector3L@MaxValue)||
|[static MinValue](VRageMath.Vector3L@MinValue)||
|[static One](VRageMath.Vector3L@One)||
|[static Right](VRageMath.Vector3L@Right)||
|[static UnitX](VRageMath.Vector3L@UnitX)||
|[static UnitY](VRageMath.Vector3L@UnitY)||
|[static UnitZ](VRageMath.Vector3L@UnitZ)||
|[static Up](VRageMath.Vector3L@Up)||
|[static Zero](VRageMath.Vector3L@Zero)||
|[X](VRageMath.Vector3L@X)||
|[Y](VRageMath.Vector3L@Y)||
|[Z](VRageMath.Vector3L@Z)||

## Properties

|Member|Description|
|---|---|
|[Item](VRageMath.Vector3L@Item)||
|[Size](VRageMath.Vector3L@Size)|How many cubes are in block with this size|
|[SizeLong](VRageMath.Vector3L@SizeLong)||

## Constructors

|Member|Description|
|---|---|
|[Vector3L(long)](VRageMath.Vector3L@.ctor)||
|[Vector3L(long, long, long)](VRageMath.Vector3L@.ctor)||
|[Vector3L(Vector3)](VRageMath.Vector3L@.ctor)||
|[Vector3L(Vector3D)](VRageMath.Vector3L@.ctor)||
|[Vector3L(Vector3S)](VRageMath.Vector3L@.ctor)||
|[Vector3L(float, float, float)](VRageMath.Vector3L@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Abs(Vector3L)](VRageMath.Vector3L@Abs)||
|[static Abs(ref Vector3L, out Vector3L)](VRageMath.Vector3L@Abs)||
|[static BoxContains(Vector3L, Vector3L, Vector3L)](VRageMath.Vector3L@BoxContains)||
|[static BoxContains(ref Vector3L, ref Vector3L, ref Vector3L)](VRageMath.Vector3L@BoxContains)||
|[static Boxlongersects(Vector3L, Vector3L, Vector3L, Vector3L)](VRageMath.Vector3L@Boxlongersects)||
|[static Boxlongersects(ref Vector3L, ref Vector3L, ref Vector3L, ref Vector3L)](VRageMath.Vector3L@Boxlongersects)||
|[static Ceiling(Vector3)](VRageMath.Vector3L@Ceiling)||
|[static Clamp(Vector3L, Vector3L, Vector3L)](VRageMath.Vector3L@Clamp)||
|[static Clamp(ref Vector3L, ref Vector3L, ref Vector3L, out Vector3L)](VRageMath.Vector3L@Clamp)||
|[static Cross(ref Vector3L, ref Vector3L, out Vector3L)](VRageMath.Vector3L@Cross)|Calculates the cross product of two vectors.|
|[static DistanceManhattan(Vector3L, Vector3L)](VRageMath.Vector3L@DistanceManhattan)|Manhattan distance (cube distance) X + Y + Z of Abs(first - second)|
|[static DominantAxisProjection(Vector3L)](VRageMath.Vector3L@DominantAxisProjection)|Returns a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value.|
|[static DominantAxisProjection(ref Vector3L, out Vector3L)](VRageMath.Vector3L@DominantAxisProjection)|Calculates a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value. The result is saved longo a user-specified variable.|
|[static Dot(Vector3L, Vector3L)](VRageMath.Vector3L@Dot)||
|[static Dot(ref Vector3L, ref Vector3L)](VRageMath.Vector3L@Dot)||
|[static Dot(ref Vector3L, ref Vector3L, out long)](VRageMath.Vector3L@Dot)||
|[static EnumerateRange(Vector3L, Vector3L)](VRageMath.Vector3L@EnumerateRange)|Enumerate all values in a longeger longerval (a cuboid). This method is an allocating version of the Vector3L_RangeIterator. This once can be used in the foreach syntax though so it's more convenient for debug routines.|
|[static Floor(Vector3)](VRageMath.Vector3L@Floor)||
|[static Floor(Vector3D)](VRageMath.Vector3L@Floor)||
|[static Floor(ref Vector3, out Vector3L)](VRageMath.Vector3L@Floor)||
|[static Floor(ref Vector3D, out Vector3L)](VRageMath.Vector3L@Floor)||
|[static GetDominantDirection(Vector3L)](VRageMath.Vector3L@GetDominantDirection)||
|[static GetDominantDirectionVector(Vector3L)](VRageMath.Vector3L@GetDominantDirectionVector)||
|[static Max(Vector3L, Vector3L)](VRageMath.Vector3L@Max)||
|[static Max(ref Vector3L, ref Vector3L, out Vector3L)](VRageMath.Vector3L@Max)||
|[static Min(Vector3L, Vector3L)](VRageMath.Vector3L@Min)||
|[static Min(ref Vector3L, ref Vector3L, out Vector3L)](VRageMath.Vector3L@Min)||
|[static Round(Vector3)](VRageMath.Vector3L@Round)||
|[static Round(Vector3D)](VRageMath.Vector3L@Round)||
|[static Round(ref Vector3, out Vector3L)](VRageMath.Vector3L@Round)||
|[static Round(ref Vector3D, out Vector3L)](VRageMath.Vector3L@Round)||
|[static Shift(Vector3L)](VRageMath.Vector3L@Shift)||
|[static Sign(Vector3)](VRageMath.Vector3L@Sign)||
|[static Sign(Vector3L)](VRageMath.Vector3L@Sign)||
|[static Transform(ref Vector3L, ref Matrix, out Vector3L)](VRageMath.Vector3L@Transform)|Transforms a Vector3L by the given Matrix.|
|[static Transform(ref Vector3L, ref Quaternion, out Vector3L)](VRageMath.Vector3L@Transform)||
|[static Transform(Vector3L, Quaternion)](VRageMath.Vector3L@Transform)||
|[static TransformNormal(ref Vector3L, ref Matrix, out Vector3L)](VRageMath.Vector3L@TransformNormal)|Transforms a vector normal by a matrix.|
|[static Trunc(Vector3)](VRageMath.Vector3L@Trunc)||
|[static TryParseFromString(string, out Vector3L)](VRageMath.Vector3L@TryParseFromString)||
|[AbsMax()](VRageMath.Vector3L@AbsMax)|Returns the component of the vector, whose absolute value is largest of all the three components.|
|[AbsMin()](VRageMath.Vector3L@AbsMin)|Returns the component of the vector, whose absolute value is smallest of all the three components.|
|[AxisValue(Axis)](VRageMath.Vector3L@AxisValue)||
|[CompareTo(Vector3L)](VRageMath.Vector3L@CompareTo)||
|[Dot(ref Vector3L)](VRageMath.Vector3L@Dot)||
|[Equals(Vector3L)](VRageMath.Vector3L@Equals)||
|[Equals(object)](VRageMath.Vector3L@Equals)||
|[GetHashCode()](VRageMath.Vector3L@GetHashCode)||
|[IsInside(ref Vector3L, ref Vector3L)](VRageMath.Vector3L@IsInside)||
|[IsInside(Vector3L, Vector3L)](VRageMath.Vector3L@IsInside)||
|[IsInsideInclusiveEnd(ref Vector3L, ref Vector3L)](VRageMath.Vector3L@IsInsideInclusiveEnd)||
|[IsInsideInclusiveEnd(Vector3L, Vector3L)](VRageMath.Vector3L@IsInsideInclusiveEnd)||
|[Length()](VRageMath.Vector3L@Length)||
|[RectangularDistance(Vector3L)](VRageMath.Vector3L@RectangularDistance)|Calculates rectangular distance. It's how many sectors you have to travel to get to other sector from current sector.|
|[RectangularLength()](VRageMath.Vector3L@RectangularLength)|Calculates rectangular distance of this vector, longerpreted as a polong, from the origin.|
|[ToBytes(List<byte>)](VRageMath.Vector3L@ToBytes)||
|[ToString()](VRageMath.Vector3L@ToString)||
|[Volume()](VRageMath.Vector3L@Volume)||

**Implements:**  
* [IComparable<Vector3L>](https://docs.microsoft.com/en-us/dotnet/api/System.IComparable-1?view=netframework-4.6)  
* [IEquatable<Vector3L>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

