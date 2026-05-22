**Assembly:** VRage.Math.dll

```csharp
public struct Vector3: IEquatable<Vector3>
```

Defines a vector with three components.

## Fields

|Member|Description|
|---|---|
|[static Backward](VRageMath.Vector3@Backward)||
|[static Down](VRageMath.Vector3@Down)||
|[static Forward](VRageMath.Vector3@Forward)||
|[static Half](VRageMath.Vector3@Half)||
|[static Invalid](VRageMath.Vector3@Invalid)||
|[static Left](VRageMath.Vector3@Left)||
|[static MaxValue](VRageMath.Vector3@MaxValue)||
|[static MinusOne](VRageMath.Vector3@MinusOne)||
|[static MinValue](VRageMath.Vector3@MinValue)||
|[static NegativeInfinity](VRageMath.Vector3@NegativeInfinity)||
|[static One](VRageMath.Vector3@One)||
|[static PositiveInfinity](VRageMath.Vector3@PositiveInfinity)||
|[static Right](VRageMath.Vector3@Right)||
|[static UnitX](VRageMath.Vector3@UnitX)||
|[static UnitY](VRageMath.Vector3@UnitY)||
|[static UnitZ](VRageMath.Vector3@UnitZ)||
|[static Up](VRageMath.Vector3@Up)||
|[static Zero](VRageMath.Vector3@Zero)||
|[X](VRageMath.Vector3@X)|Gets or sets the x-component of the vector.|
|[Y](VRageMath.Vector3@Y)|Gets or sets the y-component of the vector.|
|[Z](VRageMath.Vector3@Z)|Gets or sets the z-component of the vector.|

## Properties

|Member|Description|
|---|---|
|[Sum](VRageMath.Vector3@Sum)||
|[Volume](VRageMath.Vector3@Volume)||

## Constructors

