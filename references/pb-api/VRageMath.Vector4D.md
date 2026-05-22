**Assembly:** VRage.Math.dll

```csharp
public struct Vector4D: IEquatable<Vector4>
```

Defines a vector with four components.

## Fields

|Member|Description|
|---|---|
|[static One](VRageMath.Vector4D@One)||
|[static UnitW](VRageMath.Vector4D@UnitW)||
|[static UnitX](VRageMath.Vector4D@UnitX)||
|[static UnitY](VRageMath.Vector4D@UnitY)||
|[static UnitZ](VRageMath.Vector4D@UnitZ)||
|[static Zero](VRageMath.Vector4D@Zero)||
|[W](VRageMath.Vector4D@W)|Gets or sets the w-component of the vector.|
|[X](VRageMath.Vector4D@X)|Gets or sets the x-component of the vector.|
|[Y](VRageMath.Vector4D@Y)|Gets or sets the y-component of the vector.|
|[Z](VRageMath.Vector4D@Z)|Gets or sets the z-component of the vector.|

## Constructors

|Member|Description|
|---|---|
|[Vector4D(double, double, double, double)](VRageMath.Vector4D@.ctor)||
|[Vector4D(Vector2, double, double)](VRageMath.Vector4D@.ctor)||
|[Vector4D(Vector3D, double)](VRageMath.Vector4D@.ctor)||
|[Vector4D(double)](VRageMath.Vector4D@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(Vector4D, Vector4D)](VRageMath.Vector4D@Add)|Adds two vectors.|
|[static Add(ref Vector4D, ref Vector4D, out Vector4D)](VRageMath.Vector4D@Add)|Adds two vectors.|
|[static Barycentric(Vector4D, Vector4D, Vector4D, double, double)](VRageMath.Vector4D@Barycentric)|Returns a Vector4 containing the 4D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 4D triangle.|
|[static Barycentric(ref Vector4D, ref Vector4D, ref Vector4D, double, double, out Vector4D)](VRageMath.Vector4D@Barycentric)|Returns a Vector4 containing the 4D Cartesian coordinates of a point specified in Barycentric (areal) coordinates relative to a 4D triangle.|
|[static CatmullRom(Vector4D, Vector4D, Vector4D, Vector4D, double)](VRageMath.Vector4D@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CatmullRom(ref Vector4D, ref Vector4D, ref Vector4D, ref Vector4D, double, out Vector4D)](VRageMath.Vector4D@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static Clamp(Vector4D, Vector4D, Vector4D)](VRageMath.Vector4D@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(ref Vector4D, ref Vector4D, ref Vector4D, out Vector4D)](VRageMath.Vector4D@Clamp)|Restricts a value to be within a specified range.|
|[static Distance(Vector4, Vector4)](VRageMath.Vector4D@Distance)|Calculates the distance between two vectors.|
|[static Distance(ref Vector4, ref Vector4, out double)](VRageMath.Vector4D@Distance)|Calculates the distance between two vectors.|
|[static DistanceSquared(Vector4, Vector4)](VRageMath.Vector4D@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static DistanceSquared(ref Vector4, ref Vector4, out double)](VRageMath.Vector4D@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static Divide(Vector4D, Vector4D)](VRageMath.Vector4D@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(ref Vector4D, ref Vector4D, out Vector4D)](VRageMath.Vector4D@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(Vector4D, double)](VRageMath.Vector4D@Divide)|Divides a vector by a scalar value.|
|[static Divide(ref Vector4D, double, out Vector4D)](VRageMath.Vector4D@Divide)|Divides a vector by a scalar value.|
|[static Dot(Vector4, Vector4)](VRageMath.Vector4D@Dot)|Calculates the dot product of two vectors.|
|[static Dot(ref Vector4, ref Vector4, out double)](VRageMath.Vector4D@Dot)|Calculates the dot product of two vectors.|
|[static Hermite(Vector4D, Vector4D, Vector4D, Vector4D, double)](VRageMath.Vector4D@Hermite)|Performs a Hermite spline interpolation.|
|[static Hermite(ref Vector4D, ref Vector4D, ref Vector4D, ref Vector4D, double, out Vector4D)](VRageMath.Vector4D@Hermite)|Performs a Hermite spline interpolation.|
|[static Lerp(Vector4D, Vector4D, double)](VRageMath.Vector4D@Lerp)|Performs a linear interpolation between two vectors.|
|[static Lerp(ref Vector4D, ref Vector4D, double, out Vector4D)](VRageMath.Vector4D@Lerp)|Performs a linear interpolation between two vectors.|
|[static Max(Vector4, Vector4)](VRageMath.Vector4D@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Max(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4D@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Min(Vector4, Vector4)](VRageMath.Vector4D@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Min(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4D@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Multiply(Vector4D, Vector4D)](VRageMath.Vector4D@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4D@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(Vector4D, double)](VRageMath.Vector4D@Multiply)|Multiplies a vector by a scalar.|
|[static Multiply(ref Vector4D, double, out Vector4D)](VRageMath.Vector4D@Multiply)|Multiplies a vector by a scalar value.|
|[static Negate(Vector4D)](VRageMath.Vector4D@Negate)|Returns a vector pointing in the opposite direction.|
|[static Negate(ref Vector4D, out Vector4D)](VRageMath.Vector4D@Negate)|Returns a vector pointing in the opposite direction.|
|[static Normalize(Vector4D)](VRageMath.Vector4D@Normalize)|Creates a unit vector from the specified vector.|
|[static Normalize(ref Vector4D, out Vector4D)](VRageMath.Vector4D@Normalize)|Returns a normalized version of the specified vector.|
|[static PackOrthoMatrix(Vector3D, Vector3, Vector3)](VRageMath.Vector4D@PackOrthoMatrix)||
|[static PackOrthoMatrix(ref MatrixD)](VRageMath.Vector4D@PackOrthoMatrix)||
|[static SmoothStep(Vector4D, Vector4D, double)](VRageMath.Vector4D@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(ref Vector4D, ref Vector4D, double, out Vector4D)](VRageMath.Vector4D@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static Subtract(Vector4, Vector4)](VRageMath.Vector4D@Subtract)|Subtracts a vector from a vector.|
|[static Subtract(ref Vector4D, ref Vector4D, out Vector4D)](VRageMath.Vector4D@Subtract)|Subtracts a vector from a vector.|
|[static Transform(Vector2, MatrixD)](VRageMath.Vector4D@Transform)|Transforms a Vector2 by the given Matrix.|
|[static Transform(ref Vector2, ref MatrixD, out Vector4D)](VRageMath.Vector4D@Transform)|Transforms a Vector2 by the given Matrix.|
|[static Transform(Vector3D, MatrixD)](VRageMath.Vector4D@Transform)|Transforms a Vector3 by the given Matrix.|
|[static Transform(ref Vector3D, ref MatrixD, out Vector4D)](VRageMath.Vector4D@Transform)|Transforms a Vector3 by the given Matrix.|
|[static Transform(Vector4D, MatrixD)](VRageMath.Vector4D@Transform)|Transforms a Vector4 by the specified Matrix.|
|[static Transform(ref Vector4D, ref MatrixD, out Vector4D)](VRageMath.Vector4D@Transform)|Transforms a Vector4 by the given Matrix.|
|[static Transform(Vector2, Quaternion)](VRageMath.Vector4D@Transform)|Transforms a Vector2 by a specified Quaternion into a Vector4.|
|[static Transform(ref Vector2, ref Quaternion, out Vector4D)](VRageMath.Vector4D@Transform)|Transforms a Vector2 by a specified Quaternion into a Vector4.|
|[static Transform(Vector3D, Quaternion)](VRageMath.Vector4D@Transform)|Transforms a Vector3 by a specified Quaternion into a Vector4.|
|[static Transform(ref Vector3D, ref Quaternion, out Vector4D)](VRageMath.Vector4D@Transform)|Transforms a Vector3 by a specified Quaternion into a Vector4.|
|[static Transform(Vector4D, Quaternion)](VRageMath.Vector4D@Transform)|Transforms a Vector4 by a specified Quaternion.|
|[static Transform(ref Vector4D, ref Quaternion, out Vector4D)](VRageMath.Vector4D@Transform)|Transforms a Vector4 by a specified Quaternion.|
|[static Transform(Vector4D[], ref MatrixD, Vector4D[])](VRageMath.Vector4D@Transform)|Transforms an array of Vector4s by a specified Matrix.|
|[static Transform(Vector4D[], int, ref MatrixD, Vector4D[], int, int)](VRageMath.Vector4D@Transform)|Transforms a specified range in an array of Vector4s by a specified Matrix into a specified range in a destination array.|
|[static Transform(Vector4D[], ref Quaternion, Vector4D[])](VRageMath.Vector4D@Transform)|Transforms an array of Vector4s by a specified Quaternion.|
|[static Transform(Vector4D[], int, ref Quaternion, Vector4D[], int, int)](VRageMath.Vector4D@Transform)|Transforms a specified range in an array of Vector4s by a specified Quaternion into a specified range in a destination array.|
|[static UnpackOrthoMatrix(ref Vector4D)](VRageMath.Vector4D@UnpackOrthoMatrix)||
|[Equals(Vector4)](VRageMath.Vector4D@Equals)|Determines whether the specified Object is equal to the Vector4.|
|[Equals(object)](VRageMath.Vector4D@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetHashCode()](VRageMath.Vector4D@GetHashCode)|Gets the hash code of this object.|
|[Length()](VRageMath.Vector4D@Length)|Calculates the length of the vector.|
|[LengthSquared()](VRageMath.Vector4D@LengthSquared)|Calculates the length of the vector squared.|
|[Normalize()](VRageMath.Vector4D@Normalize)|Turns the current vector into a unit vector.|
|[ToString()](VRageMath.Vector4D@ToString)|Retrieves a string representation of the current object.|

**Implements:**  
* [IEquatable<Vector4>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

