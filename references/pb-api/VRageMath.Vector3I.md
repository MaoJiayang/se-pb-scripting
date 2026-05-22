**Assembly:** VRage.Math.dll

```csharp
public struct Vector3I: IEquatable<Vector3I>, IComparable<Vector3I>
```

## Fields

|Member|Description|
|---|---|
|[static Backward](VRageMath.Vector3I@Backward)||
|[static Comparer](VRageMath.Vector3I@Comparer)||
|[static Down](VRageMath.Vector3I@Down)||
|[static Forward](VRageMath.Vector3I@Forward)||
|[static Left](VRageMath.Vector3I@Left)||
|[static MaxValue](VRageMath.Vector3I@MaxValue)||
|[static MinValue](VRageMath.Vector3I@MinValue)||
|[static One](VRageMath.Vector3I@One)||
|[static Right](VRageMath.Vector3I@Right)||
|[static UnitX](VRageMath.Vector3I@UnitX)||
|[static UnitY](VRageMath.Vector3I@UnitY)||
|[static UnitZ](VRageMath.Vector3I@UnitZ)||
|[static Up](VRageMath.Vector3I@Up)||
|[static Zero](VRageMath.Vector3I@Zero)||
|[X](VRageMath.Vector3I@X)||
|[Y](VRageMath.Vector3I@Y)||
|[Z](VRageMath.Vector3I@Z)||

## Properties

|Member|Description|
|---|---|
|[IsPowerOfTwo](VRageMath.Vector3I@IsPowerOfTwo)||
|[Item](VRageMath.Vector3I@Item)||
|[Size](VRageMath.Vector3I@Size)|How many cubes are in block with this size|
|[SizeLong](VRageMath.Vector3I@SizeLong)||

## Constructors

