**Assembly:** VRage.Math.dll

```csharp
public struct MyOrientedBoundingBox: IEquatable<MyOrientedBoundingBox>
```

## Fields

|Member|Description|
|---|---|
|[static CornerCount](VRageMath.MyOrientedBoundingBox@CornerCount)||
|[static EndVertices](VRageMath.MyOrientedBoundingBox@EndVertices)||
|[static EndXVertices](VRageMath.MyOrientedBoundingBox@EndXVertices)||
|[static EndYVertices](VRageMath.MyOrientedBoundingBox@EndYVertices)||
|[static EndZVertices](VRageMath.MyOrientedBoundingBox@EndZVertices)||
|[static StartVertices](VRageMath.MyOrientedBoundingBox@StartVertices)||
|[static StartXVertices](VRageMath.MyOrientedBoundingBox@StartXVertices)||
|[static StartYVertices](VRageMath.MyOrientedBoundingBox@StartYVertices)||
|[static StartZVertices](VRageMath.MyOrientedBoundingBox@StartZVertices)||
|[static XNeighbourVectorsBack](VRageMath.MyOrientedBoundingBox@XNeighbourVectorsBack)||
|[static XNeighbourVectorsForw](VRageMath.MyOrientedBoundingBox@XNeighbourVectorsForw)||
|[static YNeighbourVectorsBack](VRageMath.MyOrientedBoundingBox@YNeighbourVectorsBack)||
|[static YNeighbourVectorsForw](VRageMath.MyOrientedBoundingBox@YNeighbourVectorsForw)||
|[static ZNeighbourVectorsBack](VRageMath.MyOrientedBoundingBox@ZNeighbourVectorsBack)||
|[static ZNeighbourVectorsForw](VRageMath.MyOrientedBoundingBox@ZNeighbourVectorsForw)||
|[Center](VRageMath.MyOrientedBoundingBox@Center)||
|[HalfExtent](VRageMath.MyOrientedBoundingBox@HalfExtent)||
|[Orientation](VRageMath.MyOrientedBoundingBox@Orientation)||

## Constructors

|Member|Description|
|---|---|
|[MyOrientedBoundingBox(ref Matrix)](VRageMath.MyOrientedBoundingBox@.ctor)||
|[MyOrientedBoundingBox(Vector3, Vector3, Quaternion)](VRageMath.MyOrientedBoundingBox@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Contains(ref BoundingBox, ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBox@Contains)||
|[static Contains(BoundingFrustum, ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBox@Contains)||
|[static Contains(ref BoundingSphere, ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBox@Contains)||
|[static ContainsRelativeBox(ref Vector3, ref Vector3, ref Matrix)](VRageMath.MyOrientedBoundingBox@ContainsRelativeBox)||
|[static Create(BoundingBox, Matrix)](VRageMath.MyOrientedBoundingBox@Create)||
|[static CreateFromBoundingBox(BoundingBox)](VRageMath.MyOrientedBoundingBox@CreateFromBoundingBox)||
|[static GetNormalBetweenEdges(int, int, int, out Vector3)](VRageMath.MyOrientedBoundingBox@GetNormalBetweenEdges)|Returns normal between two cube edge of same direction|
|[Contains(ref BoundingBox)](VRageMath.MyOrientedBoundingBox@Contains)||
|[Contains(ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBox@Contains)||
|[Contains(BoundingFrustum)](VRageMath.MyOrientedBoundingBox@Contains)||
|[Contains(ref BoundingSphere)](VRageMath.MyOrientedBoundingBox@Contains)||
|[Contains(ref Vector3)](VRageMath.MyOrientedBoundingBox@Contains)||
|[ConvertToFrustum()](VRageMath.MyOrientedBoundingBox@ConvertToFrustum)||
|[Equals(MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBox@Equals)||
|[Equals(object)](VRageMath.MyOrientedBoundingBox@Equals)||
|[GetAABB()](VRageMath.MyOrientedBoundingBox@GetAABB)||
|[GetCorners(Vector3[], int)](VRageMath.MyOrientedBoundingBox@GetCorners)||
|[GetHashCode()](VRageMath.MyOrientedBoundingBox@GetHashCode)||
|[Intersects(ref BoundingBox)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[Intersects(ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[Intersects(BoundingFrustum)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[Intersects(ref BoundingSphere)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[Intersects(ref Ray)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[Intersects(ref Line)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[Intersects(ref Plane)](VRageMath.MyOrientedBoundingBox@Intersects)||
|[ToString()](VRageMath.MyOrientedBoundingBox@ToString)||
|[Transform(Quaternion, Vector3)](VRageMath.MyOrientedBoundingBox@Transform)||
|[Transform(float, Quaternion, Vector3)](VRageMath.MyOrientedBoundingBox@Transform)||
|[Transform(Matrix)](VRageMath.MyOrientedBoundingBox@Transform)||

**Implements:**  
* [IEquatable<MyOrientedBoundingBox>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

