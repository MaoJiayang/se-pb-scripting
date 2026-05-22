**Assembly:** VRage.Math.dll

```csharp
public struct Quaternion: IEquatable<Quaternion>
```

Defines a four-dimensional vector (x,y,z,w), which is used to efficiently rotate an object about the (x, y, z) vector by the angle theta, where w = cos(theta/2).

## Fields

|Member|Description|
|---|---|
|[static Identity](VRageMath.Quaternion@Identity)||
|[static Zero](VRageMath.Quaternion@Zero)||
|[W](VRageMath.Quaternion@W)|Specifies the rotation component of the quaternion.|
|[X](VRageMath.Quaternion@X)|Specifies the x-value of the vector component of the quaternion.|
|[Y](VRageMath.Quaternion@Y)|Specifies the y-value of the vector component of the quaternion.|
|[Z](VRageMath.Quaternion@Z)|Specifies the z-value of the vector component of the quaternion.|

## Properties

|Member|Description|
|---|---|
|[Forward](VRageMath.Quaternion@Forward)||
|[Right](VRageMath.Quaternion@Right)||
|[Up](VRageMath.Quaternion@Up)||

## Constructors

|Member|Description|
|---|---|
|[Quaternion(float, float, float, float)](VRageMath.Quaternion@.ctor)||
|[Quaternion(Vector3, float)](VRageMath.Quaternion@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(Quaternion, Quaternion)](VRageMath.Quaternion@Add)|Adds two Quaternions.|
|[static Add(ref Quaternion, ref Quaternion, out Quaternion)](VRageMath.Quaternion@Add)|Adds two Quaternions.|
|[static Concatenate(Quaternion, Quaternion)](VRageMath.Quaternion@Concatenate)|Concatenates two Quaternions; the result represents the value1 rotation followed by the value2 rotation.|
|[static Concatenate(ref Quaternion, ref Quaternion, out Quaternion)](VRageMath.Quaternion@Concatenate)|Concatenates two Quaternions; the result represents the value1 rotation followed by the value2 rotation.|
|[static Conjugate(Quaternion)](VRageMath.Quaternion@Conjugate)|Returns the conjugate of a specified Quaternion.|
|[static Conjugate(ref Quaternion, out Quaternion)](VRageMath.Quaternion@Conjugate)|Returns the conjugate of a specified Quaternion.|
|[static CreateFromAxisAngle(Vector3, float)](VRageMath.Quaternion@CreateFromAxisAngle)|Creates a Quaternion from a vector and an angle to rotate about the vector.|
|[static CreateFromAxisAngle(ref Vector3, float, out Quaternion)](VRageMath.Quaternion@CreateFromAxisAngle)|Creates a Quaternion from a vector and an angle to rotate about the vector.|
|[static CreateFromForwardUp(Vector3, Vector3)](VRageMath.Quaternion@CreateFromForwardUp)|Works for normalized vectors only|
|[static CreateFromRotationMatrix(ref MatrixD)](VRageMath.Quaternion@CreateFromRotationMatrix)||
|[static CreateFromRotationMatrix(Matrix)](VRageMath.Quaternion@CreateFromRotationMatrix)|Creates a Quaternion from a rotation Matrix.|
|[static CreateFromRotationMatrix(ref MatrixD, out Quaternion)](VRageMath.Quaternion@CreateFromRotationMatrix)||
|[static CreateFromRotationMatrix(ref Matrix, out Quaternion)](VRageMath.Quaternion@CreateFromRotationMatrix)|Creates a Quaternion from a rotation Matrix.|
|[static CreateFromRotationMatrix(ref Matrix3x3, out Quaternion)](VRageMath.Quaternion@CreateFromRotationMatrix)|Creates a Quaternion from a rotation Matrix.|
|[static CreateFromTwoVectors(ref Vector3, ref Vector3, out Quaternion)](VRageMath.Quaternion@CreateFromTwoVectors)||
|[static CreateFromTwoVectors(Vector3, Vector3)](VRageMath.Quaternion@CreateFromTwoVectors)||
|[static CreateFromYawPitchRoll(float, float, float)](VRageMath.Quaternion@CreateFromYawPitchRoll)|Creates a new Quaternion from specified yaw, pitch, and roll angles.|
|[static CreateFromYawPitchRoll(float, float, float, out Quaternion)](VRageMath.Quaternion@CreateFromYawPitchRoll)|Creates a new Quaternion from specified yaw, pitch, and roll angles.|
|[static Divide(Quaternion, Quaternion)](VRageMath.Quaternion@Divide)|Divides a Quaternion by another Quaternion.|
|[static Divide(ref Quaternion, ref Quaternion, out Quaternion)](VRageMath.Quaternion@Divide)|Divides a Quaternion by another Quaternion.|
|[static Dot(Quaternion, Quaternion)](VRageMath.Quaternion@Dot)|Calculates the dot product of two Quaternions.|
|[static Dot(ref Quaternion, ref Quaternion, out float)](VRageMath.Quaternion@Dot)|Calculates the dot product of two Quaternions.|
|[static FromVector4(Vector4)](VRageMath.Quaternion@FromVector4)||
|[static GetForward(ref Quaternion, out Vector3)](VRageMath.Quaternion@GetForward)|Gets forward vector (0,0,-1) transformed by quaternion.|
|[static GetRight(ref Quaternion, out Vector3)](VRageMath.Quaternion@GetRight)|Gets right vector (1,0,0) transformed by quaternion.|
|[static GetUp(ref Quaternion, out Vector3)](VRageMath.Quaternion@GetUp)|Gets up vector (0,1,0) transformed by quaternion.|
|[static Inverse(Quaternion)](VRageMath.Quaternion@Inverse)|Returns the inverse of a Quaternion.|
|[static Inverse(ref Quaternion, out Quaternion)](VRageMath.Quaternion@Inverse)|Returns the inverse of a Quaternion.|
|[static IsZero(Quaternion)](VRageMath.Quaternion@IsZero)||
|[static IsZero(Quaternion, float)](VRageMath.Quaternion@IsZero)||
|[static Lerp(Quaternion, Quaternion, float)](VRageMath.Quaternion@Lerp)|Linearly interpolates between two quaternions.|
|[static Lerp(ref Quaternion, ref Quaternion, float, out Quaternion)](VRageMath.Quaternion@Lerp)|Linearly interpolates between two quaternions.|
|[static Multiply(Quaternion, Quaternion)](VRageMath.Quaternion@Multiply)|Multiplies two quaternions.|
|[static Multiply(ref Quaternion, ref Quaternion, out Quaternion)](VRageMath.Quaternion@Multiply)|Multiplies two quaternions.|
|[static Multiply(Quaternion, float)](VRageMath.Quaternion@Multiply)|Multiplies a quaternion by a scalar value.|
|[static Multiply(ref Quaternion, float, out Quaternion)](VRageMath.Quaternion@Multiply)|Multiplies a quaternion by a scalar value.|
|[static Negate(Quaternion)](VRageMath.Quaternion@Negate)|Flips the sign of each component of the quaternion.|
|[static Negate(ref Quaternion, out Quaternion)](VRageMath.Quaternion@Negate)|Flips the sign of each component of the quaternion.|
|[static Normalize(Quaternion)](VRageMath.Quaternion@Normalize)|Divides each component of the quaternion by the length of the quaternion.|
|[static Normalize(ref Quaternion, out Quaternion)](VRageMath.Quaternion@Normalize)|Divides each component of the quaternion by the length of the quaternion.|
|[static Slerp(Quaternion, Quaternion, float)](VRageMath.Quaternion@Slerp)|Interpolates between two quaternions, using spherical linear interpolation.|
|[static Slerp(ref Quaternion, ref Quaternion, float, out Quaternion)](VRageMath.Quaternion@Slerp)|Interpolates between two quaternions, using spherical linear interpolation.|
|[static Subtract(Quaternion, Quaternion)](VRageMath.Quaternion@Subtract)|Subtracts a quaternion from another quaternion.|
|[static Subtract(ref Quaternion, ref Quaternion, out Quaternion)](VRageMath.Quaternion@Subtract)|Subtracts a quaternion from another quaternion.|
|[Conjugate()](VRageMath.Quaternion@Conjugate)|Transforms this Quaternion into its conjugate.|
|[Equals(Quaternion)](VRageMath.Quaternion@Equals)|Determines whether the specified Object is equal to the Quaternion.|
|[Equals(Quaternion, float)](VRageMath.Quaternion@Equals)||
|[Equals(object)](VRageMath.Quaternion@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[FindLargestIndex()](VRageMath.Quaternion@FindLargestIndex)||
|[GetAxisAngle(out Vector3, out float)](VRageMath.Quaternion@GetAxisAngle)||
|[GetComponent(int)](VRageMath.Quaternion@GetComponent)||
|[GetHashCode()](VRageMath.Quaternion@GetHashCode)|Get the hash code of this object.|
|[Length()](VRageMath.Quaternion@Length)|Calculates the length of a Quaternion.|
|[LengthSquared()](VRageMath.Quaternion@LengthSquared)|Calculates the length squared of a Quaternion.|
|[Normalize()](VRageMath.Quaternion@Normalize)|Divides each component of the quaternion by the length of the quaternion.|
|[SetComponent(int, float)](VRageMath.Quaternion@SetComponent)||
|[ToString()](VRageMath.Quaternion@ToString)|Retireves a string representation of the current object.|
|[ToString(string)](VRageMath.Quaternion@ToString)||
|[ToStringAxisAngle(string)](VRageMath.Quaternion@ToStringAxisAngle)||
|[ToVector4()](VRageMath.Quaternion@ToVector4)||

**Implements:**  
* [IEquatable<Quaternion>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

