**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyTextSurface
```

Describes one of block LCDs where you can write text or draw things (PB scripting interface)

## Properties

|Member|Description|
|---|---|
|[Alignment](Sandbox.ModAPI.Ingame.IMyTextSurface@Alignment)|How should the text be aligned|
|[BackgroundAlpha](Sandbox.ModAPI.Ingame.IMyTextSurface@BackgroundAlpha)|Value for offscreen texture alpha channel - for PBR material it is metalness (should be 0) - for transparent texture it is opacity|
|[BackgroundColor](Sandbox.ModAPI.Ingame.IMyTextSurface@BackgroundColor)|Gets or sets background color|
|[ChangeInterval](Sandbox.ModAPI.Ingame.IMyTextSurface@ChangeInterval)|Gets or sets the change interval for selected textures|
|[ContentType](Sandbox.ModAPI.Ingame.IMyTextSurface@ContentType)|Type of content to be displayed on the screen.|
|[CurrentlyShownImage](Sandbox.ModAPI.Ingame.IMyTextSurface@CurrentlyShownImage)|Gets image that is currently shown on the screen. Returns NULL if there are no images selected OR the screen is in text mode.|
|[DisplayName](Sandbox.ModAPI.Ingame.IMyTextSurface@DisplayName)|Get localized name of this surface.|
|[Font](Sandbox.ModAPI.Ingame.IMyTextSurface@Font)|Gets or sets the font|
|[FontColor](Sandbox.ModAPI.Ingame.IMyTextSurface@FontColor)|Gets or sets font color|
|[FontSize](Sandbox.ModAPI.Ingame.IMyTextSurface@FontSize)|Gets or sets font size|
|[Name](Sandbox.ModAPI.Ingame.IMyTextSurface@Name)|Gets identifier name of this surface.|
|[PreserveAspectRatio](Sandbox.ModAPI.Ingame.IMyTextSurface@PreserveAspectRatio)|Gets or sets preserve aspect ratio of images.|
|[Script](Sandbox.ModAPI.Ingame.IMyTextSurface@Script)|Currently running script|
|[ScriptBackgroundColor](Sandbox.ModAPI.Ingame.IMyTextSurface@ScriptBackgroundColor)|Gets or sets background color used for scripts.|
|[ScriptForegroundColor](Sandbox.ModAPI.Ingame.IMyTextSurface@ScriptForegroundColor)|Gets or sets foreground color used for scripts.|
|[SurfaceSize](Sandbox.ModAPI.Ingame.IMyTextSurface@SurfaceSize)|Gets size of the drawing surface.|
|[TextPadding](Sandbox.ModAPI.Ingame.IMyTextSurface@TextPadding)|Gets or sets text padding from all sides of the panel.|
|[TextureSize](Sandbox.ModAPI.Ingame.IMyTextSurface@TextureSize)|Gets size of the texture the drawing surface is rendered to.|

## Methods

|Member|Description|
|---|---|
|[AddImagesToSelection(List<string>, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@AddImagesToSelection)|Adds image to list of shown images. You can get image ids by [GetSelectedImages(List<string>)](Sandbox.ModAPI.Ingame.IMyTextSurface@GetSelectedImages) |
|[AddImageToSelection(string, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@AddImageToSelection)|Adds image to list of shown images. You can get image ids by [GetSelectedImages(List<string>)](Sandbox.ModAPI.Ingame.IMyTextSurface@GetSelectedImages) |
|[ClearImagesFromSelection()](Sandbox.ModAPI.Ingame.IMyTextSurface@ClearImagesFromSelection)|Removes images from shown images.|
|[DrawFrame()](Sandbox.ModAPI.Ingame.IMyTextSurface@DrawFrame)|Creates a new draw frame where you can add sprites to be rendered.|
|[GetFonts(List<string>)](Sandbox.ModAPI.Ingame.IMyTextSurface@GetFonts)|Gets a list of available fonts|
|[GetScripts(List<string>)](Sandbox.ModAPI.Ingame.IMyTextSurface@GetScripts)|Gets a list of available scripts|
|[GetSelectedImages(List<string>)](Sandbox.ModAPI.Ingame.IMyTextSurface@GetSelectedImages)|Outputs the selected image ids to the specified list. NOTE: List is not cleared internally.|
|[GetSprites(List<string>)](Sandbox.ModAPI.Ingame.IMyTextSurface@GetSprites)|Gets a list of available sprites|
|[GetText()](Sandbox.ModAPI.Ingame.IMyTextSurface@GetText)|Gets current text that is written on surface. Allocates memory (StringBuilder.ToString())! This method doesn't allocate memory [ReadText(StringBuilder, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@ReadText) |
|[MeasureStringInPixels(StringBuilder, string, float)](Sandbox.ModAPI.Ingame.IMyTextSurface@MeasureStringInPixels)|Calculates how many pixels a string of a given font and scale will take up.|
|[ReadText(StringBuilder, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@ReadText)|Gets current text that is written on surface.|
|[RemoveImageFromSelection(string, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@RemoveImageFromSelection)|Removes image from shown images.|
|[RemoveImagesFromSelection(List<string>, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@RemoveImagesFromSelection)|Removes images from shown images.|
|[WriteText(string, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@WriteText)|Writes text to surface. If somebody opened LCD text in popup dialog, text can no longer be added to the surface. Resulting text must is capped with 100000 symbols|
|[WriteText(StringBuilder, bool)](Sandbox.ModAPI.Ingame.IMyTextSurface@WriteText)|Writes text to surface. If somebody opened LCD text in popup dialog, text can no longer be added to the surface. Resulting text must is capped with 100000 symbols|

**Inheritors:**  
* [IMyTextPanel](Sandbox.ModAPI.Ingame.IMyTextPanel)

**Type Definitions:**  
* MyObjectBuilder_TextPanel/HoloLCDLarge  
* MyObjectBuilder_TextPanel/HoloLCDSmall  
* MyObjectBuilder_TextPanel/LargeBlockCorner_LCD_1  
* MyObjectBuilder_TextPanel/LargeBlockCorner_LCD_2  
* MyObjectBuilder_TextPanel/LargeBlockCorner_LCD_Flat_1  
* MyObjectBuilder_TextPanel/LargeBlockCorner_LCD_Flat_2  
* MyObjectBuilder_TextPanel/LargeCurvedLCDPanel  
* MyObjectBuilder_TextPanel/LargeDiagonalLCDPanel  
* MyObjectBuilder_TextPanel/LargeFullBlockLCDPanel  
* MyObjectBuilder_TextPanel/LargeLCDPanel  
* MyObjectBuilder_TextPanel/LargeLCDPanel3x3  
* MyObjectBuilder_TextPanel/LargeLCDPanel5x3  
* MyObjectBuilder_TextPanel/LargeLCDPanel5x5  
* MyObjectBuilder_TextPanel/LargeLCDPanelWide  
* MyObjectBuilder_TextPanel/LargeTextPanel  
* MyObjectBuilder_TextPanel/SmallBlockConsoleModuleScreens  
* MyObjectBuilder_TextPanel/SmallBlockCorner_LCD_1  
* MyObjectBuilder_TextPanel/SmallBlockCorner_LCD_2  
* MyObjectBuilder_TextPanel/SmallBlockCorner_LCD_Flat_1  
* MyObjectBuilder_TextPanel/SmallBlockCorner_LCD_Flat_2  
* MyObjectBuilder_TextPanel/SmallCurvedLCDPanel  
* MyObjectBuilder_TextPanel/SmallDiagonalLCDPanel  
* MyObjectBuilder_TextPanel/SmallFullBlockLCDPanel  
* MyObjectBuilder_TextPanel/SmallLCDPanel  
* MyObjectBuilder_TextPanel/SmallLCDPanelWide  
* MyObjectBuilder_TextPanel/SmallTextPanel  
* MyObjectBuilder_TextPanel/TransparentLCDLarge  
* MyObjectBuilder_TextPanel/TransparentLCDSmall

