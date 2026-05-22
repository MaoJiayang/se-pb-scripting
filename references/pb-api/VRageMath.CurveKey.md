**Assembly:** VRage.Math.dll

```csharp
public class CurveKey: IEquatable<CurveKey>, IComparable<CurveKey>
```

Represents a point in a multi-point curve.

## Properties

|Member|Description|
|---|---|
|[Continuity](VRageMath.CurveKey@Continuity)|Describes whether the segment between this point and the next point in the curve is discrete or continuous.|
|[Position](VRageMath.CurveKey@Position)|Position of the CurveKey in the curve.|
|[TangentIn](VRageMath.CurveKey@TangentIn)|Describes the tangent when approaching this point from the previous point in the curve.|
|[TangentOut](VRageMath.CurveKey@TangentOut)|Describes the tangent when leaving this point to the next point in the curve.|
|[Value](VRageMath.CurveKey@Value)|Describes the value of this point.|

## Constructors

|Member|Description|
|---|---|
|[CurveKey()](VRageMath.CurveKey@.ctor)||
|[CurveKey(float, float)](VRageMath.CurveKey@.ctor)||
|[CurveKey(float, float, float, float)](VRageMath.CurveKey@.ctor)||
|[CurveKey(float, float, float, float, CurveContinuity)](VRageMath.CurveKey@.ctor)||

## Methods

|Member|Description|
|---|---|
|[Clone()](VRageMath.CurveKey@Clone)|Creates a copy of the CurveKey.|
|[CompareTo(CurveKey)](VRageMath.CurveKey@CompareTo)|Compares this instance to another CurveKey and returns an indication of their relative values.|
|[Equals(CurveKey)](VRageMath.CurveKey@Equals)|Determines whether the specified Object is equal to the CurveKey.|
|[Equals(object)](VRageMath.CurveKey@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetHashCode()](VRageMath.CurveKey@GetHashCode)|Returns the hash code for this instance.|

**Implements:**  
* [IComparable<CurveKey>](https://docs.microsoft.com/en-us/dotnet/api/System.IComparable-1?view=netframework-4.6)  
* [IEquatable<CurveKey>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

