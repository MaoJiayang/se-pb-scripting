**Assembly:** VRage.Math.dll

```csharp
public struct Rectangle: IEquatable<Rectangle>
```

Defines a rectangle.

## Fields

|Member|Description|
|---|---|
|[Height](VRageMath.Rectangle@Height)|Specifies the height of the rectangle.|
|[Width](VRageMath.Rectangle@Width)|Specifies the width of the rectangle.|
|[X](VRageMath.Rectangle@X)|Specifies the x-coordinate of the rectangle.|
|[Y](VRageMath.Rectangle@Y)|Specifies the y-coordinate of the rectangle.|

## Properties

|Member|Description|
|---|---|
|[Bottom](VRageMath.Rectangle@Bottom)|Returns the y-coordinate of the bottom of the rectangle.|
|[Center](VRageMath.Rectangle@Center)|Gets the Point that specifies the center of the rectangle.|
|[Left](VRageMath.Rectangle@Left)|Returns the x-coordinate of the left side of the rectangle.|
|[Location](VRageMath.Rectangle@Location)|Gets or sets the upper-left value of the Rectangle.|
|[Right](VRageMath.Rectangle@Right)|Returns the x-coordinate of the right side of the rectangle.|
|[Top](VRageMath.Rectangle@Top)|Returns the y-coordinate of the top of the rectangle.|

## Constructors

|Member|Description|
|---|---|
|[Rectangle(int, int, int, int)](VRageMath.Rectangle@.ctor)||

## Methods

|Member|Description|
|---|---|
|[static Intersect(Rectangle, Rectangle)](VRageMath.Rectangle@Intersect)|Creates a Rectangle defining the area where one rectangle overlaps with another rectangle.|
|[static Intersect(ref Rectangle, ref Rectangle, out Rectangle)](VRageMath.Rectangle@Intersect)|Creates a Rectangle defining the area where one rectangle overlaps with another rectangle.|
|[static Union(Rectangle, Rectangle)](VRageMath.Rectangle@Union)|Creates a new Rectangle that exactly contains two other rectangles.|
|[static Union(ref Rectangle, ref Rectangle, out Rectangle)](VRageMath.Rectangle@Union)|Creates a new Rectangle that exactly contains two other rectangles.|
|[Contains(int, int)](VRageMath.Rectangle@Contains)|Determines whether this Rectangle contains a specified point represented by its x- and y-coordinates.|
|[Contains(Point)](VRageMath.Rectangle@Contains)|Determines whether this Rectangle contains a specified Point.|
|[Contains(ref Point, out bool)](VRageMath.Rectangle@Contains)|Determines whether this Rectangle contains a specified Point.|
|[Contains(Rectangle)](VRageMath.Rectangle@Contains)|Determines whether this Rectangle entirely contains a specified Rectangle.|
|[Contains(ref Rectangle, out bool)](VRageMath.Rectangle@Contains)|Determines whether this Rectangle entirely contains a specified Rectangle.|
|[Equals(Rectangle)](VRageMath.Rectangle@Equals)|Determines whether the specified Object is equal to the Rectangle.|
|[Equals(object)](VRageMath.Rectangle@Equals)|Returns a value that indicates whether the current instance is equal to a specified object.|
|[GetHashCode()](VRageMath.Rectangle@GetHashCode)|Gets the hash code for this object.|
|[Inflate(int, int)](VRageMath.Rectangle@Inflate)|Pushes the edges of the Rectangle out by the horizontal and vertical values specified.|
|[Intersects(Rectangle)](VRageMath.Rectangle@Intersects)|Determines whether a specified Rectangle intersects with this Rectangle.|
|[Intersects(ref Rectangle, out bool)](VRageMath.Rectangle@Intersects)|Determines whether a specified Rectangle intersects with this Rectangle.|
|[Offset(Point)](VRageMath.Rectangle@Offset)|Changes the position of the Rectangle.|
|[Offset(int, int)](VRageMath.Rectangle@Offset)|Changes the position of the Rectangle.|
|[ToString()](VRageMath.Rectangle@ToString)|Retrieves a string representation of the current object.|

**Implements:**  
* [IEquatable<Rectangle>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)

