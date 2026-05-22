**Assembly:** VRage.Math.dll

```csharp
public struct MatrixI
```

## Fields

|Member|Description|
|---|---|
|[Backward](VRageMath.MatrixI@Backward)||
|[Right](VRageMath.MatrixI@Right)||
|[Translation](VRageMath.MatrixI@Translation)||
|[Up](VRageMath.MatrixI@Up)||

## Properties

|Member|Description|
|---|---|
|[BackwardVector](VRageMath.MatrixI@BackwardVector)||
|[Down](VRageMath.MatrixI@Down)||
|[DownVector](VRageMath.MatrixI@DownVector)||
|[Forward](VRageMath.MatrixI@Forward)||
|[ForwardVector](VRageMath.MatrixI@ForwardVector)||
|[Left](VRageMath.MatrixI@Left)||
|[LeftVector](VRageMath.MatrixI@LeftVector)||
|[RightVector](VRageMath.MatrixI@RightVector)||
|[UpVector](VRageMath.MatrixI@UpVector)||

## Constructors

|Member|Description|
|---|---|
|[MatrixI(ref Vector3I, Direction, Direction)](VRageMath.MatrixI@.ctor)||
|[MatrixI(Vector3I, Direction, Direction)](VRageMath.MatrixI@.ctor)||
|[MatrixI(Direction, Direction)](VRageMath.MatrixI@.ctor)||
|[MatrixI(ref Vector3I, ref Vector3I, ref Vector3I)](VRageMath.MatrixI@.ctor)||
|[MatrixI(ref Vector3I, ref Vector3, ref Vector3)](VRageMath.MatrixI@.ctor)||
|[MatrixI(MyBlockOrientation)](VRageMath.MatrixI@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static CreateRotation(Direction, Direction, Direction, Direction)](VRageMath.MatrixI@CreateRotation)||
|[static Invert(ref MatrixI, out MatrixI)](VRageMath.MatrixI@Invert)||
|[static Multiply(ref MatrixI, ref MatrixI, out MatrixI)](VRageMath.MatrixI@Multiply)||
|[static Transform(ref MyBlockOrientation, ref MatrixI)](VRageMath.MatrixI@Transform)||
|[GetBlockOrientation()](VRageMath.MatrixI@GetBlockOrientation)||
|[GetDirection(Direction)](VRageMath.MatrixI@GetDirection)||
|[GetFloatMatrix()](VRageMath.MatrixI@GetFloatMatrix)||
|[SetDirection(Direction, Direction)](VRageMath.MatrixI@SetDirection)||

