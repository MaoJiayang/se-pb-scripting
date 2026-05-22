**Assembly:** VRage.Math.dll

```csharp
public abstract sealed class MathHelper
```

Contains commonly used precalculated values.

## Fields

|Member|Description|
|---|---|
|[static E](VRageMath.MathHelper@E)|Represents the mathematical constant e.|
|[static EPSILON](VRageMath.MathHelper@EPSILON)||
|[static EPSILON10](VRageMath.MathHelper@EPSILON10)||
|[static FourPi](VRageMath.MathHelper@FourPi)|Represents the value of pi times two.|
|[static Log10E](VRageMath.MathHelper@Log10E)|Represents the log base ten of e.|
|[static Log2E](VRageMath.MathHelper@Log2E)|Represents the log base two of e.|
|[static Pi](VRageMath.MathHelper@Pi)|Represents the value of pi.|
|[static PiOver2](VRageMath.MathHelper@PiOver2)|Represents the value of pi divided by two.|
|[static PiOver4](VRageMath.MathHelper@PiOver4)|Represents the value of pi divided by four.|
|[static RadiansPerSecondToRPM](VRageMath.MathHelper@RadiansPerSecondToRPM)|60 / 2*pi|
|[static RPMToRadiansPerMillisec](VRageMath.MathHelper@RPMToRadiansPerMillisec)|2*pi / 60000|
|[static RPMToRadiansPerSecond](VRageMath.MathHelper@RPMToRadiansPerSecond)|2*pi / 60|
|[static Sqrt2](VRageMath.MathHelper@Sqrt2)|Represents the value of the square root of two|
|[static Sqrt3](VRageMath.MathHelper@Sqrt3)|Represents the value of the square root of three|
|[static TwoPi](VRageMath.MathHelper@TwoPi)|Represents the value of pi times two.|

## Methods

