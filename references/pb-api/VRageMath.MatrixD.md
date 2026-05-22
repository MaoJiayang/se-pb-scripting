**Assembly:** VRage.Math.dll

```csharp
public struct MatrixD: IEquatable<MatrixD>
```

Defines a matrix.

## Fields

|Member|Description|
|---|---|
|[static Identity](VRageMath.MatrixD@Identity)||
|[static Zero](VRageMath.MatrixD@Zero)||
|[M11](VRageMath.MatrixD@M11)|Value at row 1 column 1 of the matrix.|
|[M12](VRageMath.MatrixD@M12)|Value at row 1 column 2 of the matrix.|
|[M13](VRageMath.MatrixD@M13)|Value at row 1 column 3 of the matrix.|
|[M14](VRageMath.MatrixD@M14)|Value at row 1 column 4 of the matrix.|
|[M21](VRageMath.MatrixD@M21)|Value at row 2 column 1 of the matrix.|
|[M22](VRageMath.MatrixD@M22)|Value at row 2 column 2 of the matrix.|
|[M23](VRageMath.MatrixD@M23)|Value at row 2 column 3 of the matrix.|
|[M24](VRageMath.MatrixD@M24)|Value at row 2 column 4 of the matrix.|
|[M31](VRageMath.MatrixD@M31)|Value at row 3 column 1 of the matrix.|
|[M32](VRageMath.MatrixD@M32)|Value at row 3 column 2 of the matrix.|
|[M33](VRageMath.MatrixD@M33)|Value at row 3 column 3 of the matrix.|
|[M34](VRageMath.MatrixD@M34)|Value at row 3 column 4 of the matrix.|
|[M41](VRageMath.MatrixD@M41)|Value at row 4 column 1 of the matrix.|
|[M42](VRageMath.MatrixD@M42)|Value at row 4 column 2 of the matrix.|
|[M43](VRageMath.MatrixD@M43)|Value at row 4 column 3 of the matrix.|
|[M44](VRageMath.MatrixD@M44)|Value at row 4 column 4 of the matrix.|

## Properties

|Member|Description|
|---|---|
|[Backward](VRageMath.MatrixD@Backward)|Gets and sets the backward vector of the Matrix.|
|[Col0](VRageMath.MatrixD@Col0)||
|[Col1](VRageMath.MatrixD@Col1)||
|[Col2](VRageMath.MatrixD@Col2)||
|[Down](VRageMath.MatrixD@Down)|Gets and sets the down vector of the Matrix.|
|[Forward](VRageMath.MatrixD@Forward)|Gets and sets the forward vector of the Matrix.|
|[Item](VRageMath.MatrixD@Item)||
|[Left](VRageMath.MatrixD@Left)|Gets and sets the left vector of the Matrix.|
|[Right](VRageMath.MatrixD@Right)|Gets and sets the right vector of the Matrix.|
|[Rotation](VRageMath.MatrixD@Rotation)||
|[Scale](VRageMath.MatrixD@Scale)||
|[Translation](VRageMath.MatrixD@Translation)|Gets and sets the translation vector of the Matrix.|
|[Up](VRageMath.MatrixD@Up)|Gets and sets the up vector of the Matrix.|

## Constructors

