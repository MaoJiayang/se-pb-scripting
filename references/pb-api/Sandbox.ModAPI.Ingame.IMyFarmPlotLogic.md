**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyFarmPlotLogic
```

Describes the exposed farm plot logic (PB scripting interface).

## Properties

|Member|Description|
|---|---|
|[AmountOfSeedsRequired](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@AmountOfSeedsRequired)|The amount of seeds that are needed to start growing a plant at this farm plot.|
|[IsAlive](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@IsAlive)|Whether the plant is alive.|
|[IsHarvestable](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@IsHarvestable)|Whether the plant can be harvested. By default, the block is harvestable if it contains a plant that is fully grown or dead.|
|[IsPlantFullyGrown](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@IsPlantFullyGrown)|Whether the plant is fully grown.|
|[IsPlantPlanted](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@IsPlantPlanted)|Whether a plant is planted, dead or alive.|
|[OutputItem](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@OutputItem)|The item that the currently planted seed will produce when fully grown.|
|[OutputItemAmount](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@OutputItemAmount)|The amount of items that the currently planted seed will produce when fully grown. Returns 0 if the plant is not yet fully grown.|

## Methods

|Member|Description|
|---|---|
|[GetDetailedInfoWithoutRequiredInput()](Sandbox.ModAPI.Ingame.IMyFarmPlotLogic@GetDetailedInfoWithoutRequiredInput)|Obtains detailed info that does not include the required power input. Used by the plant management screen.|