|Member|Description|
|---|---|
|[static Align(int, int)](VRageMath.MathHelper@Align)||
|[static Atan(float)](VRageMath.MathHelper@Atan)|Faster Atan implementation. Good only in the [-pi/2, pi/2] range.|
|[static Atan(double)](VRageMath.MathHelper@Atan)|Faster Atan implementation. Good only in the [-pi/2, pi/2] range.|
|[static Barycentric(float, float, float, float, float)](VRageMath.MathHelper@Barycentric)|Returns the Cartesian coordinate for one axis of a point that is defined by a given triangle and two normalized barycentric (areal) coordinates.|
|[static CalculateBezierPoint(double, Vector3D, Vector3D, Vector3D, Vector3D)](VRageMath.MathHelper@CalculateBezierPoint)||
|[static CalculateVectorOnSphere(Vector3, float, float)](VRageMath.MathHelper@CalculateVectorOnSphere)||
|[static CatmullRom(float, float, float, float, float)](VRageMath.MathHelper@CatmullRom)|Performs a Catmull-Rom interpolation using the specified positions.|
|[static CeilToInt(float)](VRageMath.MathHelper@CeilToInt)||
|[static CeilToInt(double)](VRageMath.MathHelper@CeilToInt)||
|[static Clamp(float, float, float)](VRageMath.MathHelper@Clamp)|Restricts a value to be within a specified range. Reference page contains links to related code samples.|
|[static Clamp(double, double, double)](VRageMath.MathHelper@Clamp)|Restricts a value to be within a specified range. Reference page contains links to related code samples.|
|[static Clamp(MyFixedPoint, MyFixedPoint, MyFixedPoint)](VRageMath.MathHelper@Clamp)|Restricts a value to be within a specified range. Reference page contains links to related code samples.|
|[static Clamp(int, int, int)](VRageMath.MathHelper@Clamp)|Restricts a value to be within a specified range. Reference page contains links to related code samples.|
|[static Clamp(byte, byte, byte)](VRageMath.MathHelper@Clamp)|Restricts a value to be within a specified range.|
|[static ComputeHashFromBytes(Byte[])](VRageMath.MathHelper@ComputeHashFromBytes)||
|[static CubicInterp(double, double, double, double, double)](VRageMath.MathHelper@CubicInterp)||
|[static Distance(float, float)](VRageMath.MathHelper@Distance)|Calculates the absolute value of the difference of two values.|
|[static Floor(float)](VRageMath.MathHelper@Floor)||
|[static Floor(double)](VRageMath.MathHelper@Floor)||
|[static FloorToInt(float)](VRageMath.MathHelper@FloorToInt)||
|[static FloorToInt(double)](VRageMath.MathHelper@FloorToInt)||
|[static GetNearestBiggerPowerOfTwo(int)](VRageMath.MathHelper@GetNearestBiggerPowerOfTwo)||
|[static GetNearestBiggerPowerOfTwo(uint)](VRageMath.MathHelper@GetNearestBiggerPowerOfTwo)||
|[static GetNearestBiggerPowerOfTwo(float)](VRageMath.MathHelper@GetNearestBiggerPowerOfTwo)|Returns nearest bigger power of two|
|[static GetNearestBiggerPowerOfTwo(double)](VRageMath.MathHelper@GetNearestBiggerPowerOfTwo)||
|[static GetNumberOfMipmaps(int)](VRageMath.MathHelper@GetNumberOfMipmaps)||
|[static Hermite(float, float, float, float, float)](VRageMath.MathHelper@Hermite)|Performs a Hermite spline interpolation.|
|[static InterpLog(float, float, float)](VRageMath.MathHelper@InterpLog)|Performs interpolation on logarithmic scale.|
|[static InterpLogInv(float, float, float)](VRageMath.MathHelper@InterpLogInv)||
|[static IsEqual(float, float)](VRageMath.MathHelper@IsEqual)||
|[static IsEqual(Vector2, Vector2)](VRageMath.MathHelper@IsEqual)||
|[static IsEqual(Vector3, Vector3)](VRageMath.MathHelper@IsEqual)||
|[static IsEqual(Quaternion, Quaternion)](VRageMath.MathHelper@IsEqual)||
|[static IsEqual(QuaternionD, QuaternionD)](VRageMath.MathHelper@IsEqual)||
|[static IsEqual(Matrix, Matrix)](VRageMath.MathHelper@IsEqual)||
|[static IsPowerOfTwo(int)](VRageMath.MathHelper@IsPowerOfTwo)|Returns true if value is power of two|
|[static IsValid(Matrix)](VRageMath.MathHelper@IsValid)||
|[static IsValid(MatrixD)](VRageMath.MathHelper@IsValid)||
|[static IsValid(Vector3)](VRageMath.MathHelper@IsValid)||
|[static IsValid(Vector3D)](VRageMath.MathHelper@IsValid)||
|[static IsValid(Vector2)](VRageMath.MathHelper@IsValid)||
|[static IsValid(float)](VRageMath.MathHelper@IsValid)||
|[static IsValid(double)](VRageMath.MathHelper@IsValid)||
|[static IsValid(Vector3?)](VRageMath.MathHelper@IsValid)||
|[static IsValid(Quaternion)](VRageMath.MathHelper@IsValid)||
|[static IsValidNormal(Vector3)](VRageMath.MathHelper@IsValidNormal)||
|[static IsValidOrZero(Matrix)](VRageMath.MathHelper@IsValidOrZero)||
|[static IsZero(float, float)](VRageMath.MathHelper@IsZero)||
|[static IsZero(double, float)](VRageMath.MathHelper@IsZero)||
|[static IsZero(Vector3, float)](VRageMath.MathHelper@IsZero)||
|[static IsZero(Vector3D, float)](VRageMath.MathHelper@IsZero)||
|[static IsZero(Quaternion, float)](VRageMath.MathHelper@IsZero)||
|[static IsZero(Vector4)](VRageMath.MathHelper@IsZero)||
|[static Lerp(float, float, float)](VRageMath.MathHelper@Lerp)|Linearly interpolates between two values.|
|[static Lerp(double, double, double)](VRageMath.MathHelper@Lerp)|Linearly interpolates between two values.|
|[static LimitRadians(ref float)](VRageMath.MathHelper@LimitRadians)|Returns angle in range 0..2*PI|
|[static LimitRadians2PI(ref double)](VRageMath.MathHelper@LimitRadians2PI)|Returns angle in range 0..2*PI|
|[static LimitRadiansPI(ref double)](VRageMath.MathHelper@LimitRadiansPI)|Returns angle in range -PI..PI|
|[static LimitRadiansPI(ref float)](VRageMath.MathHelper@LimitRadiansPI)|Returns angle in range -PI..PI|
|[static Log2(int)](VRageMath.MathHelper@Log2)||
|[static Log2(uint)](VRageMath.MathHelper@Log2)||
|[static Log2Ceiling(int)](VRageMath.MathHelper@Log2Ceiling)||
|[static Log2Floor(int)](VRageMath.MathHelper@Log2Floor)||
|[static Max(float, float)](VRageMath.MathHelper@Max)|Returns the greater of two values.|
|[static Max(double, double)](VRageMath.MathHelper@Max)|Returns the greater of two values.|
|[static Max(float, float, float)](VRageMath.MathHelper@Max)||
|[static Max(int, int, int)](VRageMath.MathHelper@Max)||
|[static Max(double, double, double)](VRageMath.MathHelper@Max)||
|[static Min(float, float)](VRageMath.MathHelper@Min)|Returns the lesser of two values.|
|[static Min(double, double)](VRageMath.MathHelper@Min)|Returns the lesser of two values.|
|[static Min(float, float, float)](VRageMath.MathHelper@Min)||
|[static Min(double, double, double)](VRageMath.MathHelper@Min)||
|[static MonotonicAcos(float)](VRageMath.MathHelper@MonotonicAcos)||
|[static MonotonicCosine(float)](VRageMath.MathHelper@MonotonicCosine)|Calculate the monotonic cosine of a value. Monotonic cosine is an alternative cosine encoding that is monotonic in the [-pi, pi] interval. We use this when some parameter of an onject in a planet is constrained by latitude. The 'monotonicity' is guaranteed by subtracting the cosine value from 2 if the angle is positive. So for instance MonotonicCos(pi/2) = 2. This only works in the above interval of course.|
|[static Pow2(int)](VRageMath.MathHelper@Pow2)|Returns 2^n|
|[static RoundOn2(float)](VRageMath.MathHelper@RoundOn2)||
|[static RoundToInt(float)](VRageMath.MathHelper@RoundToInt)||
|[static RoundToInt(double)](VRageMath.MathHelper@RoundToInt)||
|[static Saturate(float)](VRageMath.MathHelper@Saturate)||
|[static Saturate(double)](VRageMath.MathHelper@Saturate)||
|[static SCurve3(float)](VRageMath.MathHelper@SCurve3)||
|[static SCurve3(double)](VRageMath.MathHelper@SCurve3)||
|[static SCurve5(float)](VRageMath.MathHelper@SCurve5)||
|[static SCurve5(double)](VRageMath.MathHelper@SCurve5)||
|[static Smooth(int, int)](VRageMath.MathHelper@Smooth)||
|[static Smooth(float, float)](VRageMath.MathHelper@Smooth)||
|[static SmoothStep(float, float, float)](VRageMath.MathHelper@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStep(double, double, double)](VRageMath.MathHelper@SmoothStep)|Interpolates between two values using a cubic equation.|
|[static SmoothStepStable(float)](VRageMath.MathHelper@SmoothStepStable)|Interpolates between zero and one using cubic equiation, solved by de Casteljau.|
|[static SmoothStepStable(double)](VRageMath.MathHelper@SmoothStepStable)|Interpolates between zero and one using cubic equiation, solved by de Casteljau.|
|[static ToDegrees(float)](VRageMath.MathHelper@ToDegrees)|Converts radians to degrees.|
|[static ToDegrees(double)](VRageMath.MathHelper@ToDegrees)||
|[static ToRadians(float)](VRageMath.MathHelper@ToRadians)|Converts degrees to radians.|
|[static ToRadians(Vector3)](VRageMath.MathHelper@ToRadians)||
|[static ToRadians(double)](VRageMath.MathHelper@ToRadians)|Converts degrees to radians.|
|[static WrapAngle(float)](VRageMath.MathHelper@WrapAngle)|Reduces a given angle to a value between π and -π.|

