**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyCryoChamber: IMyCockpit, IMyShipController, IMyTerminalBlock, IMyCubeBlock, IMyEntity, IMyTextSurfaceProvider
```

Describes cryo chamber block (PB scripting interface)

## Properties

|Member|Description|
|---|---|
|[BlockDefinition](VRage.Game.ModAPI.Ingame.IMyCubeBlock@BlockDefinition)|Gets definition.Id assigned to this block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[CanControlShip](Sandbox.ModAPI.Ingame.IMyShipController@CanControlShip)|Determines whether this specific ship controller is capable of controlling the ship it's installed on.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[CenterOfMass](Sandbox.ModAPI.Ingame.IMyShipController@CenterOfMass)|Center of mass in world coordinates<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[Closed](VRage.Game.ModAPI.Ingame.IMyEntity@Closed)|True if the block has been removed from the world.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[Components](VRage.Game.ModAPI.Ingame.IMyEntity@Components)|Gets blocks component logic container<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[ControlThrusters](Sandbox.ModAPI.Ingame.IMyShipController@ControlThrusters)|Gets or sets whether thrusters are being controlled by this controller.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[ControlWheels](Sandbox.ModAPI.Ingame.IMyShipController@ControlWheels)|Gets or sets whether wheels are being controlled by this controller.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[CubeGrid](VRage.Game.ModAPI.Ingame.IMyCubeBlock@CubeGrid)|Grid in which the block is placed<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[CustomData](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomData)|Gets or sets the Custom Data string. NOTE: Only use this for user input. For storing large mod configs, create your own MyModStorageComponent<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[CustomInfo](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomInfo)|Gets information about block status (available from mods) `IMyTerminalBlock.AppendingCustomInfo`<sub>prohibited</sub>  `IMyTerminalBlock.RefreshCustomInfo`<sub>prohibited</sub> .<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[CustomName](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomName)|Gets or sets how block is named in Terminal menu<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[CustomNameWithFaction](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomNameWithFaction)|Gets or sets how block is named in Terminal menu. Work only for Cockpit, LaserAntenna RadioAntenna, SpaceBall, Beacon<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[DampenersOverride](Sandbox.ModAPI.Ingame.IMyShipController@DampenersOverride)|Gets or sets whether dampeners are currently enabled.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[DefinitionDisplayNameText](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DefinitionDisplayNameText)|Definition name<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[DetailedInfo](Sandbox.ModAPI.Ingame.IMyTerminalBlock@DetailedInfo)|Gets information about block status. In Control panel bottom right text<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[DisassembleRatio](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DisassembleRatio)|Is set in definition Ratio at which is the block disassembled (grinding) Bigger values - longer grinding<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[DisplayName](VRage.Game.ModAPI.Ingame.IMyEntity@DisplayName)|Gets user friendly name of entity. May be null For block terminal name use [DisplayNameText](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DisplayNameText)<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[DisplayNameText](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DisplayNameText)|Translated block name<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[EntityId](VRage.Game.ModAPI.Ingame.IMyEntity@EntityId)|Id of entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[HandBrake](Sandbox.ModAPI.Ingame.IMyShipController@HandBrake)|Gets or sets the current state of the handbrake.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[HasInventory](VRage.Game.ModAPI.Ingame.IMyEntity@HasInventory)|Returns true if this entity has got at least one inventory. Note that one aggregate inventory can contain zero simple inventories => zero will be returned even if GetInventory() != null.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[HasWheels](Sandbox.ModAPI.Ingame.IMyShipController@HasWheels)|Determines whether there are any wheels on this ship.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[InventoryCount](VRage.Game.ModAPI.Ingame.IMyEntity@InventoryCount)|Returns the count of the number of inventories this entity has.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[IsBeingHacked](VRage.Game.ModAPI.Ingame.IMyCubeBlock@IsBeingHacked)|Hacking of the block is in progress<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[IsFunctional](VRage.Game.ModAPI.Ingame.IMyCubeBlock@IsFunctional)|Gets if integrity is above breaking threshold<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[IsMainCockpit](Sandbox.ModAPI.Ingame.IMyShipController@IsMainCockpit)|Gets or sets if this controller is the main one for current ship Setter checks if there is any other main cockpit on the ship before proceeding<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[IsUnderControl](Sandbox.ModAPI.Ingame.IMyShipController@IsUnderControl)|Indicates whether a block is locally or remotely controlled.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[IsWorking](VRage.Game.ModAPI.Ingame.IMyCubeBlock@IsWorking)|True if block is able to do its work depening on block type (is functional, powered, enabled, etc...)<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Mass](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Mass)|Block mass<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Max](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Max)|Maximum coordinates of grid cells occupied by this block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Min](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Min)|Minimum coordinates of grid cells occupied by this block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[MoveIndicator](Sandbox.ModAPI.Ingame.IMyShipController@MoveIndicator)|Directional input from user/autopilot. Values can be very large with high controller sensitivity<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[Name](VRage.Game.ModAPI.Ingame.IMyEntity@Name)|Some entities can have uniq name, and game can find them by name `IMyEntities.TryGetEntityByName`<sub>prohibited</sub><br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[NumberInGrid](VRage.Game.ModAPI.Ingame.IMyCubeBlock@NumberInGrid)|Order in which were the blocks of same type added to grid Used in default display name<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Orientation](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Orientation)|Returns block orientation in base 6 directions<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[OwnerId](VRage.Game.ModAPI.Ingame.IMyCubeBlock@OwnerId)|IdentityId of player owning block (not steam Id)<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[OxygenCapacity](Sandbox.ModAPI.Ingame.IMyCockpit@OxygenCapacity)|Gets the maximum oxygen capacity of this cockpit.<br /><br />_Inherited from [IMyCockpit](Sandbox.ModAPI.Ingame.IMyCockpit)_|
|[OxygenFilledRatio](Sandbox.ModAPI.Ingame.IMyCockpit@OxygenFilledRatio)|Gets the current oxygen level of this cockpit, as a value between 0 (empty) and 1 (full).<br /><br />_Inherited from [IMyCockpit](Sandbox.ModAPI.Ingame.IMyCockpit)_|
|[Position](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Position)|Position in grid coordinates<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[RollIndicator](Sandbox.ModAPI.Ingame.IMyShipController@RollIndicator)|Roll input from user/autopilot. Values can be very large with high controller sensitivity<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[RotationIndicator](Sandbox.ModAPI.Ingame.IMyShipController@RotationIndicator)|Pitch, yaw input from user/autopilot. Values can be very large with high controller sensitivity<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[ShowHorizonIndicator](Sandbox.ModAPI.Ingame.IMyShipController@ShowHorizonIndicator)|Gets or sets whether the horizon indicator should be displayed for this block.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[ShowInInventory](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowInInventory)|Represent terminal gui toggle `Show block in Inventory Screen`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShowInTerminal](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowInTerminal)|Represent terminal gui toggle `Show block in terminal`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShowInToolbarConfig](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowInToolbarConfig)|Represent terminal gui toggle `Show in toolbar config`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShowOnHUD](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowOnHUD)|Represent terminal gui toggle `Show On HUD`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[SurfaceCount](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider@SurfaceCount)|Get surfaces count<br /><br />_Inherited from [IMyTextSurfaceProvider](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider)_|
|[UseGenericLcd](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider@UseGenericLcd)|Whether generic LCD terminal controls should be created<br /><br />_Inherited from [IMyTextSurfaceProvider](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider)_|
|[WorldAABB](VRage.Game.ModAPI.Ingame.IMyEntity@WorldAABB)|Gets world axis-aligned bounding box<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldAABBHr](VRage.Game.ModAPI.Ingame.IMyEntity@WorldAABBHr)|Gets world axis-aligned bounding box<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldMatrix](VRage.Game.ModAPI.Ingame.IMyEntity@WorldMatrix)|Gets world matrix of this entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldVolume](VRage.Game.ModAPI.Ingame.IMyEntity@WorldVolume)|Gets bounding sphere of this entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldVolumeHr](VRage.Game.ModAPI.Ingame.IMyEntity@WorldVolumeHr)|Gets bounding sphere of this entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|

## Methods

|Member|Description|
|---|---|
|[CalculateShipMass()](Sandbox.ModAPI.Ingame.IMyShipController@CalculateShipMass)|Gets information about the current mass of the ship.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetActions(List<ITerminalAction>, Func<ITerminalAction, bool>)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetActions)|Get all terminal actions available for block<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetActionWithName(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetActionWithName)|Get first found terminal action with name<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetArtificialGravity()](Sandbox.ModAPI.Ingame.IMyShipController@GetArtificialGravity)|Gets the detected artificial gravity vector and power at the current location.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetInventory()](VRage.Game.ModAPI.Ingame.IMyEntity@GetInventory)|Simply get the MyInventoryBase component stored in this entity.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[GetInventory(int)](VRage.Game.ModAPI.Ingame.IMyEntity@GetInventory)|Search for inventory component with maching index.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[GetNaturalGravity()](Sandbox.ModAPI.Ingame.IMyShipController@GetNaturalGravity)|Gets the detected natural gravity vector and power at the current location.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetOwnerFactionTag()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@GetOwnerFactionTag)|Tag of faction owning block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[GetPosition()](VRage.Game.ModAPI.Ingame.IMyEntity@GetPosition)|Gets position in world coordinates<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[GetProperties(List<ITerminalProperty>, Func<ITerminalProperty, bool>)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetProperties)|Get all terminal actions available for block.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetProperty(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetProperty)|Finds terminal property with provided id<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetShipSpeed()](Sandbox.ModAPI.Ingame.IMyShipController@GetShipSpeed)|Gets the basic ship speed in meters per second, for when you just need to know how fast you're going.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetShipVelocities()](Sandbox.ModAPI.Ingame.IMyShipController@GetShipVelocities)|Determines the linear velocities in meters per second and angular velocities in radians per second. Provides a more accurate representation of the directions and axis speeds.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetSurface(int)](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider@GetSurface)|Get surface by index<br /><br />_Inherited from [IMyTextSurfaceProvider](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider)_|
|[GetTotalGravity()](Sandbox.ModAPI.Ingame.IMyShipController@GetTotalGravity)|Gets the total accumulated gravity vector and power at the current location, taking both natural and artificial gravity into account.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetUserRelationToOwner(long, MyRelationsBetweenPlayerAndBlock)](VRage.Game.ModAPI.Ingame.IMyCubeBlock@GetUserRelationToOwner)|Gets relation to owner of block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[HasLocalPlayerAccess()](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasLocalPlayerAccess)|Returns if local player can use block. Executes [HasPlayerAccess(long, MyRelationsBetweenPlayerAndBlock)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasPlayerAccess) with local player identityId. On Dedicated Server as identityId it is using 0 as playerId<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[HasNobodyPlayerAccessToBlock()](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasNobodyPlayerAccessToBlock)|Returns if Nobody has access to block.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[HasPlayerAccess(long, MyRelationsBetweenPlayerAndBlock)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasPlayerAccess)|Returns if local player can use block. It is also checking for admin access.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[HasPlayerAccessWithNobodyCheck(long, bool)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasPlayerAccessWithNobodyCheck)|Returns if player can use block. If playerId is 0 (Nobody), calls HasNobodyPlayerAccessToBlock instead It is also checking for admin access.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[IsSameConstructAs(IMyTerminalBlock)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@IsSameConstructAs)|Determines whether this block is `Mechanical`<sub>prohibited</sub> connected to the other. This is any block connected with rotors or pistons or other mechanical devices, but not things like connectors. This will in most cases constitute your complete construct.<br /><br />Be aware that using merge blocks combines grids into one, so this function will not filter out grids connected that way. Also be aware that detaching the heads of pistons and rotors will cause this connection to change.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[SearchActionsOfName(string, List<ITerminalAction>, Func<ITerminalAction, bool>)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@SearchActionsOfName)|Get all terminal actions available for block. NOTE: First called `<br /><br />` and then `<br /><br />` check<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[TryGetPlanetElevation(MyPlanetElevation, out double)](Sandbox.ModAPI.Ingame.IMyShipController@TryGetPlanetElevation)|Attempts to get the elevation of the ship in relation to the nearest planet. This method is only available when a ship is within the gravity well of a planet.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[TryGetPlanetPosition(out Vector3D)](Sandbox.ModAPI.Ingame.IMyShipController@TryGetPlanetPosition)|Attempts to get the world position of the nearest planet. This method is only available when a ship is within the gravity well of a planet.<br /><br />_Inherited from [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)_|
|[GetPlayerRelationToOwner()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@GetPlayerRelationToOwner)|_**Obsolete:** GetPlayerRelationToOwner() is useless ingame. Mods should use the one in ModAPI.IMyCubeBlock_<br /><br />Relation of local player to the block Should not be called on Dedicated Server.<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[SetCustomName(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@SetCustomName)|_**Obsolete:** Use the setter of Customname_<br /><br />Obsolete<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[SetCustomName(StringBuilder)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@SetCustomName)|_**Obsolete:** Use the setter of Customname_<br /><br />Obsolete<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[UpdateIsWorking()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@UpdateIsWorking)|_**Obsolete**_<br /><br />Force refresh working state. Call if you change block state that could affect its working status.<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[UpdateVisual()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@UpdateVisual)|_**Obsolete**_<br /><br />Updates block visuals (ie. block emissivity)<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|

**Implements:**  
* [IMyCockpit](Sandbox.ModAPI.Ingame.IMyCockpit)  
* [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)  
* [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)  
* [IMyShipController](Sandbox.ModAPI.Ingame.IMyShipController)  
* [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)  
* [IMyTextSurfaceProvider](Sandbox.ModAPI.Ingame.IMyTextSurfaceProvider)

**Type Definitions:**  
* MyObjectBuilder_CryoChamber/LargeBlockBed  
* MyObjectBuilder_CryoChamber/LargeBlockBedFree  
* MyObjectBuilder_CryoChamber/LargeBlockCryoChamber  
* MyObjectBuilder_CryoChamber/LargeBlockCryoLabVat  
* MyObjectBuilder_CryoChamber/LargeBlockCryoRoom  
* MyObjectBuilder_CryoChamber/LargeBlockHalfBed  
* MyObjectBuilder_CryoChamber/LargeBlockHalfBedOffset  
* MyObjectBuilder_CryoChamber/LargeBlockInsetBed  
* MyObjectBuilder_CryoChamber/SmallBlockBunkBed  
* MyObjectBuilder_CryoChamber/SmallBlockCryoChamber

