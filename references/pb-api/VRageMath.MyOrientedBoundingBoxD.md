**Assembly:** VRage.Math.dll

```csharp
public struct MyOrientedBoundingBoxD: IEquatable<MyOrientedBoundingBoxD>
```

## Fields

|Member|Description|
|---|---|
|[static CornerCount](VRageMath.MyOrientedBoundingBoxD@CornerCount)||
|[static EndVertices](VRageMath.MyOrientedBoundingBoxD@EndVertices)||
|[static EndXVertices](VRageMath.MyOrientedBoundingBoxD@EndXVertices)||
|[static EndYVertices](VRageMath.MyOrientedBoundingBoxD@EndYVertices)||
|[static EndZVertices](VRageMath.MyOrientedBoundingBoxD@EndZVertices)||
|[static StartVertices](VRageMath.MyOrientedBoundingBoxD@StartVertices)||
|[static StartXVertices](VRageMath.MyOrientedBoundingBoxD@StartXVertices)||
|[static StartYVertices](VRageMath.MyOrientedBoundingBoxD@StartYVertices)||
|[static StartZVertices](VRageMath.MyOrientedBoundingBoxD@StartZVertices)||
|[static XNeighbourVectorsBack](VRageMath.MyOrientedBoundingBoxD@XNeighbourVectorsBack)||
|[static XNeighbourVectorsForw](VRageMath.MyOrientedBoundingBoxD@XNeighbourVectorsForw)||
|[static YNeighbourVectorsBack](VRageMath.MyOrientedBoundingBoxD@YNeighbourVectorsBack)||
|[static YNeighbourVectorsForw](VRageMath.MyOrientedBoundingBoxD@YNeighbourVectorsForw)||
|[static ZNeighbourVectorsBack](VRageMath.MyOrientedBoundingBoxD@ZNeighbourVectorsBack)||
|[static ZNeighbourVectorsForw](VRageMath.MyOrientedBoundingBoxD@ZNeighbourVectorsForw)||
|[Center](VRageMath.MyOrientedBoundingBoxD@Center)||
|[HalfExtent](VRageMath.MyOrientedBoundingBoxD@HalfExtent)||
|[Orientation](VRageMath.MyOrientedBoundingBoxD@Orientation)||

## Constructors

|Member|Description|
|---|---|
|[MyOrientedBoundingBoxD(MatrixD)](VRageMath.MyOrientedBoundingBoxD@.ctor)||
|[MyOrientedBoundingBoxD(Vector3D, Vector3D, Quaternion)](VRageMath.MyOrientedBoundingBoxD@.ctor)||
|[MyOrientedBoundingBoxD(BoundingBoxD, MatrixD)](VRageMath.MyOrientedBoundingBoxD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Contains(ref BoundingBox, ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[static Contains(BoundingFrustumD, ref MyOrientedBoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[static Contains(ref BoundingSphere, ref MyOrientedBoundingBox)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[static ContainsRelativeBox(ref Vector3D, ref Vector3D, ref MatrixD)](VRageMath.MyOrientedBoundingBoxD@ContainsRelativeBox)||
|[static Create(BoundingBoxD, MatrixD)](VRageMath.MyOrientedBoundingBoxD@Create)||
|[static CreateFromBoundingBox(BoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@CreateFromBoundingBox)||
|[static GetNormalBetweenEdges(int, int, int, out Vector3)](VRageMath.MyOrientedBoundingBoxD@GetNormalBetweenEdges)|Returns normal between two cube edge of same direction|
|[Contains(ref BoundingBox)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[Contains(ref BoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[Contains(ref MyOrientedBoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[Contains(BoundingFrustumD)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[Contains(ref BoundingSphereD)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[Contains(ref Vector3)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[Contains(ref Vector3D)](VRageMath.MyOrientedBoundingBoxD@Contains)||
|[ConvertToFrustum()](VRageMath.MyOrientedBoundingBoxD@ConvertToFrustum)||
|[Distance(RayD)](VRageMath.MyOrientedBoundingBoxD@Distance)||
|[Equals(MyOrientedBoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@Equals)||
|[Equals(object)](VRageMath.MyOrientedBoundingBoxD@Equals)||
|[GetAABB()](VRageMath.MyOrientedBoundingBoxD@GetAABB)||
|[GetCorner(int)](VRageMath.MyOrientedBoundingBoxD@GetCorner)|Gets corner of the BB by index|
|[GetCorners(Vector3D[], int)](VRageMath.MyOrientedBoundingBoxD@GetCorners)||
|[GetHashCode()](VRageMath.MyOrientedBoundingBoxD@GetHashCode)||
|[Intersects(ref BoundingBox)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(ref BoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(ref MyOrientedBoundingBoxD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(BoundingFrustumD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(ref BoundingSphereD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(ref RayD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(ref LineD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[Intersects(ref PlaneD)](VRageMath.MyOrientedBoundingBoxD@Intersects)||
|[IntersectsOrContains(ref LineD)](VRageMath.MyOrientedBoundingBoxD@IntersectsOrContains)||
|[ToString()](VRageMath.MyOrientedBoundingBoxD@ToString)||
|[Transform(Quaternion, Vector3D)](VRageMath.MyOrientedBoundingBoxD@Transform)||
|[Transform(float, Quaternion, Vector3D)](VRageMath.MyOrientedBoundingBoxD@Transform)||
|[Transform(MatrixD)](VRageMath.MyOrientedBoundingBoxD@Transform)||
|[Transform(ref MatrixD)](VRageMath.MyOrientedBoundingBoxD@Transform)||

**Implements:**  
* [IEquatable<MyOrientedBoundingBoxD>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

