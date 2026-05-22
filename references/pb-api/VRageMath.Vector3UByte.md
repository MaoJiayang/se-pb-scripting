**Assembly:** VRage.Math.dll

```csharp
public struct Vector3UByte
```

## Fields

|Member|Description|
|---|---|
|[static Comparer](VRageMath.Vector3UByte@Comparer)||
|[static Zero](VRageMath.Vector3UByte@Zero)||
|[X](VRageMath.Vector3UByte@X)||
|[Y](VRageMath.Vector3UByte@Y)||
|[Z](VRageMath.Vector3UByte@Z)||

## Constructors

|Member|Description|
|---|---|
|[Vector3UByte(byte, byte, byte)](VRageMath.Vector3UByte@.ctor)||
|[Vector3UByte(Vector3I)](VRageMath.Vector3UByte@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Denormalize(Vector3UByte, float)](VRageMath.Vector3UByte@Denormalize)|Unpacks Vector3 from Vector3UByte, scales vector from (0, 255) to (-range, range)|
|[static Floor(Vector3)](VRageMath.Vector3UByte@Floor)||
|[static IsMiddle(Vector3UByte)](VRageMath.Vector3UByte@IsMiddle)|Returns true when all components are 127|
|[static Normalize(Vector3, float)](VRageMath.Vector3UByte@Normalize)|Normalizes Vector3 into Vector4UByte, scales vector from (-range, range) to (0, 255). Unsafe for values "range >= any_vec_value / 257";|
|[static Round(Vector3)](VRageMath.Vector3UByte@Round)||
|[Equals(object)](VRageMath.Vector3UByte@Equals)||
|[GetHashCode()](VRageMath.Vector3UByte@GetHashCode)||
|[LengthSquared()](VRageMath.Vector3UByte@LengthSquared)||
|[ToString()](VRageMath.Vector3UByte@ToString)||

