**Assembly:** VRage.Math.dll

```csharp
public struct Vector3D: IEquatable<Vector3D>
```

Defines a vector with three components. Vector3 with double floating point precision

## Fields

|Member|Description|
|---|---|
|[static Backward](VRageMath.Vector3D@Backward)||
|[static Down](VRageMath.Vector3D@Down)||
|[static Forward](VRageMath.Vector3D@Forward)||
|[static Half](VRageMath.Vector3D@Half)||
|[static Left](VRageMath.Vector3D@Left)||
|[static MaxValue](VRageMath.Vector3D@MaxValue)||
|[static MinValue](VRageMath.Vector3D@MinValue)||
|[static NegativeInfinity](VRageMath.Vector3D@NegativeInfinity)||
|[static One](VRageMath.Vector3D@One)||
|[static PositiveInfinity](VRageMath.Vector3D@PositiveInfinity)||
|[static Right](VRageMath.Vector3D@Right)||
|[static UnitX](VRageMath.Vector3D@UnitX)||
|[static UnitY](VRageMath.Vector3D@UnitY)||
|[static UnitZ](VRageMath.Vector3D@UnitZ)||
|[static Up](VRageMath.Vector3D@Up)||
|[static Zero](VRageMath.Vector3D@Zero)||
|[X](VRageMath.Vector3D@X)|Gets or sets the x-component of the vector.|
|[Y](VRageMath.Vector3D@Y)|Gets or sets the y-component of the vector.|
|[Z](VRageMath.Vector3D@Z)|Gets or sets the z-component of the vector.|

## Properties

|Member|Description|
|---|---|
|[Sum](VRageMath.Vector3D@Sum)||
|[Volume](VRageMath.Vector3D@Volume)||

## Constructors

