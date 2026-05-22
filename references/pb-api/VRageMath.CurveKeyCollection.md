**Assembly:** VRage.Math.dll

```csharp
public class CurveKeyCollection: ICollection<CurveKey>, IEnumerable<CurveKey>, IEnumerable
```

Contains the CurveKeys making up a Curve.

## Properties

|Member|Description|
|---|---|
|[Count](VRageMath.CurveKeyCollection@Count)|Gets the number of elements contained in the CurveKeyCollection.|
|[IsReadOnly](VRageMath.CurveKeyCollection@IsReadOnly)|Returns a value indicating whether the CurveKeyCollection is read-only.|
|[Item](VRageMath.CurveKeyCollection@Item)||

## Constructors

|Member|Description|
|---|---|
|[CurveKeyCollection()](VRageMath.CurveKeyCollection@.ctor)||

## Methods

|Member|Description|
|---|---|
|[Add(object)](VRageMath.CurveKeyCollection@Add)||
|[Add(CurveKey)](VRageMath.CurveKeyCollection@Add)|Adds a CurveKey to the CurveKeyCollection.|
|[Clear()](VRageMath.CurveKeyCollection@Clear)|Removes all CurveKeys from the CurveKeyCollection.|
|[Clone()](VRageMath.CurveKeyCollection@Clone)|Creates a copy of the CurveKeyCollection.|
|[Contains(CurveKey)](VRageMath.CurveKeyCollection@Contains)|Determines whether the CurveKeyCollection contains a specific CurveKey.|
|[CopyTo(CurveKey[], int)](VRageMath.CurveKeyCollection@CopyTo)|Copies the CurveKeys of the CurveKeyCollection to an array, starting at the array index provided.|
|[GetEnumerator()](VRageMath.CurveKeyCollection@GetEnumerator)|Returns an enumerator that iterates through the CurveKeyCollection.|
|[IndexOf(CurveKey)](VRageMath.CurveKeyCollection@IndexOf)|Determines the index of a CurveKey in the CurveKeyCollection.|
|[Remove(CurveKey)](VRageMath.CurveKeyCollection@Remove)|Removes the first occurrence of a specific CurveKey from the CurveKeyCollection.|
|[RemoveAt(int)](VRageMath.CurveKeyCollection@RemoveAt)|Removes the CurveKey at the specified index.|

**Implements:**  
* [ICollection<CurveKey>](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1?view=netframework-4.6)  
* [IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable?view=netframework-4.6)  
* [IEnumerable<CurveKey>](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1?view=netframework-4.6)