|Member|Description|
|---|---|
|[MatrixD(double, double, double, double, double, double, double, double, double, double, double, double, double, double, double, double)](VRageMath.MatrixD@.ctor)||
|[MatrixD(double, double, double, double, double, double, double, double, double)](VRageMath.MatrixD@.ctor)||
|[MatrixD(Matrix)](VRageMath.MatrixD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(MatrixD, MatrixD)](VRageMath.MatrixD@Add)|Adds a matrix to another matrix.|
|[static Add(ref MatrixD, ref MatrixD, out MatrixD)](VRageMath.MatrixD@Add)|Adds a matrix to another matrix.|
|[static AlignRotationToAxes(ref MatrixD, ref MatrixD)](VRageMath.MatrixD@AlignRotationToAxes)||
|[static CreateBillboard(Vector3D, Vector3D, Vector3D, Vector3D?)](VRageMath.MatrixD@CreateBillboard)|Creates a spherical billboard that rotates around a specified object position.|
|[static CreateBillboard(ref Vector3D, ref Vector3D, ref Vector3D, Vector3D?, out MatrixD)](VRageMath.MatrixD@CreateBillboard)|Creates a spherical billboard that rotates around a specified object position.|
|[static CreateConstrainedBillboard(Vector3D, Vector3D, Vector3D, Vector3D?, Vector3D?)](VRageMath.MatrixD@CreateConstrainedBillboard)|Creates a cylindrical billboard that rotates around a specified axis.|
|[static CreateConstrainedBillboard(ref Vector3D, ref Vector3D, ref Vector3D, Vector3D?, Vector3D?, out MatrixD)](VRageMath.MatrixD@CreateConstrainedBillboard)|Creates a cylindrical billboard that rotates around a specified axis.|
|[static CreateFromAxisAngle(Vector3D, double)](VRageMath.MatrixD@CreateFromAxisAngle)|Creates a new Matrix that rotates around an arbitrary vector.|
|[static CreateFromAxisAngle(ref Vector3D, double, out MatrixD)](VRageMath.MatrixD@CreateFromAxisAngle)|Creates a new Matrix that rotates around an arbitrary vector.|
|[static CreateFromDir(Vector3D)](VRageMath.MatrixD@CreateFromDir)||
|[static CreateFromDir(Vector3D, Vector3D)](VRageMath.MatrixD@CreateFromDir)||
|[static CreateFromQuaternion(Quaternion)](VRageMath.MatrixD@CreateFromQuaternion)|Creates a rotation Matrix from a Quaternion.|
|[static CreateFromQuaternion(QuaternionD)](VRageMath.MatrixD@CreateFromQuaternion)||
|[static CreateFromQuaternion(ref Quaternion, out MatrixD)](VRageMath.MatrixD@CreateFromQuaternion)|Creates a rotation Matrix from a Quaternion.|
|[static CreateFromTransformScale(Quaternion, Vector3D, Vector3D)](VRageMath.MatrixD@CreateFromTransformScale)||
|[static CreateFromYawPitchRoll(double, double, double)](VRageMath.MatrixD@CreateFromYawPitchRoll)|Creates a new rotation matrix from a specified yaw, pitch, and roll.|
|[static CreateFromYawPitchRoll(double, double, double, out MatrixD)](VRageMath.MatrixD@CreateFromYawPitchRoll)|Fills in a rotation matrix from a specified yaw, pitch, and roll.|
|[static CreateLookAt(Vector3D, Vector3D, Vector3)](VRageMath.MatrixD@CreateLookAt)||
|[static CreateLookAt(Vector3D, Vector3D, Vector3D)](VRageMath.MatrixD@CreateLookAt)|Creates a view matrix.|
|[static CreateLookAt(ref Vector3D, ref Vector3D, ref Vector3D, out MatrixD)](VRageMath.MatrixD@CreateLookAt)|Creates a view matrix.|
|[static CreateLookAtInverse(Vector3D, Vector3D, Vector3D)](VRageMath.MatrixD@CreateLookAtInverse)||
|[static CreateOrthographic(double, double, double, double)](VRageMath.MatrixD@CreateOrthographic)|Builds an orthogonal projection matrix.|
|[static CreateOrthographic(double, double, double, double, out MatrixD)](VRageMath.MatrixD@CreateOrthographic)|Builds an orthogonal projection matrix.|
|[static CreateOrthographicOffCenter(double, double, double, double, double, double)](VRageMath.MatrixD@CreateOrthographicOffCenter)|Builds a customized, orthogonal projection matrix.|
|[static CreateOrthographicOffCenter(double, double, double, double, double, double, out MatrixD)](VRageMath.MatrixD@CreateOrthographicOffCenter)|Builds a customized, orthogonal projection matrix.|
|[static CreatePerspective(double, double, double, double)](VRageMath.MatrixD@CreatePerspective)|Builds a perspective projection matrix and returns the result by value.|
|[static CreatePerspective(double, double, double, double, out MatrixD)](VRageMath.MatrixD@CreatePerspective)|Builds a perspective projection matrix and returns the result by reference.|
|[static CreatePerspectiveFieldOfView(double, double, double, double)](VRageMath.MatrixD@CreatePerspectiveFieldOfView)|Builds a perspective projection matrix based on a field of view and returns by value.|
|[static CreatePerspectiveFieldOfView(double, double, double, double, out MatrixD)](VRageMath.MatrixD@CreatePerspectiveFieldOfView)|Builds a perspective projection matrix based on a field of view and returns by reference.|
|[static CreatePerspectiveOffCenter(double, double, double, double, double, double)](VRageMath.MatrixD@CreatePerspectiveOffCenter)|Builds a customized, perspective projection matrix.|
|[static CreatePerspectiveOffCenter(double, double, double, double, double, double, out MatrixD)](VRageMath.MatrixD@CreatePerspectiveOffCenter)|Builds a customized, perspective projection matrix.|
|[static CreateReflection(Plane)](VRageMath.MatrixD@CreateReflection)|Creates a Matrix that reflects the coordinate system about a specified Plane.|
|[static CreateReflection(ref Plane, out MatrixD)](VRageMath.MatrixD@CreateReflection)|Fills in an existing Matrix so that it reflects the coordinate system about a specified Plane.|
|[static CreateRotationX(double)](VRageMath.MatrixD@CreateRotationX)|Returns a matrix that can be used to rotate a set of vertices around the x-axis.|
|[static CreateRotationX(double, out MatrixD)](VRageMath.MatrixD@CreateRotationX)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the x-axis.|
|[static CreateRotationY(double)](VRageMath.MatrixD@CreateRotationY)|Returns a matrix that can be used to rotate a set of vertices around the y-axis.|
|[static CreateRotationY(double, out MatrixD)](VRageMath.MatrixD@CreateRotationY)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the y-axis.|
|[static CreateRotationZ(double)](VRageMath.MatrixD@CreateRotationZ)|Returns a matrix that can be used to rotate a set of vertices around the z-axis.|
|[static CreateRotationZ(double, out MatrixD)](VRageMath.MatrixD@CreateRotationZ)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the z-axis.|
|[static CreateScale(double, double, double)](VRageMath.MatrixD@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(double, double, double, out MatrixD)](VRageMath.MatrixD@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(Vector3D)](VRageMath.MatrixD@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(ref Vector3D, out MatrixD)](VRageMath.MatrixD@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(double)](VRageMath.MatrixD@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(double, out MatrixD)](VRageMath.MatrixD@CreateScale)|Creates a scaling Matrix.|
|[static CreateShadow(Vector3D, Plane)](VRageMath.MatrixD@CreateShadow)|Creates a Matrix that flattens geometry into a specified Plane as if casting a shadow from a specified light source.|
|[static CreateShadow(ref Vector3D, ref Plane, out MatrixD)](VRageMath.MatrixD@CreateShadow)|Fills in a Matrix to flatten geometry into a specified Plane as if casting a shadow from a specified light source.|
|[static CreateTranslation(Vector3D)](VRageMath.MatrixD@CreateTranslation)|Creates a translation Matrix.|
|[static CreateTranslation(Vector3)](VRageMath.MatrixD@CreateTranslation)||
|[static CreateTranslation(ref Vector3D, out MatrixD)](VRageMath.MatrixD@CreateTranslation)|Creates a translation Matrix.|
|[static CreateTranslation(double, double, double)](VRageMath.MatrixD@CreateTranslation)|Creates a translation Matrix.|
|[static CreateTranslation(double, double, double, out MatrixD)](VRageMath.MatrixD@CreateTranslation)|Creates a translation Matrix.|
|[static CreateWorld(Vector3D, Vector3, Vector3)](VRageMath.MatrixD@CreateWorld)||
|[static CreateWorld(Vector3D)](VRageMath.MatrixD@CreateWorld)||
|[static CreateWorld(Vector3D, Vector3D, Vector3D)](VRageMath.MatrixD@CreateWorld)|Creates a world matrix with the specified parameters.|
|[static CreateWorld(ref Vector3D, ref Vector3D, ref Vector3D, out MatrixD)](VRageMath.MatrixD@CreateWorld)|Creates a world matrix with the specified parameters.|
|[static Divide(MatrixD, MatrixD)](VRageMath.MatrixD@Divide)|Divides the components of a matrix by the corresponding components of another matrix.|
|[static Divide(ref MatrixD, ref MatrixD, out MatrixD)](VRageMath.MatrixD@Divide)|Divides the components of a matrix by the corresponding components of another matrix.|
|[static Divide(MatrixD, double)](VRageMath.MatrixD@Divide)|Divides the components of a matrix by a scalar.|
|[static Divide(ref MatrixD, double, out MatrixD)](VRageMath.MatrixD@Divide)|Divides the components of a matrix by a scalar.|
|[static GetEulerAnglesXYZ(ref MatrixD, out Vector3D)](VRageMath.MatrixD@GetEulerAnglesXYZ)||
|[static Invert(MatrixD)](VRageMath.MatrixD@Invert)|Calculates the inverse of a matrix.|
|[static Invert(ref MatrixD)](VRageMath.MatrixD@Invert)||
|[static Invert(ref MatrixD, out MatrixD)](VRageMath.MatrixD@Invert)|Calculates the inverse of a matrix.|
|[static Lerp(MatrixD, MatrixD, double)](VRageMath.MatrixD@Lerp)|Linearly interpolates between the corresponding values of two matrices.|
|[static Lerp(ref MatrixD, ref MatrixD, double, out MatrixD)](VRageMath.MatrixD@Lerp)|Linearly interpolates between the corresponding values of two matrices.|
|[static Multiply(MatrixD, MatrixD)](VRageMath.MatrixD@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(MatrixD, Matrix)](VRageMath.MatrixD@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(ref MatrixD, ref Matrix, out MatrixD)](VRageMath.MatrixD@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(ref Matrix, ref MatrixD, out MatrixD)](VRageMath.MatrixD@Multiply)||
|[static Multiply(ref MatrixD, ref MatrixD, out MatrixD)](VRageMath.MatrixD@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(MatrixD, double)](VRageMath.MatrixD@Multiply)|Multiplies a matrix by a scalar value.|
|[static Multiply(ref MatrixD, double, out MatrixD)](VRageMath.MatrixD@Multiply)|Multiplies a matrix by a scalar value.|
|[static Negate(MatrixD)](VRageMath.MatrixD@Negate)|Negates individual elements of a matrix.|
|[static Negate(ref MatrixD, out MatrixD)](VRageMath.MatrixD@Negate)|Negates individual elements of a matrix.|
|[static Normalize(MatrixD)](VRageMath.MatrixD@Normalize)||
|[static Orthogonalize(MatrixD)](VRageMath.MatrixD@Orthogonalize)||
|[static Rescale(ref MatrixD, double)](VRageMath.MatrixD@Rescale)|Same result as Matrix.CreateScale(scale) * matrix, but much faster|
|[static Rescale(ref MatrixD, float)](VRageMath.MatrixD@Rescale)|Same result as Matrix.CreateScale(scale) * matrix, but much faster|
|[static Rescale(ref MatrixD, ref Vector3D)](VRageMath.MatrixD@Rescale)|Same result as Matrix.CreateScale(scale) * matrix, but much faster|
|[static Rescale(MatrixD, double)](VRageMath.MatrixD@Rescale)||
|[static Rescale(MatrixD, Vector3D)](VRageMath.MatrixD@Rescale)||
|[static Slerp(ref MatrixD, ref MatrixD, double, out MatrixD)](VRageMath.MatrixD@Slerp)|Performs spherical linear interpolation of position and rotation.|
|[static Slerp(MatrixD, MatrixD, double)](VRageMath.MatrixD@Slerp)|Performs spherical linear interpolation of position and rotation.|
|[static SlerpScale(ref MatrixD, ref MatrixD, double, out MatrixD)](VRageMath.MatrixD@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static SlerpScale(MatrixD, MatrixD, double, out MatrixD)](VRageMath.MatrixD@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static SlerpScale(MatrixD, MatrixD, double)](VRageMath.MatrixD@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static Subtract(ref MatrixD, ref MatrixD, out MatrixD)](VRageMath.MatrixD@Subtract)|Subtracts matrices.|
|[static Subtract(Matrix, Matrix)](VRageMath.MatrixD@Subtract)|Subtracts matrices.|
|[static SwapYZCoordinates(MatrixD)](VRageMath.MatrixD@SwapYZCoordinates)||
|[static Transform(MatrixD, Quaternion)](VRageMath.MatrixD@Transform)|Transforms a Matrix by applying a Quaternion rotation.|
|[static Transform(ref MatrixD, ref Quaternion, out MatrixD)](VRageMath.MatrixD@Transform)|Transforms a Matrix by applying a Quaternion rotation.|
|[static Transpose(MatrixD)](VRageMath.MatrixD@Transpose)|Transposes the rows and columns of a matrix.|
|[static Transpose(ref MatrixD, out MatrixD)](VRageMath.MatrixD@Transpose)|Transposes the rows and columns of a matrix.|
|[AssertIsValid(string)](VRageMath.MatrixD@AssertIsValid)||
|[Determinant()](VRageMath.MatrixD@Determinant)|Calculates the determinant of the matrix.|
|[Equals(MatrixD)](VRageMath.MatrixD@Equals)|Determines whether the specified Object is equal to the Matrix.|
|[Equals(object)](VRageMath.MatrixD@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[EqualsFast(ref MatrixD, double)](VRageMath.MatrixD@EqualsFast)|Compares just position, forward and up|
|[GetClosestDirection(Vector3D)](VRageMath.MatrixD@GetClosestDirection)||
|[GetClosestDirection(ref Vector3D)](VRageMath.MatrixD@GetClosestDirection)||
|[GetDirectionVector(Direction)](VRageMath.MatrixD@GetDirectionVector)||
|[GetHashCode()](VRageMath.MatrixD@GetHashCode)|Gets the hash code of this object.|
|[GetOrientation()](VRageMath.MatrixD@GetOrientation)|Gets the orientation.|
|[GetRow(int)](VRageMath.MatrixD@GetRow)||
|[HasNoTranslationOrPerspective()](VRageMath.MatrixD@HasNoTranslationOrPerspective)|Returns true if this matrix represents invertible (you can call Invert on it) linear (it does not contain translation or perspective transformation) transformation. Such matrix consist solely of rotations, shearing, mirroring and scaling. It can be orthogonalized to create an orthogonal rotation matrix.|
|[IsMirrored()](VRageMath.MatrixD@IsMirrored)||
|[IsNan()](VRageMath.MatrixD@IsNan)||
|[IsOrthogonal()](VRageMath.MatrixD@IsOrthogonal)||
|[IsOrthogonal(double)](VRageMath.MatrixD@IsOrthogonal)||
|[IsRotation()](VRageMath.MatrixD@IsRotation)||
|[IsValid()](VRageMath.MatrixD@IsValid)||
|[Orthogonalize()](VRageMath.MatrixD@Orthogonalize)||
|[SetDirectionVector(Direction, Vector3D)](VRageMath.MatrixD@SetDirectionVector)||
|[SetFrom(ref Matrix)](VRageMath.MatrixD@SetFrom)||
|[SetRotationAndScale(ref Matrix)](VRageMath.MatrixD@SetRotationAndScale)||
|[SetRow(int, Vector4)](VRageMath.MatrixD@SetRow)||
|[ToString()](VRageMath.MatrixD@ToString)|Retrieves a string representation of the current object.|

**Implements:**  
* [IEquatable<MatrixD>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

