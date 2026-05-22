**Assembly:** VRage.Math.dll

```csharp
public struct Color: IPackedVector<uint>, IPackedVector, IEquatable<Color>
```

Represents a four-component color using red, green, blue, and alpha data.

## Fields

|Member|Description|
|---|---|
|PackedValue|Gets the current color as a packed value.|

## Properties

|Member|Description|
|---|---|
|static AliceBlue|Gets a system-defined color with the value R:240 G:248 B:255 A:255.|
|static AntiqueWhite|Gets a system-defined color with the value R:250 G:235 B:215 A:255.|
|static Aqua|Gets a system-defined color with the value R:0 G:255 B:255 A:255.|
|static Aquamarine|Gets a system-defined color with the value R:127 G:255 B:212 A:255.|
|static Azure|Gets a system-defined color with the value R:240 G:255 B:255 A:255.|
|static Beige|Gets a system-defined color with the value R:245 G:245 B:220 A:255.|
|static Bisque|Gets a system-defined color with the value R:255 G:228 B:196 A:255.|
|static Black|Gets a system-defined color with the value R:0 G:0 B:0 A:255.|
|static BlanchedAlmond|Gets a system-defined color with the value R:255 G:235 B:205 A:255.|
|static Blue|Gets a system-defined color with the value R:0 G:0 B:255 A:255.|
|static BlueViolet|Gets a system-defined color with the value R:138 G:43 B:226 A:255.|
|static Brown|Gets a system-defined color with the value R:165 G:42 B:42 A:255.|
|static BurlyWood|Gets a system-defined color with the value R:222 G:184 B:135 A:255.|
|static CadetBlue|Gets a system-defined color with the value R:95 G:158 B:160 A:255.|
|static Chartreuse|Gets a system-defined color with the value R:127 G:255 B:0 A:255.|
|static Chocolate|Gets a system-defined color with the value R:210 G:105 B:30 A:255.|
|static Coral|Gets a system-defined color with the value R:255 G:127 B:80 A:255.|
|static CornflowerBlue|Gets a system-defined color with the value R:100 G:149 B:237 A:255.|
|static Cornsilk|Gets a system-defined color with the value R:255 G:248 B:220 A:255.|
|static Crimson|Gets a system-defined color with the value R:220 G:20 B:60 A:255.|
|static Cyan|Gets a system-defined color with the value R:0 G:255 B:255 A:255.|
|static DarkBlue|Gets a system-defined color with the value R:0 G:0 B:139 A:255.|
|static DarkCyan|Gets a system-defined color with the value R:0 G:139 B:139 A:255.|
|static DarkGoldenrod|Gets a system-defined color with the value R:184 G:134 B:11 A:255.|
|static DarkGray|Gets a system-defined color with the value R:169 G:169 B:169 A:255.|
|static DarkGreen|Gets a system-defined color with the value R:0 G:100 B:0 A:255.|
|static DarkKhaki|Gets a system-defined color with the value R:189 G:183 B:107 A:255.|
|static DarkMagenta|Gets a system-defined color with the value R:139 G:0 B:139 A:255.|
|static DarkOliveGreen|Gets a system-defined color with the value R:85 G:107 B:47 A:255.|
|static DarkOrange|Gets a system-defined color with the value R:255 G:140 B:0 A:255.|
|static DarkOrchid|Gets a system-defined color with the value R:153 G:50 B:204 A:255.|
|static DarkRed|Gets a system-defined color with the value R:139 G:0 B:0 A:255.|
|static DarkSalmon|Gets a system-defined color with the value R:233 G:150 B:122 A:255.|
|static DarkSeaGreen|Gets a system-defined color with the value R:143 G:188 B:139 A:255.|
|static DarkSlateBlue|Gets a system-defined color with the value R:72 G:61 B:139 A:255.|
|static DarkSlateGray|Gets a system-defined color with the value R:47 G:79 B:79 A:255.|
|static DarkTurquoise|Gets a system-defined color with the value R:0 G:206 B:209 A:255.|
|static DarkViolet|Gets a system-defined color with the value R:148 G:0 B:211 A:255.|
|static DeepPink|Gets a system-defined color with the value R:255 G:20 B:147 A:255.|
|static DeepSkyBlue|Gets a system-defined color with the value R:0 G:191 B:255 A:255.|
|static DimGray|Gets a system-defined color with the value R:105 G:105 B:105 A:255.|
|static DodgerBlue|Gets a system-defined color with the value R:30 G:144 B:255 A:255.|
|static Firebrick|Gets a system-defined color with the value R:178 G:34 B:34 A:255.|
|static FloralWhite|Gets a system-defined color with the value R:255 G:250 B:240 A:255.|
|static ForestGreen|Gets a system-defined color with the value R:34 G:139 B:34 A:255.|
|static Fuchsia|Gets a system-defined color with the value R:255 G:0 B:255 A:255.|
|static Gainsboro|Gets a system-defined color with the value R:220 G:220 B:220 A:255.|
|static GhostWhite|Gets a system-defined color with the value R:248 G:248 B:255 A:255.|
|static Gold|Gets a system-defined color with the value R:255 G:215 B:0 A:255.|
|static Goldenrod|Gets a system-defined color with the value R:218 G:165 B:32 A:255.|
|static Gray|Gets a system-defined color with the value R:128 G:128 B:128 A:255.|
|static Green|Gets a system-defined color with the value R:0 G:128 B:0 A:255.|
|static GreenYellow|Gets a system-defined color with the value R:173 G:255 B:47 A:255.|
|static Honeydew|Gets a system-defined color with the value R:240 G:255 B:240 A:255.|
|static HotPink|Gets a system-defined color with the value R:255 G:105 B:180 A:255.|
|static IndianRed|Gets a system-defined color with the value R:205 G:92 B:92 A:255.|
|static Indigo|Gets a system-defined color with the value R:75 G:0 B:130 A:255.|
|static Ivory|Gets a system-defined color with the value R:255 G:255 B:240 A:255.|
|static Khaki|Gets a system-defined color with the value R:240 G:230 B:140 A:255.|
|static Lavender|Gets a system-defined color with the value R:230 G:230 B:250 A:255.|
|static LavenderBlush|Gets a system-defined color with the value R:255 G:240 B:245 A:255.|
|static LawnGreen|Gets a system-defined color with the value R:124 G:252 B:0 A:255.|
|static LemonChiffon|Gets a system-defined color with the value R:255 G:250 B:205 A:255.|
|static LightBlue|Gets a system-defined color with the value R:173 G:216 B:230 A:255.|
|static LightCoral|Gets a system-defined color with the value R:240 G:128 B:128 A:255.|
|static LightCyan|Gets a system-defined color with the value R:224 G:255 B:255 A:255.|
|static LightGoldenrodYellow|Gets a system-defined color with the value R:250 G:250 B:210 A:255.|
|static LightGray|Gets a system-defined color with the value R:211 G:211 B:211 A:255.|
|static LightGreen|Gets a system-defined color with the value R:144 G:238 B:144 A:255.|
|static LightPink|Gets a system-defined color with the value R:255 G:182 B:193 A:255.|
|static LightSalmon|Gets a system-defined color with the value R:255 G:160 B:122 A:255.|
|static LightSeaGreen|Gets a system-defined color with the value R:32 G:178 B:170 A:255.|
|static LightSkyBlue|Gets a system-defined color with the value R:135 G:206 B:250 A:255.|
|static LightSlateGray|Gets a system-defined color with the value R:119 G:136 B:153 A:255.|
|static LightSteelBlue|Gets a system-defined color with the value R:176 G:196 B:222 A:255.|
|static LightYellow|Gets a system-defined color with the value R:255 G:255 B:224 A:255.|
|static Lime|Gets a system-defined color with the value R:0 G:255 B:0 A:255.|
|static LimeGreen|Gets a system-defined color with the value R:50 G:205 B:50 A:255.|
|static Linen|Gets a system-defined color with the value R:250 G:240 B:230 A:255.|
|static Magenta|Gets a system-defined color with the value R:255 G:0 B:255 A:255.|
|static Maroon|Gets a system-defined color with the value R:128 G:0 B:0 A:255.|
|static MediumAquamarine|Gets a system-defined color with the value R:102 G:205 B:170 A:255.|
|static MediumBlue|Gets a system-defined color with the value R:0 G:0 B:205 A:255.|
|static MediumOrchid|Gets a system-defined color with the value R:186 G:85 B:211 A:255.|
|static MediumPurple|Gets a system-defined color with the value R:147 G:112 B:219 A:255.|
|static MediumSeaGreen|Gets a system-defined color with the value R:60 G:179 B:113 A:255.|
|static MediumSlateBlue|Gets a system-defined color with the value R:123 G:104 B:238 A:255.|
|static MediumSpringGreen|Gets a system-defined color with the value R:0 G:250 B:154 A:255.|
|static MediumTurquoise|Gets a system-defined color with the value R:72 G:209 B:204 A:255.|
|static MediumVioletRed|Gets a system-defined color with the value R:199 G:21 B:133 A:255.|
|static MidnightBlue|Gets a system-defined color with the value R:25 G:25 B:112 A:255.|
|static MintCream|Gets a system-defined color with the value R:245 G:255 B:250 A:255.|
|static MistyRose|Gets a system-defined color with the value R:255 G:228 B:225 A:255.|
|static Moccasin|Gets a system-defined color with the value R:255 G:228 B:181 A:255.|
|static NavajoWhite|Gets a system-defined color with the value R:255 G:222 B:173 A:255.|
|static Navy|Gets a system-defined color R:0 G:0 B:128 A:255.|
|static OldLace|Gets a system-defined color with the value R:253 G:245 B:230 A:255.|
|static Olive|Gets a system-defined color with the value R:128 G:128 B:0 A:255.|
|static OliveDrab|Gets a system-defined color with the value R:107 G:142 B:35 A:255.|
|static Orange|Gets a system-defined color with the value R:255 G:165 B:0 A:255.|
|static OrangeRed|Gets a system-defined color with the value R:255 G:69 B:0 A:255.|
|static Orchid|Gets a system-defined color with the value R:218 G:112 B:214 A:255.|
|static PaleGoldenrod|Gets a system-defined color with the value R:238 G:232 B:170 A:255.|
|static PaleGreen|Gets a system-defined color with the value R:152 G:251 B:152 A:255.|
|static PaleTurquoise|Gets a system-defined color with the value R:175 G:238 B:238 A:255.|
|static PaleVioletRed|Gets a system-defined color with the value R:219 G:112 B:147 A:255.|
|static PapayaWhip|Gets a system-defined color with the value R:255 G:239 B:213 A:255.|
|static PeachPuff|Gets a system-defined color with the value R:255 G:218 B:185 A:255.|
|static Peru|Gets a system-defined color with the value R:205 G:133 B:63 A:255.|
|static Pink|Gets a system-defined color with the value R:255 G:192 B:203 A:255.|
|static Plum|Gets a system-defined color with the value R:221 G:160 B:221 A:255.|
|static PowderBlue|Gets a system-defined color with the value R:176 G:224 B:230 A:255.|
|static Purple|Gets a system-defined color with the value R:128 G:0 B:128 A:255.|
|static Red|Gets a system-defined color with the value R:255 G:0 B:0 A:255.|
|static RosyBrown|Gets a system-defined color with the value R:188 G:143 B:143 A:255.|
|static RoyalBlue|Gets a system-defined color with the value R:65 G:105 B:225 A:255.|
|static SaddleBrown|Gets a system-defined color with the value R:139 G:69 B:19 A:255.|
|static Salmon|Gets a system-defined color with the value R:250 G:128 B:114 A:255.|
|static SandyBrown|Gets a system-defined color with the value R:244 G:164 B:96 A:255.|
|static SeaGreen|Gets a system-defined color with the value R:46 G:139 B:87 A:255.|
|static SeaShell|Gets a system-defined color with the value R:255 G:245 B:238 A:255.|
|static Sienna|Gets a system-defined color with the value R:160 G:82 B:45 A:255.|
|static Silver|Gets a system-defined color with the value R:192 G:192 B:192 A:255.|
|static SkyBlue|Gets a system-defined color with the value R:135 G:206 B:235 A:255.|
|static SlateBlue|Gets a system-defined color with the value R:106 G:90 B:205 A:255.|
|static SlateGray|Gets a system-defined color with the value R:112 G:128 B:144 A:255.|
|static Snow|Gets a system-defined color with the value R:255 G:250 B:250 A:255.|
|static SpringGreen|Gets a system-defined color with the value R:0 G:255 B:127 A:255.|
|static SteelBlue|Gets a system-defined color with the value R:70 G:130 B:180 A:255.|
|static Tan|Gets a system-defined color with the value R:210 G:180 B:140 A:255.|
|static Teal|Gets a system-defined color with the value R:0 G:128 B:128 A:255.|
|static Thistle|Gets a system-defined color with the value R:216 G:191 B:216 A:255.|
|static Tomato|Gets a system-defined color with the value R:255 G:99 B:71 A:255.|
|static Transparent|Gets a system-defined color with the value R:0 G:0 B:0 A:0.|
|static Turquoise|Gets a system-defined color with the value R:64 G:224 B:208 A:255.|
|static Violet|Gets a system-defined color with the value R:238 G:130 B:238 A:255.|
|static Wheat|Gets a system-defined color with the value R:245 G:222 B:179 A:255.|
|static White|Gets a system-defined color with the value R:255 G:255 B:255 A:255.|
|static WhiteSmoke|Gets a system-defined color with the value R:245 G:245 B:245 A:255.|
|static Yellow|Gets a system-defined color with the value R:255 G:255 B:0 A:255.|
|static YellowGreen|Gets a system-defined color with the value R:154 G:205 B:50 A:255.|
|A|Gets or sets the alpha component value.|
|B|Gets or sets the blue component value of this Color.|
|G|Gets or sets the green component value of this Color.|
|R|Gets or sets the red component value of this Color.|
|X|Gets or sets the red component value of this Color.|
|Y|Gets or sets the green component value of this Color.|
|Z|Gets or sets the blue component value of this Color.|

