**Assembly:** VRage.Math.dll

```csharp
public struct Vector2: IEquatable<Vector2>
```

Defines a vector with two components.

## Fields

|Member|Description|
|---|---|
|[static One](VRageMath.Vector2@One)||
|[static PositiveInfinity](VRageMath.Vector2@PositiveInfinity)||
|[static UnitX](VRageMath.Vector2@UnitX)||
|[static UnitY](VRageMath.Vector2@UnitY)||
|[static Zero](VRageMath.Vector2@Zero)||
|[X](VRageMath.Vector2@X)|Gets or sets the x-component of the vector.|
|[Y](VRageMath.Vector2@Y)|Gets or sets the y-component of the vector.|

## Properties

|Member|Description|
|---|---|
|[Item](VRageMath.Vector2@Item)||

## Constructors

|Member|Description|
|---|---|
|[Vector2(float, float)](VRageMath.Vector2@.ctor)||
|[Vector2(float)](VRageMath.Vector2@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(Vector2, Vector2)](VRageMath.Vector2@Add)|Adds two vectors.|
|[static Add(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Add)|Adds two vectors.|
|[static Barycentric(Vector2, Vector2, Vector2, float, float)](VRageMath.Vector2@Barycentric)|Returns a Vector2 containing the 2D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 2D triangle.|
|[static Barycentric(ref Vector2, ref Vector2, ref Vector2, float, float, out Vector2)](VRageMath.Vector2@Barycentric)|Returns a Vector2 containing the 2D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 2D triangle.|
|[static CatmullRom(Vector2, Vector2, Vector2, Vector2, float)](VRageMath.Vector2@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CatmullRom(ref Vector2, ref Vector2, ref Vector2, ref Vector2, float, out Vector2)](VRageMath.Vector2@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static Clamp(Vector2, Vector2, Vector2)](VRageMath.Vector2@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(ref Vector2, ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Clamp)|Restricts a value to be within a specified range.|
|[static ClampToSphere(Vector2, float)](VRageMath.Vector2@ClampToSphere)||
|[static ClampToSphere(ref Vector2, float)](VRageMath.Vector2@ClampToSphere)||
|[static Distance(Vector2, Vector2)](VRageMath.Vector2@Distance)|Calculates the distance between two vectors.|
|[static Distance(ref Vector2, ref Vector2, out float)](VRageMath.Vector2@Distance)|Calculates the distance between two vectors.|
|[static DistanceSquared(Vector2, Vector2)](VRageMath.Vector2@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static DistanceSquared(ref Vector2, ref Vector2, out float)](VRageMath.Vector2@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static Divide(Vector2, Vector2)](VRageMath.Vector2@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(Vector2, float)](VRageMath.Vector2@Divide)|Divides a vector by a scalar value.|
|[static Divide(ref Vector2, float, out Vector2)](VRageMath.Vector2@Divide)|Divides a vector by a scalar value.|
|[static Dot(Vector2, Vector2)](VRageMath.Vector2@Dot)|Calculates the dot product of two vectors. If the two vectors are unit vectors, the dot product returns a floating point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Dot(ref Vector2, ref Vector2, out float)](VRageMath.Vector2@Dot)|Calculates the dot product of two vectors and writes the result to a user-specified variable. If the two vectors are unit vectors, the dot product returns a floating point value between -1 and 1 that can be used to determine some properties of the angle between two vectors. For example, it can show whether the vectors are orthogonal, parallel, or have an acute or obtuse angle between them.|
|[static Floor(Vector2)](VRageMath.Vector2@Floor)||
|[static Hermite(Vector2, Vector2, Vector2, Vector2, float)](VRageMath.Vector2@Hermite)|Performs a Hermite spline interpolation.|
|[static Hermite(ref Vector2, ref Vector2, ref Vector2, ref Vector2, float, out Vector2)](VRageMath.Vector2@Hermite)|Performs a Hermite spline interpolation.|
|[static IsZero(ref Vector2)](VRageMath.Vector2@IsZero)||
|[static IsZero(ref Vector2, float)](VRageMath.Vector2@IsZero)||
|[static IsZero(Vector2, float)](VRageMath.Vector2@IsZero)||
|[static Lerp(Vector2, Vector2, float)](VRageMath.Vector2@Lerp)|Performs a linear interpolation between two vectors.|
|[static Lerp(ref Vector2, ref Vector2, float, out Vector2)](VRageMath.Vector2@Lerp)|Performs a linear interpolation between two vectors.|
|[static Max(Vector2, Vector2)](VRageMath.Vector2@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Max(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Min(Vector2, Vector2)](VRageMath.Vector2@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Min(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Multiply(Vector2, Vector2)](VRageMath.Vector2@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(Vector2, float)](VRageMath.Vector2@Multiply)|Multiplies a vector by a scalar value.|
|[static Multiply(ref Vector2, float, out Vector2)](VRageMath.Vector2@Multiply)|Multiplies a vector by a scalar value.|
|[static Negate(Vector2)](VRageMath.Vector2@Negate)|Returns a vector pointing in the opposite direction.|
|[static Negate(ref Vector2, out Vector2)](VRageMath.Vector2@Negate)|Returns a vector pointing in the opposite direction.|
|[static Normalize(Vector2)](VRageMath.Vector2@Normalize)|Creates a unit vector from the specified vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static Normalize(ref Vector2, out Vector2)](VRageMath.Vector2@Normalize)|Creates a unit vector from the specified vector, writing the result to a user-specified variable. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[static Reflect(Vector2, Vector2)](VRageMath.Vector2@Reflect)|Determines the reflect vector of the given vector and normal.|
|[static Reflect(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Reflect)|Determines the reflect vector of the given vector and normal.|
|[static SignNonZero(Vector2)](VRageMath.Vector2@SignNonZero)||
|[static SmoothStep(Vector2, Vector2, float)](VRageMath.Vector2@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(ref Vector2, ref Vector2, float, out Vector2)](VRageMath.Vector2@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static Subtract(Vector2, Vector2)](VRageMath.Vector2@Subtract)|Subtracts a vector from a vector.|
|[static Subtract(ref Vector2, ref Vector2, out Vector2)](VRageMath.Vector2@Subtract)|Subtracts a vector from a vector.|
|[static Transform(Vector2, Matrix)](VRageMath.Vector2@Transform)|Transforms the vector (x, y, 0, 1) by the specified matrix.|
|[static Transform(ref Vector2, ref Matrix, out Vector2)](VRageMath.Vector2@Transform)|Transforms a Vector2 by the given Matrix.|
|[static Transform(Vector2, Quaternion)](VRageMath.Vector2@Transform)|Transforms a single Vector2, or the vector normal (x, y, 0, 0), by a specified Quaternion rotation.|
|[static Transform(ref Vector2, ref Quaternion, out Vector2)](VRageMath.Vector2@Transform)|Transforms a Vector2, or the vector normal (x, y, 0, 0), by a specified Quaternion rotation.|
|[static Transform(Vector2[], ref Matrix, Vector2[])](VRageMath.Vector2@Transform)|Transforms an array of Vector2s by a specified Matrix.|
|[static Transform(Vector2[], int, ref Matrix, Vector2[], int, int)](VRageMath.Vector2@Transform)|Transforms a specified range in an array of Vector2s by a specified Matrix and places the results in a specified range in a destination array.|
|[static Transform(Vector2[], ref Quaternion, Vector2[])](VRageMath.Vector2@Transform)|Transforms an array of Vector2s by a specified Quaternion.|
|[static Transform(Vector2[], int, ref Quaternion, Vector2[], int, int)](VRageMath.Vector2@Transform)|Transforms a specified range in an array of Vector2s by a specified Quaternion and places the results in a specified range in a destination array.|
|[static TransformNormal(Vector2, Matrix)](VRageMath.Vector2@TransformNormal)|Transforms a 2D vector normal by a matrix.|
|[static TransformNormal(ref Vector2, ref Matrix, out Vector2)](VRageMath.Vector2@TransformNormal)|Transforms a vector normal by a matrix.|
|[static TransformNormal(Vector2[], ref Matrix, Vector2[])](VRageMath.Vector2@TransformNormal)|Transforms an array of Vector2 vector normals by a specified Matrix.|
|[static TransformNormal(Vector2[], int, ref Matrix, Vector2[], int, int)](VRageMath.Vector2@TransformNormal)|Transforms a specified range in an array of Vector2 vector normals by a specified Matrix and places the results in a specified range in a destination array.|
|[AssertIsValid()](VRageMath.Vector2@AssertIsValid)||
|[Between(ref Vector2, ref Vector2)](VRageMath.Vector2@Between)||
|[Equals(Vector2)](VRageMath.Vector2@Equals)|Determines whether the specified Object is equal to the Vector2.|
|[Equals(object)](VRageMath.Vector2@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetHashCode()](VRageMath.Vector2@GetHashCode)|Gets the hash code of the vector object.|
|[IsValid()](VRageMath.Vector2@IsValid)||
|[Length()](VRageMath.Vector2@Length)|Calculates the length of the vector.|
|[LengthSquared()](VRageMath.Vector2@LengthSquared)|Calculates the length of the vector squared.|
|[Normalize()](VRageMath.Vector2@Normalize)|Turns the current vector into a unit vector. The result is a vector one unit in length pointing in the same direction as the original vector.|
|[Rotate(double)](VRageMath.Vector2@Rotate)||
|[ToString()](VRageMath.Vector2@ToString)|Retrieves a string representation of the current object.|

**Implements:**  
* [IEquatable<Vector2>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

