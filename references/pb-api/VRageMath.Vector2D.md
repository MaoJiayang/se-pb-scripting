**Assembly:** VRage.Math.dll

```csharp
public struct Vector2D: IEquatable<Vector2D>
```

Defines a vector with two components.

## Fields

|Member|Description|
|---|---|
|[static One](VRageMath.Vector2D@One)||
|[static PositiveInfinity](VRageMath.Vector2D@PositiveInfinity)||
|[static UnitX](VRageMath.Vector2D@UnitX)||
|[static UnitY](VRageMath.Vector2D@UnitY)||
|[static Zero](VRageMath.Vector2D@Zero)||
|[X](VRageMath.Vector2D@X)|Gets or sets the x-component of the vector.|
|[Y](VRageMath.Vector2D@Y)|Gets or sets the y-component of the vector.|

## Properties

|Member|Description|
|---|---|
|[Item](VRageMath.Vector2D@Item)||

## Constructors

|Member|Description|
|---|---|
|[Vector2D(double, double)](VRageMath.Vector2D@.ctor)||
|[Vector2D(double)](VRageMath.Vector2D@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(Vector2D, Vector2D)](VRageMath.Vector2D@Add)|Adds two vectors.|
|[static Add(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Add)|Adds two vectors.|
|[static Barycentric(Vector2D, Vector2D, Vector2D, double, double)](VRageMath.Vector2D@Barycentric)|Returns a Vector2D containing the 2D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 2D triangle.|
|[static Barycentric(ref Vector2D, ref Vector2D, ref Vector2D, double, double, out Vector2D)](VRageMath.Vector2D@Barycentric)|Returns a Vector2D containing the 2D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 2D triangle.|
|[static CatmullRom(Vector2D, Vector2D, Vector2D, Vector2D, double)](VRageMath.Vector2D@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CatmullRom(ref Vector2D, ref Vector2D, ref Vector2D, ref Vector2D, double, out Vector2D)](VRageMath.Vector2D@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static Clamp(Vector2D, Vector2D, Vector2D)](VRageMath.Vector2D@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(ref Vector2D, ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Clamp)|Restricts a value to be within a specified range.|
|[static ClampToSphere(Vector2D, double)](VRageMath.Vector2D@ClampToSphere)||
|[static ClampToSphere(ref Vector2D, double)](VRageMath.Vector2D@ClampToSphere)||
|[static Distance(Vector2D, Vector2D)](VRageMath.Vector2D@Distance)|Calculates the distance between two vectors.|
|[static Distance(ref Vector2D, ref Vector2D, out double)](VRageMath.Vector2D@Distance)|Calculates the distance between two vectors.|
|[static DistanceSquared(Vector2D, Vector2D)](VRageMath.Vector2D@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static DistanceSquared(ref Vector2D, ref Vector2D, out double)](VRageMath.Vector2D@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static Divide(Vector2D, Vector2D)](VRageMath.Vector2D@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(Vector2D, double)](VRageMath.Vector2D@Divide)|Divides a vector by a scalar value.|
|[static Divide(ref Vector2D, double, out Vector2D)](VRageMath.Vector2D@Divide)|Divides a vector by a scalar value.|
|[static Dot(Vector2D, Vector2D)](VRageMath.Vector2D@Dot)|Calculates the dot product of two vectors. If the two vectors are unit vectors, the dot product returns a doubleing point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Dot(ref Vector2D, ref Vector2D, out double)](VRageMath.Vector2D@Dot)|Calculates the dot product of two vectors and writes the result to a user-specified variable. If the two vectors are unit vectors, the dot product returns a doubleing point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Floor(Vector2D)](VRageMath.Vector2D@Floor)||
|[static Hermite(Vector2D, Vector2D, Vector2D, Vector2D, double)](VRageMath.Vector2D@Hermite)|Performs a Hermite spline interpolation.|
|[static Hermite(ref Vector2D, ref Vector2D, ref Vector2D, ref Vector2D, double, out Vector2D)](VRageMath.Vector2D@Hermite)|Performs a Hermite spline interpolation.|
|[static Lerp(Vector2D, Vector2D, double)](VRageMath.Vector2D@Lerp)|Performs a linear interpolation between two vectors.|
|[static Lerp(ref Vector2D, ref Vector2D, double, out Vector2D)](VRageMath.Vector2D@Lerp)|Performs a linear interpolation between two vectors.|
|[static Max(Vector2D, Vector2D)](VRageMath.Vector2D@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Max(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Min(Vector2D, Vector2D)](VRageMath.Vector2D@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Min(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Multiply(Vector2D, Vector2D)](VRageMath.Vector2D@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(Vector2D, double)](VRageMath.Vector2D@Multiply)|Multiplies a vector by a scalar value.|
|[static Multiply(ref Vector2D, double, out Vector2D)](VRageMath.Vector2D@Multiply)|Multiplies a vector by a scalar value.|
|[static Negate(Vector2D)](VRageMath.Vector2D@Negate)|Returns a vector pointing in the opposite direction.|
|[static Negate(ref Vector2D, out Vector2D)](VRageMath.Vector2D@Negate)|Returns a vector pointing in the opposite direction.|
|[static Normalize(Vector2D)](VRageMath.Vector2D@Normalize)|Creates a unit vector from the specified vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static Normalize(ref Vector2D, out Vector2D)](VRageMath.Vector2D@Normalize)|Creates a unit vector from the specified vector, writing the result to a user-specified variable. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static Reflect(Vector2D, Vector2D)](VRageMath.Vector2D@Reflect)|Determines the reflect vector of the given vector and normal.|
|[static Reflect(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Reflect)|Determines the reflect vector of the given vector and normal.|
|[static SmoothStep(Vector2D, Vector2D, double)](VRageMath.Vector2D@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(ref Vector2D, ref Vector2D, double, out Vector2D)](VRageMath.Vector2D@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static Subtract(Vector2D, Vector2D)](VRageMath.Vector2D@Subtract)|Subtracts a vector from a vector.|
|[static Subtract(ref Vector2D, ref Vector2D, out Vector2D)](VRageMath.Vector2D@Subtract)|Subtracts a vector from a vector.|
|[static Transform(Vector2D, Matrix)](VRageMath.Vector2D@Transform)|Transforms the vector (x, y, 0, 1) by the specified matrix.|
|[static Transform(ref Vector2D, ref Matrix, out Vector2D)](VRageMath.Vector2D@Transform)|Transforms a Vector2D by the given Matrix.|
|[static Transform(Vector2D, Quaternion)](VRageMath.Vector2D@Transform)|Transforms a single Vector2D, or the vector normal (x, y, 0, 0), by a specified Quaternion rotation.|
|[static Transform(ref Vector2D, ref Quaternion, out Vector2D)](VRageMath.Vector2D@Transform)|Transforms a Vector2D, or the vector normal (x, y, 0, 0), by a specified Quaternion rotation.|
|[static Transform(Vector2D[], ref Matrix, Vector2D[])](VRageMath.Vector2D@Transform)|Transforms an array of Vector2s by a specified Matrix.|
|[static Transform(Vector2D[], int, ref Matrix, Vector2D[], int, int)](VRageMath.Vector2D@Transform)|Transforms a specified range in an array of Vector2s by a specified Matrix and places the results in a specified range in a destination array.|
|[static Transform(Vector2D[], ref Quaternion, Vector2D[])](VRageMath.Vector2D@Transform)|Transforms an array of Vector2s by a specified Quaternion.|
|[static Transform(Vector2D[], int, ref Quaternion, Vector2D[], int, int)](VRageMath.Vector2D@Transform)|Transforms a specified range in an array of Vector2s by a specified Quaternion and places the results in a specified range in a destination array.|
|[static TransformNormal(Vector2D, Matrix)](VRageMath.Vector2D@TransformNormal)|Transforms a 2D vector normal by a matrix.|
|[static TransformNormal(ref Vector2D, ref Matrix, out Vector2D)](VRageMath.Vector2D@TransformNormal)|Transforms a vector normal by a matrix.|
|[static TransformNormal(Vector2D[], ref Matrix, Vector2D[])](VRageMath.Vector2D@TransformNormal)|Transforms an array of Vector2D vector normals by a specified Matrix.|
|[static TransformNormal(Vector2D[], int, ref Matrix, Vector2D[], int, int)](VRageMath.Vector2D@TransformNormal)|Transforms a specified range in an array of Vector2D vector normals by a specified Matrix and places the results in a specified range in a destination array.|
|[AssertIsValid()](VRageMath.Vector2D@AssertIsValid)||
|[Between(ref Vector2D, ref Vector2D)](VRageMath.Vector2D@Between)||
|[Equals(Vector2D)](VRageMath.Vector2D@Equals)|Determines whether the specified Object is equal to the Vector2D.|
|[Equals(object)](VRageMath.Vector2D@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetHashCode()](VRageMath.Vector2D@GetHashCode)|Gets the hash code of the vector object.|
|[IsValid()](VRageMath.Vector2D@IsValid)||
|[Length()](VRageMath.Vector2D@Length)|Calculates the length of the vector.|
|[LengthSquared()](VRageMath.Vector2D@LengthSquared)|Calculates the length of the vector squared.|
|[Normalize()](VRageMath.Vector2D@Normalize)|Turns the current vector into a unit vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[Rotate(double)](VRageMath.Vector2D@Rotate)||
|[ToString()](VRageMath.Vector2D@ToString)|Retrieves a string representation of the current object.|

**Implements:**  
* [IEquatable<Vector2D>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