## Constructors

|Member|Description|
|---|---|
|Color(uint)||
|Color(int, int, int)||
|Color(int, int, int, int)||
|Color(float)||
|Color(float, float, float)||
|Color(float, float, float, float)||
|Color(Color, float)||
|Color(Vector3)||
|Color(Vector4)||

## Methods

|Member|Description|
|---|---|
|static Darken(Color, double)||
|static FromNonPremultiplied(Vector4)|Convert a non premultipled color into color data that contains alpha.|
|static FromNonPremultiplied(int, int, int, int)|Converts a non-premultipled alpha color to a color that contains premultiplied alpha.|
|static Lerp(Color, Color, float)|Linearly interpolate a color.|
|static Lighten(Color, double)||
|static Multiply(Color, float)|Multiply each color component by the scale factor.|
|Equals(object)|Test an instance of a color object to see if it is equal to this object.|
|Equals(Color)|Test a color to see if it is equal to the color in this instance.|
|GetHashCode()|Serves as a hash function for a particular type.|
|ToGray()||
|ToString()|Gets a string representation of this object.|
|ToVector3()|Gets a three-component vector representation for this object.|
|ToVector4()|Gets a four-component vector representation for this object.|

**Implements:**  
* [IEquatable<Color>](https://docs.microsoft.com/en-us/dotnet/api/System.IEquatable-1?view=netframework-4.6)  
* IPackedVector <sub>prohibited</sub>  
* IPackedVector<uint> <sub>prohibited</sub>

