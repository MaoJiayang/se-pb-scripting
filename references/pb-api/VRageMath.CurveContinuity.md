**Assembly:** VRage.Math.dll

```csharp
public enum CurveContinuity
```

Defines the continuity of CurveKeys on a Curve.

## Fields

|Member|Description|
|---|---|
|Smooth|Interpolation can be used between this CurveKey and the next.|
|Step|Interpolation cannot be used between this CurveKey and the next. Specifying a position between the two points returns this point.|