|Member|Description|
|---|---|
|[Vector3D(double, double, double)](VRageMath.Vector3D@.ctor)||
|[Vector3D(double)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector2, double)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector2D, double)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector4)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector4D)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector3)](VRageMath.Vector3D@.ctor)||
|[Vector3D(ref Vector3I)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector3I)](VRageMath.Vector3D@.ctor)||
|[Vector3D(Vector3D)](VRageMath.Vector3D@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Abs(ref Vector3D, out Vector3D)](VRageMath.Vector3D@Abs)||
|[static Abs(Vector3D)](VRageMath.Vector3D@Abs)||
|[static Add(Vector3D, Vector3D)](VRageMath.Vector3D@Add)|Adds two vectors.|
|[static Add(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Add)|Adds two vectors.|
|[static Angle(Vector3D, Vector3D)](VRageMath.Vector3D@Angle)|Gets angle between 2 vectors in radians|
|[static ArePerpendicular(ref Vector3D, ref Vector3D)](VRageMath.Vector3D@ArePerpendicular)||
|[static Barycentric(Vector3D, Vector3D, Vector3D, double, double)](VRageMath.Vector3D@Barycentric)|Returns a Vector3 containing the 3D Cartesian coordinates of a point specified in Barycentric coordinates relative to a 3D triangle.|
|[static Barycentric(ref Vector3D, ref Vector3D, ref Vector3D, double, double, out Vector3D)](VRageMath.Vector3D@Barycentric)|Returns a Vector3 containing the 3D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 3D triangle.|
|[static Barycentric(Vector3D, Vector3D, Vector3D, Vector3D, out double, out double, out double)](VRageMath.Vector3D@Barycentric)|Compute barycentric coordinates (u, v, w) for point p with respect to triangle (a, b, c) From : Real-Time Collision Detection, Christer Ericson, CRC Press 3.4 Barycentric Coordinates|
|[static CalculatePerpendicularVector(Vector3D)](VRageMath.Vector3D@CalculatePerpendicularVector)||
|[static CatmullRom(Vector3D, Vector3D, Vector3D, Vector3D, double)](VRageMath.Vector3D@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CatmullRom(ref Vector3D, ref Vector3D, ref Vector3D, ref Vector3D, double, out Vector3D)](VRageMath.Vector3D@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static Clamp(Vector3D, Vector3D, Vector3D)](VRageMath.Vector3D@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(ref Vector3D, ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Clamp)|Restricts a value to be within a specified range.|
|[static ClampToSphere(Vector3D, double, bool)](VRageMath.Vector3D@ClampToSphere)||
|[static ClampToSphere(ref Vector3D, double)](VRageMath.Vector3D@ClampToSphere)||
|[static CreateFromAzimuthAndElevation(double, double, out Vector3D)](VRageMath.Vector3D@CreateFromAzimuthAndElevation)||
|[static Cross(Vector3D, Vector3D)](VRageMath.Vector3D@Cross)|Calculates the cross product of two vectors.|
|[static Cross(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Cross)|Calculates the cross product of two vectors.|
|[static Distance(Vector3D, Vector3D)](VRageMath.Vector3D@Distance)|Calculates the distance between two vectors.|
|[static Distance(Vector3D, Vector3)](VRageMath.Vector3D@Distance)||
|[static Distance(Vector3, Vector3D)](VRageMath.Vector3D@Distance)||
|[static Distance(ref Vector3D, ref Vector3D, out double)](VRageMath.Vector3D@Distance)|Calculates the distance between two vectors.|
|[static DistanceSquared(Vector3D, Vector3D)](VRageMath.Vector3D@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static DistanceSquared(ref Vector3D, ref Vector3D, out double)](VRageMath.Vector3D@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static Divide(Vector3D, Vector3D)](VRageMath.Vector3D@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(Vector3D, double)](VRageMath.Vector3D@Divide)|Divides a vector by a scalar value.|
|[static Divide(ref Vector3D, double, out Vector3D)](VRageMath.Vector3D@Divide)|Divides a vector by a scalar value.|
|[static DominantAxisProjection(Vector3D)](VRageMath.Vector3D@DominantAxisProjection)|Returns a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value.|
|[static DominantAxisProjection(ref Vector3D, out Vector3D)](VRageMath.Vector3D@DominantAxisProjection)|Calculates a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value. The result is saved into a user-specified variable.|
|[static Dot(Vector3D, Vector3D)](VRageMath.Vector3D@Dot)|Calculates the dot product of two vectors. If the two vectors are unit vectors, the dot product returns a doubleing point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Dot(Vector3D, Vector3)](VRageMath.Vector3D@Dot)||
|[static Dot(ref Vector3D, ref Vector3D, out double)](VRageMath.Vector3D@Dot)|Calculates the dot product of two vectors and writes the result to a user-specified variable. If the two vectors are unit vectors, the dot product returns a doubleing point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Dot(ref Vector3D, ref Vector3, out double)](VRageMath.Vector3D@Dot)||
|[static Dot(ref Vector3, ref Vector3D, out double)](VRageMath.Vector3D@Dot)||
|[static Floor(Vector3D)](VRageMath.Vector3D@Floor)||
|[static Fract(ref Vector3D, out Vector3D)](VRageMath.Vector3D@Fract)||
|[static GetAzimuthAndElevation(Vector3D, out double, out double)](VRageMath.Vector3D@GetAzimuthAndElevation)||
|[static Hermite(Vector3D, Vector3D, Vector3D, Vector3D, double)](VRageMath.Vector3D@Hermite)|Performs a Hermite spline interpolation.|
|[static Hermite(ref Vector3D, ref Vector3D, ref Vector3D, ref Vector3D, double, out Vector3D)](VRageMath.Vector3D@Hermite)|Performs a Hermite spline interpolation.|
|[static IsUnit(ref Vector3D)](VRageMath.Vector3D@IsUnit)||
|[static IsZero(Vector3D)](VRageMath.Vector3D@IsZero)||
|[static IsZero(Vector3D, double)](VRageMath.Vector3D@IsZero)||
|[static IsZeroVector(Vector3D)](VRageMath.Vector3D@IsZeroVector)||
|[static IsZeroVector(Vector3D, double)](VRageMath.Vector3D@IsZeroVector)||
|[static Lerp(Vector3D, Vector3D, double)](VRageMath.Vector3D@Lerp)|Performs a linear interpolation between two vectors.|
|[static Lerp(ref Vector3D, ref Vector3D, double, out Vector3D)](VRageMath.Vector3D@Lerp)|Performs a linear interpolation between two vectors.|
|[static Max(Vector3D, Vector3D)](VRageMath.Vector3D@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Max(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Min(Vector3D, Vector3D)](VRageMath.Vector3D@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Min(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static MinMax(ref Vector3D, ref Vector3D)](VRageMath.Vector3D@MinMax)|Separates minimal and maximal values of any two input vectors|
|[static Multiply(Vector3D, Vector3D)](VRageMath.Vector3D@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(Vector3D, double)](VRageMath.Vector3D@Multiply)|Multiplies a vector by a scalar value.|
|[static Multiply(ref Vector3D, double, out Vector3D)](VRageMath.Vector3D@Multiply)|Multiplies a vector by a scalar value.|
|[static Negate(Vector3D)](VRageMath.Vector3D@Negate)|Returns a vector pointing in the opposite direction.|
|[static Negate(ref Vector3D, out Vector3D)](VRageMath.Vector3D@Negate)|Returns a vector pointing in the opposite direction.|
|[static Normalize(Vector3D)](VRageMath.Vector3D@Normalize)|Creates a unit vector from the specified vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static Normalize(ref Vector3D, out Vector3D)](VRageMath.Vector3D@Normalize)|Creates a unit vector from the specified vector, writing the result to a user-specified variable. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static ProjectOnPlane(ref Vector3D, ref Vector3D)](VRageMath.Vector3D@ProjectOnPlane)|Projects given vector on plane specified by it's normal.|
|[static ProjectOnVector(ref Vector3D, ref Vector3D)](VRageMath.Vector3D@ProjectOnVector)|Projects vector on another vector resulting in new vector in guided vector's direction with different length.|
|[static RectangularDistance(Vector3D, Vector3D)](VRageMath.Vector3D@RectangularDistance)|Calculates rectangular distance (a.k.a. Manhattan distance or Chessboard distace) between two vectors.|
|[static RectangularDistance(ref Vector3D, ref Vector3D)](VRageMath.Vector3D@RectangularDistance)|Calculates rectangular distance (a.k.a. Manhattan distance or Chessboard distace) between two vectors.|
|[static Reflect(Vector3D, Vector3D)](VRageMath.Vector3D@Reflect)|Returns the reflection of a vector off a surface that has the specified normal. Reference page contains code sample.|
|[static Reflect(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Reflect)|Returns the reflection of a vector off a surface that has the specified normal. Reference page contains code sample.|
|[static Reject(Vector3D, Vector3D)](VRageMath.Vector3D@Reject)|Returns the rejection of vector from direction, i.e. projection of vector onto the plane defined by origin and direction|
|[static Reject(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Reject)|Returns the rejection of vector from direction, i.e. projection of vector onto the plane defined by origin and direction|
|[static Rotate(ref Vector3D, ref MatrixD, out Vector3D)](VRageMath.Vector3D@Rotate)||
|[static Rotate(Vector3D, MatrixD)](VRageMath.Vector3D@Rotate)||
|[static RotateAndScale(ref Vector3D, ref MatrixD, out Vector3D)](VRageMath.Vector3D@RotateAndScale)||
|[static Round(Vector3D)](VRageMath.Vector3D@Round)||
|[static Round(Vector3D, int)](VRageMath.Vector3D@Round)||
|[static Sign(Vector3D)](VRageMath.Vector3D@Sign)||
|[static SignNonZero(Vector3D)](VRageMath.Vector3D@SignNonZero)|Returns per component sign, never returns zero. For zero component returns sign 1. Faster than Sign.|
|[static SmoothStep(Vector3D, Vector3D, double)](VRageMath.Vector3D@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(ref Vector3D, ref Vector3D, double, out Vector3D)](VRageMath.Vector3D@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static Step(Vector3D)](VRageMath.Vector3D@Step)||
|[static Subtract(Vector3D, Vector3D)](VRageMath.Vector3D@Subtract)|Subtracts a vector from a vector.|
|[static Subtract(ref Vector3D, ref Vector3D, out Vector3D)](VRageMath.Vector3D@Subtract)|Subtracts a vector from a vector.|
|[static SwapYZCoordinates(Vector3D)](VRageMath.Vector3D@SwapYZCoordinates)||
|[static Transform(Vector3D, Quaternion)](VRageMath.Vector3D@Transform)|Transforms a Vector3 by a specified Quaternion rotation.|
|[static Transform(Vector3D, QuaternionD)](VRageMath.Vector3D@Transform)|Transforms a Vector3 by a specified Quaternion rotation.|
|[static Transform(ref Vector3D, ref Quaternion, out Vector3D)](VRageMath.Vector3D@Transform)|Transforms a Vector3 by a specified Quaternion rotation.|
|[static Transform(Vector3D[], ref MatrixD, Vector3D[])](VRageMath.Vector3D@Transform)|Transforms a source array of Vector3s by a specified Matrix and writes the results to an existing destination array.|
|[static Transform(Vector3D[], ref MatrixD, *Vector3D)](VRageMath.Vector3D@Transform)||
|[static Transform(Vector3D[], int, ref Matrix, Vector3D[], int, int)](VRageMath.Vector3D@Transform)|Applies a specified transform Matrix to a specified range of an array of Vector3s and writes the results into a specified range of a destination array.|
|[static Transform(Vector3D[], ref Quaternion, Vector3D[])](VRageMath.Vector3D@Transform)|Transforms a source array of Vector3s by a specified Quaternion rotation and writes the results to an existing destination array.|
|[static Transform(Vector3D[], int, ref Quaternion, Vector3D[], int, int)](VRageMath.Vector3D@Transform)|Applies a specified Quaternion rotation to a specified range of an array of Vector3s and writes the results into a specified range of a destination array.|
|[static Transform(Vector3D, MatrixD)](VRageMath.Vector3D@Transform)|Transforms a 3D vector by the given matrix.|
|[static Transform(Vector3, MatrixD)](VRageMath.Vector3D@Transform)||
|[static Transform(Vector3D, Matrix)](VRageMath.Vector3D@Transform)|Transforms a 3D vector by the given matrix.|
|[static Transform(Vector3D, ref MatrixD)](VRageMath.Vector3D@Transform)||
|[static Transform(ref Vector3D, ref MatrixD, out Vector3D)](VRageMath.Vector3D@Transform)|Transforms a Vector3 by the given Matrix.|
|[static Transform(ref Vector3, ref MatrixD, out Vector3D)](VRageMath.Vector3D@Transform)||
|[static Transform(ref Vector3D, ref MatrixI, out Vector3D)](VRageMath.Vector3D@Transform)||
|[static TransformNoProjection(ref Vector3D, ref MatrixD, out Vector3D)](VRageMath.Vector3D@TransformNoProjection)||
|[static TransformNormal(Vector3D, MatrixD)](VRageMath.Vector3D@TransformNormal)|Transforms a 3D vector normal by a matrix.|
|[static TransformNormal(ref Vector3D, ref MatrixD, out Vector3D)](VRageMath.Vector3D@TransformNormal)|Transforms a vector normal by a matrix.|
|[static TransformNormal(ref Vector3, ref MatrixD, out Vector3D)](VRageMath.Vector3D@TransformNormal)||
|[static TransformNormal(ref Vector3D, ref MatrixI, out Vector3D)](VRageMath.Vector3D@TransformNormal)||
|[static TransformNormal(Vector3D, MyBlockOrientation)](VRageMath.Vector3D@TransformNormal)||
|[static TransformNormal(ref Vector3D, MyBlockOrientation, out Vector3D)](VRageMath.Vector3D@TransformNormal)||
|[static TransformNormal(Vector3D, ref MatrixD)](VRageMath.Vector3D@TransformNormal)||
|[static TransformNormal(Vector3D[], ref Matrix, Vector3D[])](VRageMath.Vector3D@TransformNormal)|Transforms an array of 3D vector normals by a specified Matrix.|
|[static TransformNormal(Vector3D[], ref Matrix, *Vector3D)](VRageMath.Vector3D@TransformNormal)||
|[static TransformNormal(Vector3D[], int, ref Matrix, Vector3D[], int, int)](VRageMath.Vector3D@TransformNormal)|Transforms a specified range in an array of 3D vector normals by a specified Matrix and writes the results to a specified range in a destination array.|
|[static TransformNormal(Vector3D, Matrix)](VRageMath.Vector3D@TransformNormal)|Transforms a 3D vector normal by a matrix.|
|[static TransformNormal(Vector3, MatrixD)](VRageMath.Vector3D@TransformNormal)|Transforms a 3D vector normal by a matrix.|
|[static TryParse(string, out Vector3D)](VRageMath.Vector3D@TryParse)||
|[AbsMax()](VRageMath.Vector3D@AbsMax)|Returns the component of the vector, whose absolute value is largest of all the three components.|
|[AbsMaxComponent()](VRageMath.Vector3D@AbsMaxComponent)||
|[AbsMin()](VRageMath.Vector3D@AbsMin)|Returns the component of the vector, whose absolute value is smallest of all the three components.|
|[AssertIsValid()](VRageMath.Vector3D@AssertIsValid)||
|[CalculatePerpendicularVector(out Vector3D)](VRageMath.Vector3D@CalculatePerpendicularVector)||
|[Cross(Vector3D)](VRageMath.Vector3D@Cross)||
|[Dot(Vector3D)](VRageMath.Vector3D@Dot)||
|[Dot(Vector3)](VRageMath.Vector3D@Dot)||
|[Dot(ref Vector3D)](VRageMath.Vector3D@Dot)||
|[Equals(Vector3D)](VRageMath.Vector3D@Equals)|Determines whether the specified Object is equal to the Vector3.|
|[Equals(Vector3D, double)](VRageMath.Vector3D@Equals)||
|[Equals(object)](VRageMath.Vector3D@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetDim(int)](VRageMath.Vector3D@GetDim)||
|[GetHash()](VRageMath.Vector3D@GetHash)|Gets the hash code of the vector object.|
|[GetHashCode()](VRageMath.Vector3D@GetHashCode)||
|[Interpolate3(Vector3D, Vector3D, double)](VRageMath.Vector3D@Interpolate3)||
|[IsInsideInclusive(ref Vector3D, ref Vector3D)](VRageMath.Vector3D@IsInsideInclusive)||
|[IsValid()](VRageMath.Vector3D@IsValid)||
|[IsZero()](VRageMath.Vector3D@IsZero)||
|[Length()](VRageMath.Vector3D@Length)|Calculates the length of the vector.|
|[LengthSquared()](VRageMath.Vector3D@LengthSquared)|Calculates the length of the vector squared.|
|[Max()](VRageMath.Vector3D@Max)|Returns the component of the vector that is largest of all the three components.|
|[Min()](VRageMath.Vector3D@Min)|Returns the component of the vector that is smallest of all the three components.|
|[Normalize()](VRageMath.Vector3D@Normalize)|Turns the current vector into a unit vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[Normalized()](VRageMath.Vector3D@Normalized)|Creates a unit vector from the specified vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[Rotate(Vector3D, double)](VRageMath.Vector3D@Rotate)||
|[SetDim(int, double)](VRageMath.Vector3D@SetDim)||
|[ToString()](VRageMath.Vector3D@ToString)|Retrieves a string representation of the current object.|
|[ToString(string)](VRageMath.Vector3D@ToString)||
|[VolumeInt(double)](VRageMath.Vector3D@VolumeInt)||

**Implements:**  
* [IEquatable<Vector3D>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

