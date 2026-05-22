**Assembly:** VRage.Math.dll

```csharp
public struct Matrix: IEquatable<Matrix>
```

Defines a matrix.

## Fields

|Member|Description|
|---|---|
|[static Identity](VRageMath.Matrix@Identity)||
|[static Zero](VRageMath.Matrix@Zero)||
|[M11](VRageMath.Matrix@M11)|Value at row 1 column 1 of the matrix.|
|[M12](VRageMath.Matrix@M12)|Value at row 1 column 2 of the matrix.|
|[M13](VRageMath.Matrix@M13)|Value at row 1 column 3 of the matrix.|
|[M14](VRageMath.Matrix@M14)|Value at row 1 column 4 of the matrix.|
|[M21](VRageMath.Matrix@M21)|Value at row 2 column 1 of the matrix.|
|[M22](VRageMath.Matrix@M22)|Value at row 2 column 2 of the matrix.|
|[M23](VRageMath.Matrix@M23)|Value at row 2 column 3 of the matrix.|
|[M24](VRageMath.Matrix@M24)|Value at row 2 column 4 of the matrix.|
|[M31](VRageMath.Matrix@M31)|Value at row 3 column 1 of the matrix.|
|[M32](VRageMath.Matrix@M32)|Value at row 3 column 2 of the matrix.|
|[M33](VRageMath.Matrix@M33)|Value at row 3 column 3 of the matrix.|
|[M34](VRageMath.Matrix@M34)|Value at row 3 column 4 of the matrix.|
|[M41](VRageMath.Matrix@M41)|Value at row 4 column 1 of the matrix.|
|[M42](VRageMath.Matrix@M42)|Value at row 4 column 2 of the matrix.|
|[M43](VRageMath.Matrix@M43)|Value at row 4 column 3 of the matrix.|
|[M44](VRageMath.Matrix@M44)|Value at row 4 column 4 of the matrix.|

## Properties

|Member|Description|
|---|---|
|[Backward](VRageMath.Matrix@Backward)|Gets and sets the backward vector of the Matrix.|
|[Col0](VRageMath.Matrix@Col0)||
|[Col1](VRageMath.Matrix@Col1)||
|[Col2](VRageMath.Matrix@Col2)||
|[Down](VRageMath.Matrix@Down)|Gets and sets the down vector of the Matrix.|
|[Forward](VRageMath.Matrix@Forward)|Gets and sets the forward vector of the Matrix.|
|[Item](VRageMath.Matrix@Item)||
|[Left](VRageMath.Matrix@Left)|Gets and sets the left vector of the Matrix.|
|[Right](VRageMath.Matrix@Right)|Gets and sets the right vector of the Matrix.|
|[Scale](VRageMath.Matrix@Scale)||
|[Translation](VRageMath.Matrix@Translation)|Gets and sets the translation vector of the Matrix.|
|[Up](VRageMath.Matrix@Up)|Gets and sets the up vector of the Matrix.|

## Constructors

