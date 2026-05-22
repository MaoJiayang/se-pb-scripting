**Assembly:** VRage.Math.dll

```csharp
public struct Matrix3x3: IEquatable<Matrix3x3>
```

Defines a matrix.

## Fields

|Member|Description|
|---|---|
|[static Identity](VRageMath.Matrix3x3@Identity)||
|[static Zero](VRageMath.Matrix3x3@Zero)||
|[M11](VRageMath.Matrix3x3@M11)|Value at row 1 column 1 of the matrix.|
|[M12](VRageMath.Matrix3x3@M12)|Value at row 1 column 2 of the matrix.|
|[M13](VRageMath.Matrix3x3@M13)|Value at row 1 column 3 of the matrix.|
|[M21](VRageMath.Matrix3x3@M21)|Value at row 2 column 1 of the matrix.|
|[M22](VRageMath.Matrix3x3@M22)|Value at row 2 column 2 of the matrix.|
|[M23](VRageMath.Matrix3x3@M23)|Value at row 2 column 3 of the matrix.|
|[M31](VRageMath.Matrix3x3@M31)|Value at row 3 column 1 of the matrix.|
|[M32](VRageMath.Matrix3x3@M32)|Value at row 3 column 2 of the matrix.|
|[M33](VRageMath.Matrix3x3@M33)|Value at row 3 column 3 of the matrix.|

## Properties

|Member|Description|
|---|---|
|[Backward](VRageMath.Matrix3x3@Backward)|Gets and sets the backward vector of the Matrix3x3.|
|[Col0](VRageMath.Matrix3x3@Col0)||
|[Col1](VRageMath.Matrix3x3@Col1)||
|[Col2](VRageMath.Matrix3x3@Col2)||
|[Down](VRageMath.Matrix3x3@Down)|Gets and sets the down vector of the Matrix3x3.|
|[Forward](VRageMath.Matrix3x3@Forward)|Gets and sets the forward vector of the Matrix3x3.|
|[Item](VRageMath.Matrix3x3@Item)||
|[Left](VRageMath.Matrix3x3@Left)|Gets and sets the left vector of the Matrix3x3.|
|[Right](VRageMath.Matrix3x3@Right)|Gets and sets the right vector of the Matrix3x3.|
|[Scale](VRageMath.Matrix3x3@Scale)||
|[Up](VRageMath.Matrix3x3@Up)|Gets and sets the up vector of the Matrix3x3.|

## Constructors

