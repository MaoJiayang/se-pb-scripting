**Assembly:** VRage.Math.dll

```csharp
public class Curve
```

Stores an arbitrary collection of 2D CurveKey points, and provides methods for evaluating features of the curve they define.

## Properties

|Member|Description|
|---|---|
|[IsConstant](VRageMath.Curve@IsConstant)|Gets a value indicating whether the curve is constant.|
|[Keys](VRageMath.Curve@Keys)|The points that make up the curve.|
|[PostLoop](VRageMath.Curve@PostLoop)|Specifies how to handle weighting values that are greater than the last control point in the curve.|
|[PreLoop](VRageMath.Curve@PreLoop)|Specifies how to handle weighting values that are less than the first control point in the curve.|

## Constructors

|Member|Description|
|---|---|
|[Curve()](VRageMath.Curve@.ctor)||

## Methods

|Member|Description|
|---|---|
|[Clone()](VRageMath.Curve@Clone)|Creates a copy of the Curve.|
|[ComputeTangent(int, CurveTangent)](VRageMath.Curve@ComputeTangent)|Computes both the TangentIn and the TangentOut for a CurveKey specified by its index.|
|[ComputeTangent(int, CurveTangent, CurveTangent)](VRageMath.Curve@ComputeTangent)|Computes a specified type of TangentIn and a specified type of TangentOut for a given CurveKey.|
|[ComputeTangents(CurveTangent)](VRageMath.Curve@ComputeTangents)|Computes all tangents for all CurveKeys in this Curve, using a specified tangent type for both TangentIn and TangentOut.|
|[ComputeTangents(CurveTangent, CurveTangent)](VRageMath.Curve@ComputeTangents)|Computes all tangents for all CurveKeys in this Curve, using different tangent types for TangentOut and TangentIn.|
|[Evaluate(float)](VRageMath.Curve@Evaluate)|Finds the value at a position on the Curve.|

