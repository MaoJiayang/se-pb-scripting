**Assembly:** VRage.Math.dll

```csharp
public struct Vector4: IEquatable<Vector4>
```

Defines a vector with four components.

## Fields

|Member|Description|
|---|---|
|[static One](VRageMath.Vector4@One)||
|[static UnitW](VRageMath.Vector4@UnitW)||
|[static UnitX](VRageMath.Vector4@UnitX)||
|[static UnitY](VRageMath.Vector4@UnitY)||
|[static UnitZ](VRageMath.Vector4@UnitZ)||
|[static Zero](VRageMath.Vector4@Zero)||
|[W](VRageMath.Vector4@W)|Gets or sets the w-component of the vector.|
|[X](VRageMath.Vector4@X)|Gets or sets the x-component of the vector.|
|[Y](VRageMath.Vector4@Y)|Gets or sets the y-component of the vector.|
|[Z](VRageMath.Vector4@Z)|Gets or sets the z-component of the vector.|

## Properties

|Member|Description|
|---|---|
|[Item](VRageMath.Vector4@Item)||

## Constructors

|Member|Description|
|---|---|
|[Vector4(float, float, float, float)](VRageMath.Vector4@.ctor)||
|[Vector4(Vector2, float, float)](VRageMath.Vector4@.ctor)||
|[Vector4(Vector3, float)](VRageMath.Vector4@.ctor)||
|[Vector4(float)](VRageMath.Vector4@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(Vector4, Vector4)](VRageMath.Vector4@Add)|Adds two vectors.|
|[static Add(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Add)|Adds two vectors.|
|[static Barycentric(Vector4, Vector4, Vector4, float, float)](VRageMath.Vector4@Barycentric)|Returns a Vector4 containing the 4D Cartesian coordinates of a point specified in barycentric (areal) coordinates relative to a 4D triangle.|
|[static Barycentric(ref Vector4, ref Vector4, ref Vector4, float, float, out Vector4)](VRageMath.Vector4@Barycentric)|Returns a Vector4 containing the 4D Cartesian coordinates of a point specified in Barycentric (areal) coordinates relative to a 4D triangle.|
|[static CatmullRom(Vector4, Vector4, Vector4, Vector4, float)](VRageMath.Vector4@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CatmullRom(ref Vector4, ref Vector4, ref Vector4, ref Vector4, float, out Vector4)](VRageMath.Vector4@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static Clamp(Vector4, Vector4, Vector4)](VRageMath.Vector4@Clamp)|Restricts a value to be within a specified range.|
|[static Clamp(ref Vector4, ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Clamp)|Restricts a value to be within a specified range.|
|[static Distance(Vector4, Vector4)](VRageMath.Vector4@Distance)|Calculates the distance between two vectors.|
|[static Distance(ref Vector4, ref Vector4, out float)](VRageMath.Vector4@Distance)|Calculates the distance between two vectors.|
|[static DistanceSquared(Vector4, Vector4)](VRageMath.Vector4@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static DistanceSquared(ref Vector4, ref Vector4, out float)](VRageMath.Vector4@DistanceSquared)|Calculates the distance between two vectors squared.|
|[static Divide(Vector4, Vector4)](VRageMath.Vector4@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Divide)|Divides the components of a vector by the components of another vector.|
|[static Divide(Vector4, float)](VRageMath.Vector4@Divide)|Divides a vector by a scalar value.|
|[static Divide(ref Vector4, float, out Vector4)](VRageMath.Vector4@Divide)|Divides a vector by a scalar value.|
|[static Dot(Vector4, Vector4)](VRageMath.Vector4@Dot)|Calculates the dot product of two vectors.|
|[static Dot(ref Vector4, ref Vector4, out float)](VRageMath.Vector4@Dot)|Calculates the dot product of two vectors.|
|[static Hermite(Vector4, Vector4, Vector4, Vector4, float)](VRageMath.Vector4@Hermite)|Performs a Hermite spline interpolation.|
|[static Hermite(ref Vector4, ref Vector4, ref Vector4, ref Vector4, float, out Vector4)](VRageMath.Vector4@Hermite)|Performs a Hermite spline interpolation.|
|[static Lerp(Vector4, Vector4, float)](VRageMath.Vector4@Lerp)|Performs a linear interpolation between two vectors.|
|[static Lerp(ref Vector4, ref Vector4, float, out Vector4)](VRageMath.Vector4@Lerp)|Performs a linear interpolation between two vectors.|
|[static Max(Vector4, Vector4)](VRageMath.Vector4@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Max(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Max)|Returns a vector that contains the highest value from each matching pair of components.|
|[static Min(Vector4, Vector4)](VRageMath.Vector4@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Min(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Min)|Returns a vector that contains the lowest value from each matching pair of components.|
|[static Multiply(Vector4, Vector4)](VRageMath.Vector4@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Multiply)|Multiplies the components of two vectors by each other.|
|[static Multiply(Vector4, float)](VRageMath.Vector4@Multiply)|Multiplies a vector by a scalar.|
|[static Multiply(ref Vector4, float, out Vector4)](VRageMath.Vector4@Multiply)|Multiplies a vector by a scalar value.|
|[static Negate(Vector4)](VRageMath.Vector4@Negate)|Returns a vector pointing in the opposite direction.|
|[static Negate(ref Vector4, out Vector4)](VRageMath.Vector4@Negate)|Returns a vector pointing in the opposite direction.|
|[static Normalize(Vector4)](VRageMath.Vector4@Normalize)|Creates a unit vector from the specified vector.|
|[static Normalize(ref Vector4, out Vector4)](VRageMath.Vector4@Normalize)|Returns a normalized version of the specified vector.|
|[static PackOrthoMatrix(Vector3, Vector3, Vector3)](VRageMath.Vector4@PackOrthoMatrix)||
|[static PackOrthoMatrix(ref Matrix)](VRageMath.Vector4@PackOrthoMatrix)||
|[static SmoothStep(Vector4, Vector4, float)](VRageMath.Vector4@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(ref Vector4, ref Vector4, float, out Vector4)](VRageMath.Vector4@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static Subtract(Vector4, Vector4)](VRageMath.Vector4@Subtract)|Subtracts a vector from a vector.|
|[static Subtract(ref Vector4, ref Vector4, out Vector4)](VRageMath.Vector4@Subtract)|Subtracts a vector from a vector.|
|[static Transform(Vector2, Matrix)](VRageMath.Vector4@Transform)|Transforms a Vector2 by the given Matrix.|
|[static Transform(ref Vector2, ref Matrix, out Vector4)](VRageMath.Vector4@Transform)|Transforms a Vector2 by the given Matrix.|
|[static Transform(Vector3, Matrix)](VRageMath.Vector4@Transform)|Transforms a Vector3 by the given Matrix.|
|[static Transform(ref Vector3, ref Matrix, out Vector4)](VRageMath.Vector4@Transform)|Transforms a Vector3 by the given Matrix.|
|[static Transform(Vector4, Matrix)](VRageMath.Vector4@Transform)|Transforms a Vector4 by the specified Matrix.|
|[static Transform(ref Vector4, ref Matrix, out Vector4)](VRageMath.Vector4@Transform)|Transforms a Vector4 by the given Matrix.|
|[static Transform(Vector2, Quaternion)](VRageMath.Vector4@Transform)|Transforms a Vector2 by a specified Quaternion into a Vector4.|
|[static Transform(ref Vector2, ref Quaternion, out Vector4)](VRageMath.Vector4@Transform)|Transforms a Vector2 by a specified Quaternion into a Vector4.|
|[static Transform(Vector3, Quaternion)](VRageMath.Vector4@Transform)|Transforms a Vector3 by a specified Quaternion into a Vector4.|
|[static Transform(ref Vector3, ref Quaternion, out Vector4)](VRageMath.Vector4@Transform)|Transforms a Vector3 by a specified Quaternion into a Vector4.|
|[static Transform(Vector4, Quaternion)](VRageMath.Vector4@Transform)|Transforms a Vector4 by a specified Quaternion.|
|[static Transform(ref Vector4, ref Quaternion, out Vector4)](VRageMath.Vector4@Transform)|Transforms a Vector4 by a specified Quaternion.|
|[static Transform(Vector4[], ref Matrix, Vector4[])](VRageMath.Vector4@Transform)|Transforms an array of Vector4s by a specified Matrix.|
|[static Transform(Vector4[], int, ref Matrix, Vector4[], int, int)](VRageMath.Vector4@Transform)|Transforms a specified range in an array of Vector4s by a specified Matrix into a specified range in a destination array.|
|[static Transform(Vector4[], ref Quaternion, Vector4[])](VRageMath.Vector4@Transform)|Transforms an array of Vector4s by a specified Quaternion.|
|[static Transform(Vector4[], int, ref Quaternion, Vector4[], int, int)](VRageMath.Vector4@Transform)|Transforms a specified range in an array of Vector4s by a specified Quaternion into a specified range in a destination array.|
|[static UnpackOrthoMatrix(ref Vector4)](VRageMath.Vector4@UnpackOrthoMatrix)||
|[static UnpackOrthoMatrix(ref Vector4, out Matrix)](VRageMath.Vector4@UnpackOrthoMatrix)||
|[Equals(Vector4)](VRageMath.Vector4@Equals)|Determines whether the specified Object is equal to the Vector4.|
|[Equals(object)](VRageMath.Vector4@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetHashCode()](VRageMath.Vector4@GetHashCode)|Gets the hash code of this object.|
|[Length()](VRageMath.Vector4@Length)|Calculates the length of the vector.|
|[LengthSquared()](VRageMath.Vector4@LengthSquared)|Calculates the length of the vector squared.|
|[Normalize()](VRageMath.Vector4@Normalize)|Turns the current vector into a unit vector.|
|[ToString()](VRageMath.Vector4@ToString)|Retrieves a string representation of the current object.|

**Implements:**  
* [IEquatable<Vector4>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

