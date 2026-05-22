**Assembly:** VRage.Math.dll

```csharp
public struct QuaternionD
```

Defines a four-dimensional vector (x,y,z,w), which is used to efficiently rotate an object about the (x, y, z) vector by the angle theta, where w = cos(theta/2). Uses double precision floating point numbers for calculation and storage

## Fields

|Member|Description|
|---|---|
|[static Identity](VRageMath.QuaternionD@Identity)||
|[W](VRageMath.QuaternionD@W)|Specifies the rotation component of the quaternion.|
|[X](VRageMath.QuaternionD@X)|Specifies the x-value of the vector component of the quaternion.|
|[Y](VRageMath.QuaternionD@Y)|Specifies the y-value of the vector component of the quaternion.|
|[Z](VRageMath.QuaternionD@Z)|Specifies the z-value of the vector component of the quaternion.|

## Constructors

|Member|Description|
|---|---|
|[QuaternionD(double, double, double, double)](VRageMath.QuaternionD@.ctor)||
|[QuaternionD(Vector3D, double)](VRageMath.QuaternionD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(QuaternionD, QuaternionD)](VRageMath.QuaternionD@Add)|Adds two Quaternions.|
|[static Add(ref QuaternionD, ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Add)|Adds two Quaternions.|
|[static Concatenate(QuaternionD, QuaternionD)](VRageMath.QuaternionD@Concatenate)|Concatenates two Quaternions; the result represents the value1 rotation followed by the value2 rotation.|
|[static Concatenate(ref QuaternionD, ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Concatenate)|Concatenates two Quaternions; the result represents the value1 rotation followed by the value2 rotation.|
|[static Conjugate(QuaternionD)](VRageMath.QuaternionD@Conjugate)|Returns the conjugate of a specified QuaternionD.|
|[static Conjugate(ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Conjugate)|Returns the conjugate of a specified QuaternionD.|
|[static CreateFromAxisAngle(Vector3D, double)](VRageMath.QuaternionD@CreateFromAxisAngle)|Creates a QuaternionD from a vector and an angle to rotate about the vector.|
|[static CreateFromAxisAngle(ref Vector3D, double, out QuaternionD)](VRageMath.QuaternionD@CreateFromAxisAngle)|Creates a QuaternionD from a vector and an angle to rotate about the vector.|
|[static CreateFromForwardUp(Vector3D, Vector3D)](VRageMath.QuaternionD@CreateFromForwardUp)|Works for normalized vectors only|
|[static CreateFromRotationMatrix(MatrixD)](VRageMath.QuaternionD@CreateFromRotationMatrix)|Creates a QuaternionD from a rotation MatrixD.|
|[static CreateFromRotationMatrix(ref MatrixD, out QuaternionD)](VRageMath.QuaternionD@CreateFromRotationMatrix)|Creates a QuaternionD from a rotation MatrixD.|
|[static CreateFromTwoVectors(ref Vector3D, ref Vector3D, out QuaternionD)](VRageMath.QuaternionD@CreateFromTwoVectors)||
|[static CreateFromTwoVectors(Vector3D, Vector3D)](VRageMath.QuaternionD@CreateFromTwoVectors)||
|[static CreateFromYawPitchRoll(double, double, double)](VRageMath.QuaternionD@CreateFromYawPitchRoll)|Creates a new QuaternionD from specified yaw, pitch, and roll angles.|
|[static CreateFromYawPitchRoll(double, double, double, out QuaternionD)](VRageMath.QuaternionD@CreateFromYawPitchRoll)|Creates a new QuaternionD from specified yaw, pitch, and roll angles.|
|[static Divide(QuaternionD, QuaternionD)](VRageMath.QuaternionD@Divide)|Divides a QuaternionD by another QuaternionD.|
|[static Divide(ref QuaternionD, ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Divide)|Divides a QuaternionD by another QuaternionD.|
|[static Dot(QuaternionD, QuaternionD)](VRageMath.QuaternionD@Dot)|Calculates the dot product of two Quaternions.|
|[static Dot(ref QuaternionD, ref QuaternionD, out double)](VRageMath.QuaternionD@Dot)|Calculates the dot product of two Quaternions.|
|[static FromVector4(Vector4D)](VRageMath.QuaternionD@FromVector4)||
|[static Inverse(QuaternionD)](VRageMath.QuaternionD@Inverse)|Returns the inverse of a QuaternionD.|
|[static Inverse(ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Inverse)|Returns the inverse of a QuaternionD.|
|[static IsZero(QuaternionD)](VRageMath.QuaternionD@IsZero)||
|[static IsZero(QuaternionD, double)](VRageMath.QuaternionD@IsZero)||
|[static Lerp(QuaternionD, QuaternionD, double)](VRageMath.QuaternionD@Lerp)|Linearly interpolates between two quaternions.|
|[static Lerp(ref QuaternionD, ref QuaternionD, double, out QuaternionD)](VRageMath.QuaternionD@Lerp)|Linearly interpolates between two quaternions.|
|[static Multiply(QuaternionD, QuaternionD)](VRageMath.QuaternionD@Multiply)|Multiplies two quaternions.|
|[static Multiply(ref QuaternionD, ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Multiply)|Multiplies two quaternions.|
|[static Multiply(QuaternionD, double)](VRageMath.QuaternionD@Multiply)|Multiplies a quaternion by a scalar value.|
|[static Multiply(ref QuaternionD, double, out QuaternionD)](VRageMath.QuaternionD@Multiply)|Multiplies a quaternion by a scalar value.|
|[static Negate(QuaternionD)](VRageMath.QuaternionD@Negate)|Flips the sign of each component of the quaternion.|
|[static Negate(ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Negate)|Flips the sign of each component of the quaternion.|
|[static Normalize(QuaternionD)](VRageMath.QuaternionD@Normalize)|Divides each component of the quaternion by the length of the quaternion.|
|[static Normalize(ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Normalize)|Divides each component of the quaternion by the length of the quaternion.|
|[static Slerp(QuaternionD, QuaternionD, double)](VRageMath.QuaternionD@Slerp)|Interpolates between two quaternions, using spherical linear interpolation.|
|[static Slerp(ref QuaternionD, ref QuaternionD, double, out QuaternionD)](VRageMath.QuaternionD@Slerp)|Interpolates between two quaternions, using spherical linear interpolation.|
|[static Subtract(QuaternionD, QuaternionD)](VRageMath.QuaternionD@Subtract)|Subtracts a quaternion from another quaternion.|
|[static Subtract(ref QuaternionD, ref QuaternionD, out QuaternionD)](VRageMath.QuaternionD@Subtract)|Subtracts a quaternion from another quaternion.|
|[Conjugate()](VRageMath.QuaternionD@Conjugate)|Transforms this QuaternionD into its conjugate.|
|[Equals(QuaternionD)](VRageMath.QuaternionD@Equals)|Determines whether the specified Object is equal to the QuaternionD.|
|[Equals(object)](VRageMath.QuaternionD@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetAxisAngle(out Vector3D, out double)](VRageMath.QuaternionD@GetAxisAngle)||
|[GetHashCode()](VRageMath.QuaternionD@GetHashCode)|Get the hash code of this object.|
|[Length()](VRageMath.QuaternionD@Length)|Calculates the length of a QuaternionD.|
|[LengthSquared()](VRageMath.QuaternionD@LengthSquared)|Calculates the length squared of a QuaternionD.|
|[Normalize()](VRageMath.QuaternionD@Normalize)|Divides each component of the quaternion by the length of the quaternion.|
|[ToString()](VRageMath.QuaternionD@ToString)|Retireves a string representation of the current object.|
|[ToVector4()](VRageMath.QuaternionD@ToVector4)||