|Member|Description|
|---|---|
|[Vector3I(int)](VRageMath.Vector3I@.ctor)||
|[Vector3I(int, int, int)](VRageMath.Vector3I@.ctor)||
|[Vector3I(Vector2I, int)](VRageMath.Vector3I@.ctor)||
|[Vector3I(Vector3)](VRageMath.Vector3I@.ctor)||
|[Vector3I(Vector3D)](VRageMath.Vector3I@.ctor)||
|[Vector3I(Vector3S)](VRageMath.Vector3I@.ctor)||
|[Vector3I(float, float, float)](VRageMath.Vector3I@.ctor)||
|[Vector3I(Byte[], int)](VRageMath.Vector3I@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Abs(Vector3I)](VRageMath.Vector3I@Abs)||
|[static Abs(ref Vector3I, out Vector3I)](VRageMath.Vector3I@Abs)||
|[static BoxContains(Vector3I, Vector3I, Vector3I)](VRageMath.Vector3I@BoxContains)||
|[static BoxContains(ref Vector3I, ref Vector3I, ref Vector3I)](VRageMath.Vector3I@BoxContains)||
|[static BoxIntersects(Vector3I, Vector3I, Vector3I, Vector3I)](VRageMath.Vector3I@BoxIntersects)||
|[static BoxIntersects(ref Vector3I, ref Vector3I, ref Vector3I, ref Vector3I)](VRageMath.Vector3I@BoxIntersects)||
|[static Ceiling(Vector3)](VRageMath.Vector3I@Ceiling)||
|[static Ceiling(Vector3D)](VRageMath.Vector3I@Ceiling)||
|[static Clamp(Vector3I, Vector3I, Vector3I)](VRageMath.Vector3I@Clamp)||
|[static Clamp(ref Vector3I, ref Vector3I, ref Vector3I, out Vector3I)](VRageMath.Vector3I@Clamp)||
|[static Cross(ref Vector3I, ref Vector3I, out Vector3I)](VRageMath.Vector3I@Cross)|Calculates the cross product of two vectors.|
|[static DistanceManhattan(Vector3I, Vector3I)](VRageMath.Vector3I@DistanceManhattan)|Manhattan distance (cube distance) X + Y + Z of Abs(first - second)|
|[static DominantAxisProjection(Vector3I)](VRageMath.Vector3I@DominantAxisProjection)|Returns a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value.|
|[static DominantAxisProjection(ref Vector3I, out Vector3I)](VRageMath.Vector3I@DominantAxisProjection)|Calculates a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value. The result is saved into a user-specified variable.|
|[static Dot(Vector3I, Vector3I)](VRageMath.Vector3I@Dot)||
|[static Dot(ref Vector3I, ref Vector3I)](VRageMath.Vector3I@Dot)||
|[static Dot(ref Vector3I, ref Vector3I, out int)](VRageMath.Vector3I@Dot)||
|[static EnumerateRange(Vector3I, Vector3I)](VRageMath.Vector3I@EnumerateRange)|Enumerate all values in a integer interval (a cuboid). This method is an allocating version of the Vector3I_RangeIterator. This once can be used in the foreach syntax though so it's more convenient for debug routines.|
|[static Floor(Vector3)](VRageMath.Vector3I@Floor)||
|[static Floor(Vector3D)](VRageMath.Vector3I@Floor)||
|[static Floor(ref Vector3, out Vector3I)](VRageMath.Vector3I@Floor)||
|[static Floor(ref Vector3D, out Vector3I)](VRageMath.Vector3I@Floor)||
|[static GetDominantDirection(Vector3I)](VRageMath.Vector3I@GetDominantDirection)||
|[static GetDominantDirectionVector(Vector3I)](VRageMath.Vector3I@GetDominantDirectionVector)||
|[static Max(Vector3I, Vector3I)](VRageMath.Vector3I@Max)||
|[static Max(ref Vector3I, ref Vector3I, out Vector3I)](VRageMath.Vector3I@Max)||
|[static Min(Vector3I, Vector3I)](VRageMath.Vector3I@Min)||
|[static Min(ref Vector3I, ref Vector3I, out Vector3I)](VRageMath.Vector3I@Min)||
|[static MinMax(ref Vector3I, ref Vector3I)](VRageMath.Vector3I@MinMax)|Separates minimal and maximal values of any two input vectors|
|[static Round(Vector3)](VRageMath.Vector3I@Round)||
|[static Round(Vector3D)](VRageMath.Vector3I@Round)||
|[static Round(ref Vector3, out Vector3I)](VRageMath.Vector3I@Round)||
|[static Round(ref Vector3D, out Vector3I)](VRageMath.Vector3I@Round)||
|[static Shift(Vector3I)](VRageMath.Vector3I@Shift)||
|[static Sign(Vector3)](VRageMath.Vector3I@Sign)||
|[static Sign(Vector3I)](VRageMath.Vector3I@Sign)||
|[static Transform(ref Vector3I, ref Matrix, out Vector3I)](VRageMath.Vector3I@Transform)|Transforms a Vector3I by the given Matrix.|
|[static Transform(ref Vector3I, ref Quaternion, out Vector3I)](VRageMath.Vector3I@Transform)||
|[static Transform(Vector3I, Quaternion)](VRageMath.Vector3I@Transform)||
|[static Transform(ref Vector3I, ref MatrixI, out Vector3I)](VRageMath.Vector3I@Transform)||
|[static Transform(Vector3I, MatrixI)](VRageMath.Vector3I@Transform)||
|[static Transform(Vector3I, ref MatrixI)](VRageMath.Vector3I@Transform)||
|[static TransformNormal(Vector3I, ref MatrixI)](VRageMath.Vector3I@TransformNormal)||
|[static TransformNormal(ref Vector3I, ref Matrix, out Vector3I)](VRageMath.Vector3I@TransformNormal)|Transforms a vector normal by a matrix.|
|[static TransformNormal(ref Vector3I, ref MatrixI, out Vector3I)](VRageMath.Vector3I@TransformNormal)||
|[static Trunc(Vector3)](VRageMath.Vector3I@Trunc)||
|[static TryParseFromString(string, out Vector3I)](VRageMath.Vector3I@TryParseFromString)||
|[AbsMax()](VRageMath.Vector3I@AbsMax)|Returns the component of the vector, whose absolute value is largest of all the three components.|
|[AbsMin()](VRageMath.Vector3I@AbsMin)|Returns the component of the vector, whose absolute value is smallest of all the three components.|
|[AxisValue(Axis)](VRageMath.Vector3I@AxisValue)||
|[CompareTo(Vector3I)](VRageMath.Vector3I@CompareTo)||
|[Dot(ref Vector3I)](VRageMath.Vector3I@Dot)||
|[Equals(Vector3I)](VRageMath.Vector3I@Equals)||
|[Equals(object)](VRageMath.Vector3I@Equals)||
|[GetHashCode()](VRageMath.Vector3I@GetHashCode)||
|[IsAxisAligned()](VRageMath.Vector3I@IsAxisAligned)||
|[IsInside(ref Vector3I, ref Vector3I)](VRageMath.Vector3I@IsInside)||
|[IsInside(Vector3I, Vector3I)](VRageMath.Vector3I@IsInside)||
|[IsInsideInclusiveEnd(ref Vector3I, ref Vector3I)](VRageMath.Vector3I@IsInsideInclusiveEnd)||
|[IsInsideInclusiveEnd(Vector3I, Vector3I)](VRageMath.Vector3I@IsInsideInclusiveEnd)||
|[Length()](VRageMath.Vector3I@Length)||
|[RectangularDistance(Vector3I)](VRageMath.Vector3I@RectangularDistance)|Calculates rectangular distance. It's how many sectors you have to travel to get to other sector from current sector.|
|[RectangularLength()](VRageMath.Vector3I@RectangularLength)|Calculates rectangular distance of this vector, interpreted as a point, from the origin.|
|[ToBytes(List<byte>)](VRageMath.Vector3I@ToBytes)||
|[ToString()](VRageMath.Vector3I@ToString)||
|[Volume()](VRageMath.Vector3I@Volume)||

**Implements:**  
* [IComparable<Vector3I>](https://docs.microsoft.com/en-us/dotnet/api/System.IComparable-1?view=netframework-4.6)  
* [IEquatable<Vector3I>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