|Member|Description|
|---|---|
|[Vector3(float, float, float)](VRageMath.Vector3@.ctor)||
|[Vector3(double, double, double)](VRageMath.Vector3@.ctor)||
|[Vector3(float)](VRageMath.Vector3@.ctor)||
|[Vector3(Vector2, float)](VRageMath.Vector3@.ctor)||
|[Vector3(Vector4)](VRageMath.Vector3@.ctor)||
|[Vector3(ref Vector3I)](VRageMath.Vector3@.ctor)||
|[Vector3(Vector3I)](VRageMath.Vector3@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Abs(Vector3)](VRageMath.Vector3@Abs)||
|[static Add(Vector3, Vector3)](VRageMath.Vector3@Add)|Adds two vectors.|
|[static Add(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Add)|Adds two vectors.|
|[static Angle(Vector3, Vector3)](VRageMath.Vector3@Angle)|Gets angle between 2 vectors in radians|
|[static ArePerpendicular(ref Vector3, ref Vector3)](VRageMath.Vector3@ArePerpendicular)||
|[static ArePerpendicular(Vector3, Vector3)](VRageMath.Vector3@ArePerpendicular)||
|[static Barycentric(Vector3, Vector3, Vector3, float, float)](VRageMath.Vector3@Barycentric)|Returns a Vector3 containing the 3D Cartesian coordinates of a point specified in Barycentric coordinates relative to a 3D triangle.|
|[static Barycentric(ref Vector3, ref Vector3, ref Vector3, float, float, out Vector3)](VRageMath.Vector3@Barycentric)|Returns a Vector3 containing the 3D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 3D triangle.|
|[static Barycentric(Vector3, Vector3, Vector3, Vector3, out float, out float, out float)](VRageMath.Vector3@Barycentric)|Compute barycentric coordinates (u, v, w) for point p with respect to triangle (a, b, c) From : Real-Time Collision Detection, Christer Ericson, CRC Press 3.4 Barycentric Coordinates|
|[static CalculatePerpendicularVector(Vector3)](VRageMath.Vector3@CalculatePerpendicularVector)||
|[static CatmullRom(Vector3, Vector3, Vector3, Vector3, float)](VRageMath.Vector3@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CatmullRom(ref Vector3, ref Vector3, ref Vector3, ref Vector3, float, out Vector3)](VRageMath.Vector3@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static Ceiling(Vector3)](VRageMath.Vector3@Ceiling)||
|[static Clamp(Vector3, Vector3, Vector3)](VRageMath.Vector3@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(Vector3, Vector3, Vector3, out Vector3, out Vector3, out Vector3)](VRageMath.Vector3@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(ref Vector3, ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Clamp)|Restricts a value to be within a specified range.|
|[static ClampToSphere(Vector3, float)](VRageMath.Vector3@ClampToSphere)||
|[static ClampToSphere(ref Vector3, float)](VRageMath.Vector3@ClampToSphere)||
|[static CreateFromAzimuthAndElevation(float, float, out Vector3)](VRageMath.Vector3@CreateFromAzimuthAndElevation)||
|[static Cross(Vector3, Vector3)](VRageMath.Vector3@Cross)|Calculates the cross product of two vectors.|
|[static Cross(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Cross)|Calculates the cross product of two vectors.|
|[static Distance(Vector3, Vector3)](VRageMath.Vector3@Distance)|Calculates the distance between two vectors.|
|[static Distance(ref Vector3, ref Vector3, out float)](VRageMath.Vector3@Distance)|Calculates the distance between two vectors.|
|[static DistanceSquared(Vector3, Vector3)](VRageMath.Vector3@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static DistanceSquared(ref Vector3, ref Vector3, out float)](VRageMath.Vector3@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static Divide(Vector3, Vector3)](VRageMath.Vector3@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(Vector3, float)](VRageMath.Vector3@Divide)|Divides a vector by a scalar value.|
|[static Divide(ref Vector3, float, out Vector3)](VRageMath.Vector3@Divide)|Divides a vector by a scalar value.|
|[static DominantAxisProjection(Vector3)](VRageMath.Vector3@DominantAxisProjection)|Returns a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value.|
|[static DominantAxisProjection(ref Vector3, out Vector3)](VRageMath.Vector3@DominantAxisProjection)|Calculates a vector that is equal to the projection of the input vector to the coordinate axis that corresponds to the original vector's largest value. The result is saved into a user-specified variable.|
|[static Dot(Vector3, Vector3)](VRageMath.Vector3@Dot)|Calculates the dot product of two vectors. If the two vectors are unit vectors, the dot product returns a floating point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Dot(ref Vector3, ref Vector3, out float)](VRageMath.Vector3@Dot)|Calculates the dot product of two vectors and writes the result to a user-specified variable. If the two vectors are unit vectors, the dot product returns a floating point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Floor(Vector3)](VRageMath.Vector3@Floor)||
|[static GetAzimuthAndElevation(Vector3, out float, out float)](VRageMath.Vector3@GetAzimuthAndElevation)||
|[static GetNormalized(ref Vector3)](VRageMath.Vector3@GetNormalized)||
|[static Hermite(Vector3, Vector3, Vector3, Vector3, float)](VRageMath.Vector3@Hermite)|Performs a Hermite spline interpolation.|
|[static Hermite(ref Vector3, ref Vector3, ref Vector3, ref Vector3, float, out Vector3)](VRageMath.Vector3@Hermite)|Performs a Hermite spline interpolation.|
|[static IsUnit(ref Vector3)](VRageMath.Vector3@IsUnit)||
|[static IsZero(ref Vector3)](VRageMath.Vector3@IsZero)||
|[static IsZero(Vector3)](VRageMath.Vector3@IsZero)||
|[static IsZero(Vector3, float)](VRageMath.Vector3@IsZero)||
|[static IsZeroVector(Vector3)](VRageMath.Vector3@IsZeroVector)||
|[static IsZeroVector(Vector3, float)](VRageMath.Vector3@IsZeroVector)||
|[static Lerp(Vector3, Vector3, float)](VRageMath.Vector3@Lerp)|Performs a linear interpolation between two vectors.|
|[static Lerp(ref Vector3, ref Vector3, float, out Vector3)](VRageMath.Vector3@Lerp)|Performs a linear interpolation between two vectors.|
|[static Max(Vector3, Vector3)](VRageMath.Vector3@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Max(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Min(Vector3, Vector3)](VRageMath.Vector3@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Min(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static MinMax(ref Vector3, ref Vector3)](VRageMath.Vector3@MinMax)|Separates minimal and maximal values of any two input vectors|
|[static Multiply(Vector3, Vector3)](VRageMath.Vector3@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(Vector3, float)](VRageMath.Vector3@Multiply)|Multiplies a vector by a scalar value.|
|[static Multiply(ref Vector3, float, out Vector3)](VRageMath.Vector3@Multiply)|Multiplies a vector by a scalar value.|
|[static Negate(Vector3)](VRageMath.Vector3@Negate)|Returns a vector pointing in the opposite direction.|
|[static Negate(ref Vector3, out Vector3)](VRageMath.Vector3@Negate)|Returns a vector pointing in the opposite direction.|
|[static Normalize(Vector3)](VRageMath.Vector3@Normalize)|Creates a unit vector from the specified vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static Normalize(Vector3D)](VRageMath.Vector3@Normalize)||
|[static Normalize(ref Vector3, out Vector3)](VRageMath.Vector3@Normalize)|Creates a unit vector from the specified vector, writing the result to a user-specified variable. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static ProjectOnPlane(ref Vector3, ref Vector3)](VRageMath.Vector3@ProjectOnPlane)|Projects given vector on plane specified by it's normal.|
|[static ProjectOnVector(ref Vector3, ref Vector3)](VRageMath.Vector3@ProjectOnVector)|Projects vector on another vector resulting in new vector in guided vector's direction with different length.|
|[static RectangularDistance(Vector3, Vector3)](VRageMath.Vector3@RectangularDistance)|Calculates rectangular distance (a.k.a. Manhattan distance or Chessboard distace) between two vectors.|
|[static RectangularDistance(ref Vector3, ref Vector3)](VRageMath.Vector3@RectangularDistance)|Calculates rectangular distance (a.k.a. Manhattan distance or Chessboard distace) between two vectors.|
|[static Reflect(Vector3, Vector3)](VRageMath.Vector3@Reflect)|Returns the reflection of a vector off a surface that has the specified normal. Reference page contains code sample.|
|[static Reflect(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Reflect)|Returns the reflection of a vector off a surface that has the specified normal. Reference page contains code sample.|
|[static Reject(Vector3, Vector3)](VRageMath.Vector3@Reject)|Returns the rejection of vector from direction, i.e. projection of vector onto the plane defined by origin and direction|
|[static Reject(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Reject)|Returns the rejection of vector from direction, i.e. projection of vector onto the plane defined by origin and direction|
|[static RotateAndScale(ref Vector3, ref Matrix, out Vector3)](VRageMath.Vector3@RotateAndScale)||
|[static RotateAndScale(Vector3, Matrix)](VRageMath.Vector3@RotateAndScale)||
|[static Round(Vector3)](VRageMath.Vector3@Round)||
|[static Round(Vector3, int)](VRageMath.Vector3@Round)||
|[static Sign(Vector3)](VRageMath.Vector3@Sign)||
|[static Sign(Vector3, float)](VRageMath.Vector3@Sign)||
|[static SignNonZero(Vector3)](VRageMath.Vector3@SignNonZero)|Returns per component sign, never returns zero. For zero component returns sign 1. Faster than Sign.|
|[static SmoothStep(Vector3, Vector3, float)](VRageMath.Vector3@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(ref Vector3, ref Vector3, float, out Vector3)](VRageMath.Vector3@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static Step(Vector3)](VRageMath.Vector3@Step)||
|[static Subtract(Vector3, Vector3)](VRageMath.Vector3@Subtract)|Subtracts a vector from a vector.|
|[static Subtract(ref Vector3, ref Vector3, out Vector3)](VRageMath.Vector3@Subtract)|Subtracts a vector from a vector.|
|[static SwapYZCoordinates(Vector3)](VRageMath.Vector3@SwapYZCoordinates)||
|[static Transform(Vector3[], ref Quaternion, Vector3[])](VRageMath.Vector3@Transform)|Transforms a source array of Vector3s by a specified Quaternion rotation and writes the results to an existing destination array.|
|[static Transform(Vector3[], int, ref Quaternion, Vector3[], int, int)](VRageMath.Vector3@Transform)|Applies a specified Quaternion rotation to a specified range of an array of Vector3s and writes the results into a specified range of a destination array.|
|[static Transform(Vector3, Matrix)](VRageMath.Vector3@Transform)|Transforms a 3D vector by the given matrix.|
|[static Transform(Vector3, MatrixD)](VRageMath.Vector3@Transform)|Transforms a 3D vector by the given matrix.|
|[static Transform(Vector3, ref Matrix)](VRageMath.Vector3@Transform)||
|[static Transform(ref Vector3, ref Matrix, out Vector3)](VRageMath.Vector3@Transform)|Transforms a Vector3 by the given Matrix.|
|[static Transform(ref Vector3, ref MatrixI, out Vector3)](VRageMath.Vector3@Transform)||
|[static Transform(Vector3, Quaternion)](VRageMath.Vector3@Transform)|Transforms a Vector3 by a specified Quaternion rotation.|
|[static Transform(ref Vector3, ref Quaternion, out Vector3)](VRageMath.Vector3@Transform)|Transforms a Vector3 by a specified Quaternion rotation.|
|[static Transform(Vector3[], ref Matrix, Vector3[])](VRageMath.Vector3@Transform)|Transforms a source array of Vector3s by a specified Matrix and writes the results to an existing destination array.|
|[static Transform(Vector3[], int, ref Matrix, Vector3[], int, int)](VRageMath.Vector3@Transform)|Applies a specified transform Matrix to a specified range of an array of Vector3s and writes the results into a specified range of a destination array.|
|[static TransformNoProjection(ref Vector3, ref Matrix, out Vector3)](VRageMath.Vector3@TransformNoProjection)||
|[static TransformNormal(Vector3, Matrix)](VRageMath.Vector3@TransformNormal)|Transforms a 3D vector normal by a matrix.|
|[static TransformNormal(Vector3, MatrixD)](VRageMath.Vector3@TransformNormal)|Transforms a 3D vector normal by a matrix.|
|[static TransformNormal(Vector3D, Matrix)](VRageMath.Vector3@TransformNormal)|Transforms a 3D vector normal by a matrix.|
|[static TransformNormal(ref Vector3, ref Matrix, out Vector3)](VRageMath.Vector3@TransformNormal)|Transforms a vector normal by a matrix.|
|[static TransformNormal(ref Vector3, ref MatrixD, out Vector3)](VRageMath.Vector3@TransformNormal)||
|[static TransformNormal(ref Vector3, ref MatrixI, out Vector3)](VRageMath.Vector3@TransformNormal)||
|[static TransformNormal(Vector3, MyBlockOrientation)](VRageMath.Vector3@TransformNormal)||
|[static TransformNormal(ref Vector3, MyBlockOrientation, out Vector3)](VRageMath.Vector3@TransformNormal)||
|[static TransformNormal(Vector3, ref Matrix)](VRageMath.Vector3@TransformNormal)||
|[static TransformNormal(Vector3[], ref Matrix, Vector3[])](VRageMath.Vector3@TransformNormal)|Transforms an array of 3D vector normals by a specified Matrix.|
|[static TransformNormal(Vector3[], int, ref Matrix, Vector3[], int, int)](VRageMath.Vector3@TransformNormal)|Transforms a specified range in an array of 3D vector normals by a specified Matrix and writes the results to a specified range in a destination array.|
|[static TransformProjection(ref Vector3, ref Matrix, out Vector3)](VRageMath.Vector3@TransformProjection)|Transforms a Vector3 by the given projection matrix (both ortho and perspective are supported)|
|[static TriangleArea(Vector3, Vector3, Vector3)](VRageMath.Vector3@TriangleArea)||
|[static TriangleArea(ref Vector3, ref Vector3, ref Vector3)](VRageMath.Vector3@TriangleArea)||
|[AbsMax()](VRageMath.Vector3@AbsMax)|Returns the component of the vector, whose absolute value is largest of all the three components.|
|[AbsMin()](VRageMath.Vector3@AbsMin)|Returns the component of the vector, whose absolute value is smallest of all the three components.|
|[Add(Vector3)](VRageMath.Vector3@Add)||
|[AssertIsValid()](VRageMath.Vector3@AssertIsValid)||
|[CalculatePerpendicularVector(out Vector3)](VRageMath.Vector3@CalculatePerpendicularVector)||
|[Cross(Vector3)](VRageMath.Vector3@Cross)||
|[Divide(float)](VRageMath.Vector3@Divide)||
|[Dot(Vector3)](VRageMath.Vector3@Dot)||
|[Dot(ref Vector3)](VRageMath.Vector3@Dot)||
|[Equals(Vector3)](VRageMath.Vector3@Equals)|Determines whether the specified Object is equal to the Vector3.|
|[Equals(Vector3, float)](VRageMath.Vector3@Equals)||
|[Equals(object)](VRageMath.Vector3@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetDim(int)](VRageMath.Vector3@GetDim)||
|[GetHash()](VRageMath.Vector3@GetHash)|Gets the hash code of the vector object.|
|[GetHashCode()](VRageMath.Vector3@GetHashCode)||
|[Interpolate3(Vector3, Vector3, float)](VRageMath.Vector3@Interpolate3)||
|[IsInsideInclusive(ref Vector3, ref Vector3)](VRageMath.Vector3@IsInsideInclusive)||
|[IsValid()](VRageMath.Vector3@IsValid)||
|[Length()](VRageMath.Vector3@Length)|Calculates the length of the vector.|
|[LengthSquared()](VRageMath.Vector3@LengthSquared)|Calculates the length of the vector squared.|
|[Max()](VRageMath.Vector3@Max)|Returns the component of the vector that is largest of all the three components.|
|[MaxAbsComponent()](VRageMath.Vector3@MaxAbsComponent)|Keeps only component with maximal absolute, others are set to zero.|
|[Min()](VRageMath.Vector3@Min)|Returns the component of the vector that is smallest of all the three components.|
|[Multiply(float)](VRageMath.Vector3@Multiply)||
|[Normalize()](VRageMath.Vector3@Normalize)|Turns the current vector into a unit vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[Normalized()](VRageMath.Vector3@Normalized)|Creates a unit vector from the specified vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[SetDim(int, float)](VRageMath.Vector3@SetDim)||
|[ToString()](VRageMath.Vector3@ToString)|Retrieves a string representation of the current object.|
|[ToString(string)](VRageMath.Vector3@ToString)||
|[VolumeInt(float)](VRageMath.Vector3@VolumeInt)||

**Implements:**  
* [IEquatable<Vector3>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

