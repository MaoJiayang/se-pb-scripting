**Assembly:** VRage.Math.dll

```csharp
public struct RectangleF: IEquatable<RectangleF>
```

Structure using the same layout than [RectangleF](https://docs.microsoft.com/en-us/dotnet/api/system.drawing.rectanglef?view=netframework-4.6) 

## Fields

|Member|Description|
|---|---|
|[Position](VRageMath.RectangleF@Position)|The Position.|
|[Size](VRageMath.RectangleF@Size)|The Size.|

## Properties

|Member|Description|
|---|---|
|[Bottom](VRageMath.RectangleF@Bottom)||
|[Center](VRageMath.RectangleF@Center)||
|[Height](VRageMath.RectangleF@Height)|Height of this rectangle.|
|[Right](VRageMath.RectangleF@Right)||
|[Width](VRageMath.RectangleF@Width)|Width of this rectangle.|
|[X](VRageMath.RectangleF@X)|Left coordinate.|
|[Y](VRageMath.RectangleF@Y)|Top coordinate.|

## Constructors

|Member|Description|
|---|---|
|[RectangleF(Vector2, Vector2)](VRageMath.RectangleF@.ctor)||
|[RectangleF(float, float, float, float)](VRageMath.RectangleF@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Intersect(ref RectangleF, ref RectangleF, out RectangleF)](VRageMath.RectangleF@Intersect)|Creates a Rectangle defining the area where one rectangle overlaps with another rectangle.|
|[static Min(RectangleF?, RectangleF?)](VRageMath.RectangleF@Min)||
|[Contains(int, int)](VRageMath.RectangleF@Contains)||
|[Contains(float, float)](VRageMath.RectangleF@Contains)||
|[Contains(Vector2)](VRageMath.RectangleF@Contains)||
|[Contains(Point)](VRageMath.RectangleF@Contains)||
|[Equals(RectangleF)](VRageMath.RectangleF@Equals)|Equals to other rectangle|
|[Equals(object)](VRageMath.RectangleF@Equals)||
|[GetHashCode()](VRageMath.RectangleF@GetHashCode)||
|[ToString()](VRageMath.RectangleF@ToString)||

**Implements:**  
* [IEquatable<RectangleF>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

