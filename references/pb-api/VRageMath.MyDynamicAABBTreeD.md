**Assembly:** VRage.Math.dll

```csharp
public class MyDynamicAABBTreeD
```

Dynamic aabb tree implementation as a prunning structure

## Fields

|Member|Description|
|---|---|
|[static NullNode](VRageMath.MyDynamicAABBTreeD@NullNode)|A dynamic tree arranges data in a binary tree to accelerate queries such as volume queries and ray casts. Leafs are proxies with an BoundingBox. In the tree we expand the proxy BoundingBox by Settings.b2_fatAABBFactor so that the proxy BoundingBox is bigger than the client object. This allows the client object to move by small amounts without triggering a tree update. Nodes are pooled and relocatable, so we use node indices rather than pointers.|

## Properties

|Member|Description|
|---|---|
|[ElementsCount](VRageMath.MyDynamicAABBTreeD@ElementsCount)||

## Constructors

|Member|Description|
|---|---|
|[MyDynamicAABBTreeD()](VRageMath.MyDynamicAABBTreeD@.ctor)||
|[MyDynamicAABBTreeD(Vector3D, double)](VRageMath.MyDynamicAABBTreeD@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Dispose()](VRageMath.MyDynamicAABBTreeD@Dispose)||
|[AddProxy(ref BoundingBoxD, object, uint, bool)](VRageMath.MyDynamicAABBTreeD@AddProxy)|Create a proxy. Provide a tight fitting BoundingBox and a userData pointer.|
|[Balance(int)](VRageMath.MyDynamicAABBTreeD@Balance)||
|[Clear()](VRageMath.MyDynamicAABBTreeD@Clear)||
|[CountLeaves(int)](VRageMath.MyDynamicAABBTreeD@CountLeaves)||
|[GetAabb(int)](VRageMath.MyDynamicAABBTreeD@GetAabb)||
|[GetAll<T>(List<T>, bool, List<BoundingBoxD>)](VRageMath.MyDynamicAABBTreeD@GetAll{T})||
|[GetAll<T>(Action<T>)](VRageMath.MyDynamicAABBTreeD@GetAll{T})||
|[GetAll<T>(Action<T, BoundingBoxD>)](VRageMath.MyDynamicAABBTreeD@GetAll{T})||
|[GetAllNodeBounds(List<BoundingBoxD>)](VRageMath.MyDynamicAABBTreeD@GetAllNodeBounds)||
|[GetAproximateClustersForAabb(ref BoundingBoxD, double, List<BoundingBoxD>)](VRageMath.MyDynamicAABBTreeD@GetAproximateClustersForAabb)||
|[GetAproximateClustersForAabbDebug(ref BoundingBoxD, double, List<BoundingBoxD>, List<MyTuple<bool, int, object>>)](VRageMath.MyDynamicAABBTreeD@GetAproximateClustersForAabbDebug)||
|[GetChildren(int, out int, out int)](VRageMath.MyDynamicAABBTreeD@GetChildren)||
|[GetFatAABB(int, out BoundingBoxD)](VRageMath.MyDynamicAABBTreeD@GetFatAABB)|Get the fat BoundingBox for a proxy.|
|[GetHeight()](VRageMath.MyDynamicAABBTreeD@GetHeight)||
|[GetLeafCount(int)](VRageMath.MyDynamicAABBTreeD@GetLeafCount)||
|[GetNodeLeaves(int, List<int>)](VRageMath.MyDynamicAABBTreeD@GetNodeLeaves)||
|[GetRoot()](VRageMath.MyDynamicAABBTreeD@GetRoot)||
|[GetUserData<T>(int)](VRageMath.MyDynamicAABBTreeD@GetUserData{T})||
|[IsRootNull()](VRageMath.MyDynamicAABBTreeD@IsRootNull)||
|[MoveProxy(int, ref BoundingBoxD, Vector3D)](VRageMath.MyDynamicAABBTreeD@MoveProxy)|Move a proxy with a swepted BoundingBox. If the proxy has moved outside of its fattened BoundingBox, then the proxy is removed from the tree and re-inserted. Otherwise the function returns immediately.|
|[OverlapAllBoundingBox<T>(ref BoundingBoxD, List<T>, uint, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllBoundingBox{T})||
|[OverlapAllBoundingBox<T>(ref MyOrientedBoundingBoxD, List<T>, uint, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllBoundingBox{T})||
|[OverlapAllBoundingSphere<T>(ref BoundingSphereD, List<T>, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllBoundingSphere{T})||
|[OverlapAllBoundingSphere<T>(ref BoundingSphereD, Action<T>)](VRageMath.MyDynamicAABBTreeD@OverlapAllBoundingSphere{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, List<T>, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, List<T>, uint, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, List<T>, List<bool>)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, T)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, List<T>, List<bool>, float, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, Action<T, bool>, float)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustumD, T, float)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustum{T})||
|[OverlapAllFrustumAny<T>(ref BoundingFrustumD, List<T>, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllFrustumAny{T})||
|[OverlapAllLineSegment<T>(ref LineD, List<MyLineSegmentOverlapResult<T>>, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllLineSegment{T})||
|[OverlapAllLineSegment<T>(ref LineD, List<MyLineSegmentOverlapResult<T>>, uint, bool)](VRageMath.MyDynamicAABBTreeD@OverlapAllLineSegment{T})||
|[OverlapsAnyLeafBoundingBox(ref BoundingBoxD)](VRageMath.MyDynamicAABBTreeD@OverlapsAnyLeafBoundingBox)||
|[Query(Func<int, bool>, ref BoundingBoxD)](VRageMath.MyDynamicAABBTreeD@Query)||
|[QueryPoint(Func<int, bool>, ref Vector3D)](VRageMath.MyDynamicAABBTreeD@QueryPoint)||
|[RemoveProxy(int)](VRageMath.MyDynamicAABBTreeD@RemoveProxy)|Destroy a proxy. This asserts if the id is invalid.|