|Member|Description|
|---|---|
|[Matrix(float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float)](VRageMath.Matrix@.ctor)||
|[Matrix(float, float, float, float, float, float, float, float, float)](VRageMath.Matrix@.ctor)||
|[Matrix(MatrixD)](VRageMath.Matrix@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Add(Matrix, Matrix)](VRageMath.Matrix@Add)|Adds a matrix to another matrix.|
|[static Add(ref Matrix, ref Matrix, out Matrix)](VRageMath.Matrix@Add)|Adds a matrix to another matrix.|
|[static AlignRotationToAxes(ref Matrix, ref Matrix)](VRageMath.Matrix@AlignRotationToAxes)||
|[static CreateBillboard(Vector3, Vector3, Vector3, Vector3?)](VRageMath.Matrix@CreateBillboard)|Creates a spherical billboard that rotates around a specified object position.|
|[static CreateBillboard(ref Vector3, ref Vector3, ref Vector3, Vector3?, out Matrix)](VRageMath.Matrix@CreateBillboard)|Creates a spherical billboard that rotates around a specified object position.|
|[static CreateConstrainedBillboard(Vector3, Vector3, Vector3, Vector3?, Vector3?)](VRageMath.Matrix@CreateConstrainedBillboard)|Creates a cylindrical billboard that rotates around a specified axis.|
|[static CreateConstrainedBillboard(ref Vector3, ref Vector3, ref Vector3, Vector3?, Vector3?, out Matrix)](VRageMath.Matrix@CreateConstrainedBillboard)|Creates a cylindrical billboard that rotates around a specified axis.|
|[static CreateFromAxisAngle(Vector3, float)](VRageMath.Matrix@CreateFromAxisAngle)|Creates a new Matrix that rotates around an arbitrary vector.|
|[static CreateFromAxisAngle(ref Vector3, float, out Matrix)](VRageMath.Matrix@CreateFromAxisAngle)|Creates a new Matrix that rotates around an arbitrary vector.|
|[static CreateFromDir(Vector3)](VRageMath.Matrix@CreateFromDir)||
|[static CreateFromDir(Vector3, Vector3)](VRageMath.Matrix@CreateFromDir)||
|[static CreateFromPerspectiveFieldOfView(ref Matrix, float, float)](VRageMath.Matrix@CreateFromPerspectiveFieldOfView)||
|[static CreateFromQuaternion(Quaternion)](VRageMath.Matrix@CreateFromQuaternion)|Creates a rotation Matrix from a Quaternion.|
|[static CreateFromQuaternion(ref Quaternion, out Matrix)](VRageMath.Matrix@CreateFromQuaternion)|Creates a rotation Matrix from a Quaternion.|
|[static CreateFromTransformScale(Quaternion, Vector3, Vector3)](VRageMath.Matrix@CreateFromTransformScale)||
|[static CreateFromYawPitchRoll(float, float, float)](VRageMath.Matrix@CreateFromYawPitchRoll)|Creates a new rotation matrix from a specified yaw, pitch, and roll.|
|[static CreateFromYawPitchRoll(float, float, float, out Matrix)](VRageMath.Matrix@CreateFromYawPitchRoll)|Fills in a rotation matrix from a specified yaw, pitch, and roll.|
|[static CreateLookAt(Vector3, Vector3, Vector3)](VRageMath.Matrix@CreateLookAt)|Creates a view matrix.|
|[static CreateLookAt(ref Vector3, ref Vector3, ref Vector3, out Matrix)](VRageMath.Matrix@CreateLookAt)|Creates a view matrix.|
|[static CreateLookAtInverse(Vector3, Vector3, Vector3)](VRageMath.Matrix@CreateLookAtInverse)||
|[static CreateOrthographic(float, float, float, float)](VRageMath.Matrix@CreateOrthographic)|Builds an orthogonal projection matrix.|
|[static CreateOrthographic(float, float, float, float, out Matrix)](VRageMath.Matrix@CreateOrthographic)|Builds an orthogonal projection matrix.|
|[static CreateOrthographicOffCenter(float, float, float, float, float, float)](VRageMath.Matrix@CreateOrthographicOffCenter)|Builds a customized, orthogonal projection matrix.|
|[static CreateOrthographicOffCenter(float, float, float, float, float, float, out Matrix)](VRageMath.Matrix@CreateOrthographicOffCenter)|Builds a customized, orthogonal projection matrix.|
|[static CreatePerspective(float, float, float, float)](VRageMath.Matrix@CreatePerspective)|Builds a perspective projection matrix and returns the result by value.|
|[static CreatePerspective(float, float, float, float, out Matrix)](VRageMath.Matrix@CreatePerspective)|Builds a perspective projection matrix and returns the result by reference.|
|[static CreatePerspectiveFieldOfView(float, float, float, float)](VRageMath.Matrix@CreatePerspectiveFieldOfView)|Builds a perspective projection matrix based on a field of view and returns by value.|
|[static CreatePerspectiveFieldOfView(float, float, float, float, out Matrix)](VRageMath.Matrix@CreatePerspectiveFieldOfView)|Builds a perspective projection matrix based on a field of view and returns by reference.|
|[static CreatePerspectiveFovRhComplementary(float, float, float, float)](VRageMath.Matrix@CreatePerspectiveFovRhComplementary)||
|[static CreatePerspectiveFovRhInfinite(float, float, float)](VRageMath.Matrix@CreatePerspectiveFovRhInfinite)||
|[static CreatePerspectiveFovRhInfiniteComplementary(float, float, float)](VRageMath.Matrix@CreatePerspectiveFovRhInfiniteComplementary)||
|[static CreatePerspectiveFovRhInfiniteComplementaryInverse(float, float, float)](VRageMath.Matrix@CreatePerspectiveFovRhInfiniteComplementaryInverse)||
|[static CreatePerspectiveFovRhInfiniteInverse(float, float, float)](VRageMath.Matrix@CreatePerspectiveFovRhInfiniteInverse)||
|[static CreatePerspectiveFovRhInverse(float, float, float, float)](VRageMath.Matrix@CreatePerspectiveFovRhInverse)||
|[static CreatePerspectiveOffCenter(float, float, float, float, float, float)](VRageMath.Matrix@CreatePerspectiveOffCenter)|Builds a customized, perspective projection matrix.|
|[static CreatePerspectiveOffCenter(float, float, float, float, float, float, out Matrix)](VRageMath.Matrix@CreatePerspectiveOffCenter)|Builds a customized, perspective projection matrix.|
|[static CreateReflection(Plane)](VRageMath.Matrix@CreateReflection)|Creates a Matrix that reflects the coordinate system about a specified Plane.|
|[static CreateReflection(ref Plane, out Matrix)](VRageMath.Matrix@CreateReflection)|Fills in an existing Matrix so that it reflects the coordinate system about a specified Plane.|
|[static CreateRotationFromTwoVectors(ref Vector3, ref Vector3, out Matrix)](VRageMath.Matrix@CreateRotationFromTwoVectors)||
|[static CreateRotationX(float)](VRageMath.Matrix@CreateRotationX)|Returns a matrix that can be used to rotate a set of vertices around the x-axis.|
|[static CreateRotationX(float, out Matrix)](VRageMath.Matrix@CreateRotationX)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the x-axis.|
|[static CreateRotationY(float)](VRageMath.Matrix@CreateRotationY)|Returns a matrix that can be used to rotate a set of vertices around the y-axis.|
|[static CreateRotationY(float, out Matrix)](VRageMath.Matrix@CreateRotationY)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the y-axis.|
|[static CreateRotationZ(float)](VRageMath.Matrix@CreateRotationZ)|Returns a matrix that can be used to rotate a set of vertices around the z-axis.|
|[static CreateRotationZ(float, out Matrix)](VRageMath.Matrix@CreateRotationZ)|Populates data into a user-specified matrix that can be used to rotate a set of vertices around the z-axis.|
|[static CreateScale(float, float, float)](VRageMath.Matrix@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(float, float, float, out Matrix)](VRageMath.Matrix@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(Vector3)](VRageMath.Matrix@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(ref Vector3, out Matrix)](VRageMath.Matrix@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(float)](VRageMath.Matrix@CreateScale)|Creates a scaling Matrix.|
|[static CreateScale(float, out Matrix)](VRageMath.Matrix@CreateScale)|Creates a scaling Matrix.|
|[static CreateShadow(Vector3, Plane)](VRageMath.Matrix@CreateShadow)|Creates a Matrix that flattens geometry into a specified Plane as if casting a shadow from a specified light source.|
|[static CreateShadow(ref Vector3, ref Plane, out Matrix)](VRageMath.Matrix@CreateShadow)|Fills in a Matrix to flatten geometry into a specified Plane as if casting a shadow from a specified light source.|
|[static CreateTranslation(Vector3)](VRageMath.Matrix@CreateTranslation)|Creates a translation Matrix.|
|[static CreateTranslation(ref Vector3, out Matrix)](VRageMath.Matrix@CreateTranslation)|Creates a translation Matrix.|
|[static CreateTranslation(float, float, float)](VRageMath.Matrix@CreateTranslation)|Creates a translation Matrix.|
|[static CreateTranslation(float, float, float, out Matrix)](VRageMath.Matrix@CreateTranslation)|Creates a translation Matrix.|
|[static CreateWorld(Vector3)](VRageMath.Matrix@CreateWorld)||
|[static CreateWorld(Vector3, Vector3, Vector3)](VRageMath.Matrix@CreateWorld)|Creates a world matrix with the specified parameters.|
|[static CreateWorld(ref Vector3, ref Vector3, ref Vector3, out Matrix)](VRageMath.Matrix@CreateWorld)|Creates a world matrix with the specified parameters.|
|[static Divide(Matrix, Matrix)](VRageMath.Matrix@Divide)|Divides the components of a matrix by the corresponding components of another matrix.|
|[static Divide(ref Matrix, ref Matrix, out Matrix)](VRageMath.Matrix@Divide)|Divides the components of a matrix by the corresponding components of another matrix.|
|[static Divide(Matrix, float)](VRageMath.Matrix@Divide)|Divides the components of a matrix by a scalar.|
|[static Divide(ref Matrix, float, out Matrix)](VRageMath.Matrix@Divide)|Divides the components of a matrix by a scalar.|
|[static GetEulerAnglesXYZ(ref Matrix, out Vector3)](VRageMath.Matrix@GetEulerAnglesXYZ)||
|[static Invert(Matrix)](VRageMath.Matrix@Invert)|Calculates the inverse of a matrix.|
|[static Invert(ref Matrix)](VRageMath.Matrix@Invert)||
|[static Invert(ref Matrix, out Matrix)](VRageMath.Matrix@Invert)|Calculates the inverse of a matrix.|
|[static Lerp(Matrix, Matrix, float)](VRageMath.Matrix@Lerp)|Linearly interpolates between the corresponding values of two matrices.|
|[static Lerp(ref Matrix, ref Matrix, float, out Matrix)](VRageMath.Matrix@Lerp)|Linearly interpolates between the corresponding values of two matrices.|
|[static Multiply(Matrix, Matrix)](VRageMath.Matrix@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(ref Matrix, ref Matrix, out Matrix)](VRageMath.Matrix@Multiply)|Multiplies a matrix by another matrix.|
|[static Multiply(Matrix, float)](VRageMath.Matrix@Multiply)|Multiplies a matrix by a scalar value.|
|[static Multiply(ref Matrix, float, out Matrix)](VRageMath.Matrix@Multiply)|Multiplies a matrix by a scalar value.|
|[static MultiplyRotation(ref Matrix, ref Matrix, out Matrix)](VRageMath.Matrix@MultiplyRotation)|Multiplies a matrix by another matrix, only rotation parts.|
|[static Negate(Matrix)](VRageMath.Matrix@Negate)|Negates individual elements of a matrix.|
|[static Negate(ref Matrix, out Matrix)](VRageMath.Matrix@Negate)|Negates individual elements of a matrix.|
|[static Normalize(Matrix)](VRageMath.Matrix@Normalize)||
|[static Orthogonalize(Matrix)](VRageMath.Matrix@Orthogonalize)||
|[static Rescale(ref Matrix, float)](VRageMath.Matrix@Rescale)|Same result as Matrix.CreateScale(scale) * matrix, but much faster|
|[static Rescale(ref Matrix, ref Vector3)](VRageMath.Matrix@Rescale)|Same result as Matrix.CreateScale(scale) * matrix, but much faster|
|[static Rescale(Matrix, float)](VRageMath.Matrix@Rescale)||
|[static Rescale(Matrix, Vector3)](VRageMath.Matrix@Rescale)||
|[static Round(ref Matrix)](VRageMath.Matrix@Round)||
|[static Slerp(ref Matrix, ref Matrix, float, out Matrix)](VRageMath.Matrix@Slerp)|Performs spherical linear interpolation of position and rotation.|
|[static Slerp(Matrix, Matrix, float, out Matrix)](VRageMath.Matrix@Slerp)|Performs spherical linear interpolation of position and rotation.|
|[static Slerp(Matrix, Matrix, float)](VRageMath.Matrix@Slerp)|Performs spherical linear interpolation of position and rotation.|
|[static SlerpScale(ref Matrix, ref Matrix, float, out Matrix)](VRageMath.Matrix@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static SlerpScale(Matrix, Matrix, float, out Matrix)](VRageMath.Matrix@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static SlerpScale(Matrix, Matrix, float)](VRageMath.Matrix@SlerpScale)|Performs spherical linear interpolation of position and rotation and scale.|
|[static Subtract(ref Matrix, ref Matrix, out Matrix)](VRageMath.Matrix@Subtract)|Subtracts matrices.|
|[static Subtract(Matrix, Matrix)](VRageMath.Matrix@Subtract)|Subtracts matrices.|
|[static SwapYZCoordinates(Matrix)](VRageMath.Matrix@SwapYZCoordinates)||
|[static Transform(Matrix, Quaternion)](VRageMath.Matrix@Transform)|Transforms a Matrix by applying a Quaternion rotation.|
|[static Transform(ref Matrix, ref Quaternion, out Matrix)](VRageMath.Matrix@Transform)|Transforms a Matrix by applying a Quaternion rotation.|
|[static Transpose(Matrix)](VRageMath.Matrix@Transpose)|Transposes the rows and columns of a matrix.|
|[static Transpose(ref Matrix, out Matrix)](VRageMath.Matrix@Transpose)|Transposes the rows and columns of a matrix.|
|[AssertIsValid()](VRageMath.Matrix@AssertIsValid)||
|[Determinant()](VRageMath.Matrix@Determinant)|Calculates the determinant of the matrix.|
|[Equals(Matrix)](VRageMath.Matrix@Equals)|Determines whether the specified Object is equal to the Matrix.|
|[Equals(object)](VRageMath.Matrix@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[EqualsFast(ref Matrix, float)](VRageMath.Matrix@EqualsFast)|Compares just position, forward and up|
|[GetClosestDirection(Vector3)](VRageMath.Matrix@GetClosestDirection)||
|[GetClosestDirection(ref Vector3)](VRageMath.Matrix@GetClosestDirection)||
|[GetDirectionVector(Direction)](VRageMath.Matrix@GetDirectionVector)||
|[GetHashCode()](VRageMath.Matrix@GetHashCode)|Gets the hash code of this object.|
|[GetOrientation()](VRageMath.Matrix@GetOrientation)|Gets the orientation.|
|[GetRow(int)](VRageMath.Matrix@GetRow)||
|[HasNoTranslationOrPerspective()](VRageMath.Matrix@HasNoTranslationOrPerspective)|Returns true if this matrix represents invertible (you can call Invert on it) linear (it does not contain translation or perspective transformation) transformation. Such matrix consist solely of rotations, shearing, mirroring and scaling. It can be orthogonalized to create an orthogonal rotation matrix.|
|[IsMirrored()](VRageMath.Matrix@IsMirrored)||
|[IsNan()](VRageMath.Matrix@IsNan)||
|[IsOrthogonal()](VRageMath.Matrix@IsOrthogonal)||
|[IsRotation()](VRageMath.Matrix@IsRotation)||
|[IsValid()](VRageMath.Matrix@IsValid)||
|[SetDirectionVector(Direction, Vector3)](VRageMath.Matrix@SetDirectionVector)||
|[SetFrom(ref MatrixD)](VRageMath.Matrix@SetFrom)|Set this ma|
|[SetRotationAndScale(ref MatrixD)](VRageMath.Matrix@SetRotationAndScale)||
|[SetRow(int, Vector4)](VRageMath.Matrix@SetRow)||
|[ToString()](VRageMath.Matrix@ToString)|Retrieves a string representation of the current object.|
|[TransposeRotationInPlace()](VRageMath.Matrix@TransposeRotationInPlace)|Transposes the rows and columns of a matrix that is assumed to be rotation only in place.|

**Implements:**  
* [IEquatable<Matrix>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

