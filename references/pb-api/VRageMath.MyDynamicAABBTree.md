**Assembly:** VRage.Math.dll

```csharp
public class MyDynamicAABBTree
```

Dynamic aabb tree implementation as a prunning structure

## Fields

|Member|Description|
|---|---|
|[static NullNode](VRageMath.MyDynamicAABBTree@NullNode)|A dynamic tree arranges data in a binary tree to accelerate queries such as volume queries and ray casts. Leafs are proxies with an BoundingBox. In the tree we expand the proxy BoundingBox by Settings.b2_fatAABBFactor so that the proxy BoundingBox is bigger than the client object. This allows the client object to move by small amounts without triggering a tree update. Nodes are pooled and relocatable, so we use node indices rather than pointers.|

## Properties

|Member|Description|
|---|---|
|[Leaves](VRageMath.MyDynamicAABBTree@Leaves)||
|[Nodes](VRageMath.MyDynamicAABBTree@Nodes)||

## Constructors

|Member|Description|
|---|---|
|[MyDynamicAABBTree()](VRageMath.MyDynamicAABBTree@.ctor)||
|[MyDynamicAABBTree(Vector3, float)](VRageMath.MyDynamicAABBTree@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Dispose()](VRageMath.MyDynamicAABBTree@Dispose)||
|[AddProxy(ref BoundingBox, object, uint, bool)](VRageMath.MyDynamicAABBTree@AddProxy)|Create a proxy. Provide a tight fitting BoundingBox and a userData pointer.|
|[Balance(int)](VRageMath.MyDynamicAABBTree@Balance)||
|[Clear()](VRageMath.MyDynamicAABBTree@Clear)||
|[CountLeaves(int)](VRageMath.MyDynamicAABBTree@CountLeaves)||
|[GetAabb(int)](VRageMath.MyDynamicAABBTree@GetAabb)||
|[GetAll<T>(List<T>, bool, List<BoundingBox>)](VRageMath.MyDynamicAABBTree@GetAll{T})||
|[GetAllNodeBounds(List<BoundingBox>)](VRageMath.MyDynamicAABBTree@GetAllNodeBounds)||
|[GetChildren(int, out int, out int)](VRageMath.MyDynamicAABBTree@GetChildren)||
|[GetFatAABB(int, out BoundingBox)](VRageMath.MyDynamicAABBTree@GetFatAABB)|Get the fat BoundingBox for a proxy.|
|[GetHeight()](VRageMath.MyDynamicAABBTree@GetHeight)||
|[GetLeafCount()](VRageMath.MyDynamicAABBTree@GetLeafCount)||
|[GetLeafCount(int)](VRageMath.MyDynamicAABBTree@GetLeafCount)||
|[GetNodeLeaves(int, List<int>)](VRageMath.MyDynamicAABBTree@GetNodeLeaves)||
|[GetRoot()](VRageMath.MyDynamicAABBTree@GetRoot)||
|[GetUserData<T>(int)](VRageMath.MyDynamicAABBTree@GetUserData{T})||
|[MoveProxy(int, ref BoundingBox, Vector3)](VRageMath.MyDynamicAABBTree@MoveProxy)|Move a proxy with a swepted BoundingBox. If the proxy has moved outside of its fattened BoundingBox, then the proxy is removed from the tree and re-inserted. Otherwise the function returns immediately.|
|[OverlapAllBoundingBox<T>(ref BoundingBox, List<T>, uint, bool)](VRageMath.MyDynamicAABBTree@OverlapAllBoundingBox{T})||
|[OverlapAllBoundingSphere<T>(ref BoundingSphere, List<T>, bool)](VRageMath.MyDynamicAABBTree@OverlapAllBoundingSphere{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustum, List<T>, bool)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustum, List<T>, uint, bool)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustum, List<T>, List<bool>, bool)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustum, Action<T, bool>)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T, Op>(ref BoundingFrustum, ref Op)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T,Op})||
|[OverlapAllFrustum<T>(ref BoundingFrustum, List<T>, List<bool>, float, bool)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T>(ref BoundingFrustum, Action<T, bool>, float)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T})||
|[OverlapAllFrustum<T, Op>(ref BoundingFrustum, float, ref Op)](VRageMath.MyDynamicAABBTree@OverlapAllFrustum{T,Op})||
|[OverlapAllFrustumAny<T>(ref BoundingFrustum, List<T>, bool)](VRageMath.MyDynamicAABBTree@OverlapAllFrustumAny{T})||
|[OverlapAllFrustumConservative<T>(ref BoundingFrustum, List<T>, uint, bool)](VRageMath.MyDynamicAABBTree@OverlapAllFrustumConservative{T})||
|[OverlapAllLineSegment<T>(ref Line, List<MyLineSegmentOverlapResult<T>>)](VRageMath.MyDynamicAABBTree@OverlapAllLineSegment{T})||
|[OverlapAllLineSegment<T>(ref Line, List<MyLineSegmentOverlapResult<T>>, uint)](VRageMath.MyDynamicAABBTree@OverlapAllLineSegment{T})||
|[OverlapsAnyLeafBoundingBox(ref BoundingBox)](VRageMath.MyDynamicAABBTree@OverlapsAnyLeafBoundingBox)||
|[OverlapSizeableClusters(ref BoundingBox, List<BoundingBox>, double)](VRageMath.MyDynamicAABBTree@OverlapSizeableClusters)||
|[Query(Func<int, bool>, ref BoundingBox)](VRageMath.MyDynamicAABBTree@Query)||
|[RemoveProxy(int)](VRageMath.MyDynamicAABBTree@RemoveProxy)|Destroy a proxy. This asserts if the id is invalid.|