|Member|Description|
|---|---|
|[Matrix3x3(float, float, float, float, float, float, float, float, float)](VRageMath.Matrix3x3@.ctor)||
|[Matrix3x3(Matrix3x3)](VRageMath.Matrix3x3@.ctor)||
|[Matrix3x3(MatrixD)](VRageMath.Matrix3x3@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(ref Matrix3x3, ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Add)|Adds a matrix to another matrix.|
|[static AlignRotationToAxes(ref Matrix3x3, ref Matrix3x3)](VRageMath.Matrix3x3@AlignRotationToAxes)||
|[static CreateFromAxisAngle(Vector3, float)](VRageMath.Matrix3x3@CreateFromAxisAngle)|Creates a new Matrix3x3 that rotates around an arbitrary vector.|
|[static CreateFromAxisAngle(ref Vector3, float, out Matrix3x3)](VRageMath.Matrix3x3@CreateFromAxisAngle)|Creates a new Matrix3x3 that rotates around an arbitrary vector.|
|[static CreateFromDir(Vector3)](VRageMath.Matrix3x3@CreateFromDir)||
|[static CreateFromDir(Vector3, Vector3)](VRageMath.Matrix3x3@CreateFromDir)||
|[static CreateFromQuaternion(Quaternion)](VRageMath.Matrix3x3@CreateFromQuaternion)|Creates a rotation Matrix3x3 from a Quaternion.|
|[static CreateFromQuaternion(ref Quaternion, out Matrix3x3)](VRageMath.Matrix3x3@CreateFromQuaternion)|Creates a rotation Matrix3x3 from a Quaternion.|
|[static CreateFromYawPitchRoll(float, float, float)](VRageMath.Matrix3x3@CreateFromYawPitchRoll)|Creates a new rotation matrix from a specified yaw, pitch, and roll.|
|[static CreateFromYawPitchRoll(float, float, float, out Matrix3x3)](VRageMath.Matrix3x3@CreateFromYawPitchRoll)|Fills in a rotation matrix from a specified yaw, pitch, and roll.|
|[static CreateRotationFromTwoVectors(ref Vector3, ref Vector3, out Matrix3x3)](VRageMath.Matrix3x3@CreateRotationFromTwoVectors)||
|[static CreateRotationX(float)](VRageMath.Matrix3x3@CreateRotationX)|Returns a matrix that can be used to rotate a set of vertices around the x-axis.|
|[static CreateRotationX(float, out Matrix3x3)](VRageMath.Matrix3x3@CreateRotationX)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the x-axis.|
|[static CreateRotationY(float)](VRageMath.Matrix3x3@CreateRotationY)|Returns a matrix that can be used to rotate a set of vertices around the y-axis.|
|[static CreateRotationY(float, out Matrix3x3)](VRageMath.Matrix3x3@CreateRotationY)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the y-axis.|
|[static CreateRotationZ(float)](VRageMath.Matrix3x3@CreateRotationZ)|Returns a matrix that can be used to rotate a set of vertices around the z-axis.|
|[static CreateRotationZ(float, out Matrix3x3)](VRageMath.Matrix3x3@CreateRotationZ)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the z-axis.|
|[static CreateScale(float, float, float)](VRageMath.Matrix3x3@CreateScale)|Creates a scaling Matrix3x3.|
|[static CreateScale(float, float, float, out Matrix3x3)](VRageMath.Matrix3x3@CreateScale)|Creates a scaling Matrix3x3.|
|[static CreateScale(Vector3)](VRageMath.Matrix3x3@CreateScale)|Creates a scaling Matrix3x3.|
|[static CreateScale(ref Vector3, out Matrix3x3)](VRageMath.Matrix3x3@CreateScale)|Creates a scaling Matrix3x3.|
|[static CreateScale(float)](VRageMath.Matrix3x3@CreateScale)|Creates a scaling Matrix3x3.|
|[static CreateScale(float, out Matrix3x3)](VRageMath.Matrix3x3@CreateScale)|Creates a scaling Matrix3x3.|
|[static CreateWorld(ref Vector3, ref Vector3)](VRageMath.Matrix3x3@CreateWorld)|Creates a world matrix with the specified parameters.|
|[static Divide(ref Matrix3x3, ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Divide)|Divides the components of a matrix by the corresponding components of another matrix.|
|[static Divide(ref Matrix3x3, float, out Matrix3x3)](VRageMath.Matrix3x3@Divide)|Divides the components of a matrix by a scalar.|
|[static GetEulerAnglesXYZ(ref Matrix3x3, out Vector3)](VRageMath.Matrix3x3@GetEulerAnglesXYZ)||
|[static Invert(ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Invert)|Calculates the inverse of a matrix.|
|[static Lerp(ref Matrix3x3, ref Matrix3x3, float, out Matrix3x3)](VRageMath.Matrix3x3@Lerp)|Linearly interpolates between the corresponding values of two matrices.|
|[static Multiply(ref Matrix3x3, ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(ref Matrix3x3, float, out Matrix3x3)](VRageMath.Matrix3x3@Multiply)|Multiplies a matrix by a scalar value.|
|[static Negate(ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Negate)|Negates individual elements of a matrix.|
|[static Normalize(Matrix3x3)](VRageMath.Matrix3x3@Normalize)||
|[static Orthogonalize(Matrix3x3)](VRageMath.Matrix3x3@Orthogonalize)||
|[static Rescale(ref Matrix3x3, float)](VRageMath.Matrix3x3@Rescale)|Same result as Matrix3x3.CreateScale(scale) * matrix, but much faster|
|[static Rescale(ref Matrix3x3, ref Vector3)](VRageMath.Matrix3x3@Rescale)|Same result as Matrix3x3.CreateScale(scale) * matrix, but much faster|
|[static Rescale(Matrix3x3, float)](VRageMath.Matrix3x3@Rescale)||
|[static Rescale(Matrix3x3, Vector3)](VRageMath.Matrix3x3@Rescale)||
|[static Round(ref Matrix3x3)](VRageMath.Matrix3x3@Round)||
|[static Slerp(ref Matrix3x3, ref Matrix3x3, float, out Matrix3x3)](VRageMath.Matrix3x3@Slerp)|Performs spherical linear interpolation of position and rotation.|
|[static SlerpScale(ref Matrix3x3, ref Matrix3x3, float, out Matrix3x3)](VRageMath.Matrix3x3@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static Subtract(ref Matrix3x3, ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Subtract)|Subtracts matrices.|
|[static Transform(ref Matrix3x3, ref Quaternion, out Matrix3x3)](VRageMath.Matrix3x3@Transform)|Transforms a Matrix3x3 by applying a Quaternion rotation.|
|[static Transpose(ref Matrix3x3, out Matrix3x3)](VRageMath.Matrix3x3@Transpose)|Transposes the rows and columns of a matrix.|
|[AssertIsValid()](VRageMath.Matrix3x3@AssertIsValid)||
|[Determinant()](VRageMath.Matrix3x3@Determinant)||
|[Equals(Matrix3x3)](VRageMath.Matrix3x3@Equals)|Determines whether the specified Object is equal to the Matrix3x3.|
|[Equals(object)](VRageMath.Matrix3x3@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[EqualsFast(ref Matrix3x3, float)](VRageMath.Matrix3x3@EqualsFast)|Compares just position, forward and up|
|[GetClosestDirection(Vector3)](VRageMath.Matrix3x3@GetClosestDirection)||
|[GetClosestDirection(ref Vector3)](VRageMath.Matrix3x3@GetClosestDirection)||
|[GetDirectionVector(Direction)](VRageMath.Matrix3x3@GetDirectionVector)||
|[GetHashCode()](VRageMath.Matrix3x3@GetHashCode)|Gets the hash code of this object.|
|[GetOrientation()](VRageMath.Matrix3x3@GetOrientation)|Gets the orientation.|
|[GetRow(int)](VRageMath.Matrix3x3@GetRow)||
|[IsMirrored()](VRageMath.Matrix3x3@IsMirrored)||
|[IsNan()](VRageMath.Matrix3x3@IsNan)||
|[IsOrthogonal()](VRageMath.Matrix3x3@IsOrthogonal)||
|[IsRotation()](VRageMath.Matrix3x3@IsRotation)||
|[IsValid()](VRageMath.Matrix3x3@IsValid)||
|[SetDirectionVector(Direction, Vector3)](VRageMath.Matrix3x3@SetDirectionVector)||
|[SetRow(int, Vector3)](VRageMath.Matrix3x3@SetRow)||
|[ToString()](VRageMath.Matrix3x3@ToString)|Retrieves a string representation of the current object.|
|[Transpose()](VRageMath.Matrix3x3@Transpose)||

**Implements:**  
* [IEquatable<Matrix3x3>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

