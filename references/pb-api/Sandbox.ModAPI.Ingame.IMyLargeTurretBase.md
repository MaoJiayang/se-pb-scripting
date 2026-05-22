**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyLargeTurretBase: IMyUserControllableGun, IMyFunctionalBlock, IMyTerminalBlock, IMyCubeBlock, IMyEntity
```

Describes turret block (PB scripting interface)

## Properties

|Member|Description|
|---|---|
|[AIEnabled](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@AIEnabled)|Checks is AI is enabled for turret|
|[Azimuth](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@Azimuth)|Gets or sets azimuth of turret, this method is not synced, you need to sync azimuth manually|
|[CanControl](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@CanControl)|Returns true if current player can control this block. Always return false on Dedicated Server|
|[Elevation](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@Elevation)|Gets / sets elevation of turret, this method is not synced, you need to sync elevation manually|
|[EnableIdleRotation](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@EnableIdleRotation)|Enable/disable idle rotation for turret, this method is not synced, you need to sync manually|
|[HasTarget](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@HasTarget)|Checks if the turret is locked onto a target|
|[IsAimed](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@IsAimed)|Returns true if turret head looking at target|
|[IsUnderControl](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@IsUnderControl)|Indicates whether a block is locally or remotely controlled.|
|[Range](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@Range)|Gets and Sets shooting range of the turret|
|[TargetCharacters](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetCharacters)|Gets/sets if the turret should target characters.|
|[TargetEnemies](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetEnemies)|Gets/sets if the turret should target enemies.|
|[TargetLargeGrids](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetLargeGrids)|Gets/sets if the turret should target large grids.|
|[TargetMeteors](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetMeteors)|Gets/sets if the turret should target meteors.|
|[TargetMissiles](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetMissiles)|Gets/sets if the turret should target missiles.|
|[TargetNeutrals](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetNeutrals)|Gets/sets if the turret should target neutrals.|
|[TargetSmallGrids](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetSmallGrids)|Gets/sets if the turret should target small grids.|
|[TargetStations](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TargetStations)|Gets/sets if the turret should target stations.|
|[BlockDefinition](VRage.Game.ModAPI.Ingame.IMyCubeBlock@BlockDefinition)|Gets definition.Id assigned to this block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Closed](VRage.Game.ModAPI.Ingame.IMyEntity@Closed)|True if the block has been removed from the world.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[Components](VRage.Game.ModAPI.Ingame.IMyEntity@Components)|Gets blocks component logic container<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[CubeGrid](VRage.Game.ModAPI.Ingame.IMyCubeBlock@CubeGrid)|Grid in which the block is placed<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[CustomData](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomData)|Gets or sets the Custom Data string. NOTE: Only use this for user input. For storing large mod configs, create your own MyModStorageComponent<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[CustomInfo](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomInfo)|Gets information about block status (available from mods) `IMyTerminalBlock.AppendingCustomInfo`<sub>prohibited</sub>  `IMyTerminalBlock.RefreshCustomInfo`<sub>prohibited</sub> .<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[CustomName](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomName)|Gets or sets how block is named in Terminal menu<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[CustomNameWithFaction](Sandbox.ModAPI.Ingame.IMyTerminalBlock@CustomNameWithFaction)|Gets or sets how block is named in Terminal menu. Work only for Cockpit, LaserAntenna RadioAntenna, SpaceBall, Beacon<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[DefinitionDisplayNameText](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DefinitionDisplayNameText)|Definition name<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[DetailedInfo](Sandbox.ModAPI.Ingame.IMyTerminalBlock@DetailedInfo)|Gets information about block status. In Control panel bottom right text<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[DisassembleRatio](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DisassembleRatio)|Is set in definition Ratio at which is the block disassembled (grinding) Bigger values - longer grinding<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[DisplayName](VRage.Game.ModAPI.Ingame.IMyEntity@DisplayName)|Gets user friendly name of entity. May be null For block terminal name use [DisplayNameText](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DisplayNameText)<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[DisplayNameText](VRage.Game.ModAPI.Ingame.IMyCubeBlock@DisplayNameText)|Translated block name<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Enabled](Sandbox.ModAPI.Ingame.IMyFunctionalBlock@Enabled)|Represents terminal gui toggle. Gets or sets if block is Enabled<br /><br />_Inherited from [IMyFunctionalBlock](Sandbox.ModAPI.Ingame.IMyFunctionalBlock)_|
|[EntityId](VRage.Game.ModAPI.Ingame.IMyEntity@EntityId)|Id of entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[HasInventory](VRage.Game.ModAPI.Ingame.IMyEntity@HasInventory)|Returns true if this entity has got at least one inventory. Note that one aggregate inventory can contain zero simple inventories => zero will be returned even if GetInventory() != null.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[InventoryCount](VRage.Game.ModAPI.Ingame.IMyEntity@InventoryCount)|Returns the count of the number of inventories this entity has.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[IsBeingHacked](VRage.Game.ModAPI.Ingame.IMyCubeBlock@IsBeingHacked)|Hacking of the block is in progress<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[IsFunctional](VRage.Game.ModAPI.Ingame.IMyCubeBlock@IsFunctional)|Gets if integrity is above breaking threshold<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[IsShooting](Sandbox.ModAPI.Ingame.IMyUserControllableGun@IsShooting)|Gets whether block is shooting<br /><br />_Inherited from [IMyUserControllableGun](Sandbox.ModAPI.Ingame.IMyUserControllableGun)_|
|[IsWorking](VRage.Game.ModAPI.Ingame.IMyCubeBlock@IsWorking)|True if block is able to do its work depening on block type (is functional, powered, enabled, etc...)<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Mass](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Mass)|Block mass<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Max](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Max)|Maximum coordinates of grid cells occupied by this block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Min](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Min)|Minimum coordinates of grid cells occupied by this block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Name](VRage.Game.ModAPI.Ingame.IMyEntity@Name)|Some entities can have uniq name, and game can find them by name `IMyEntities.TryGetEntityByName`<sub>prohibited</sub><br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[NumberInGrid](VRage.Game.ModAPI.Ingame.IMyCubeBlock@NumberInGrid)|Order in which were the blocks of same type added to grid Used in default display name<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Orientation](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Orientation)|Returns block orientation in base 6 directions<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[OwnerId](VRage.Game.ModAPI.Ingame.IMyCubeBlock@OwnerId)|IdentityId of player owning block (not steam Id)<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Position](VRage.Game.ModAPI.Ingame.IMyCubeBlock@Position)|Position in grid coordinates<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[Shoot](Sandbox.ModAPI.Ingame.IMyUserControllableGun@Shoot)|Represents terminal gui toggle element "Shoot". Not same as [IsShooting](Sandbox.ModAPI.Ingame.IMyUserControllableGun@IsShooting)<br /><br />_Inherited from [IMyUserControllableGun](Sandbox.ModAPI.Ingame.IMyUserControllableGun)_|
|[ShowInInventory](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowInInventory)|Represent terminal gui toggle `Show block in Inventory Screen`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShowInTerminal](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowInTerminal)|Represent terminal gui toggle `Show block in terminal`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShowInToolbarConfig](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowInToolbarConfig)|Represent terminal gui toggle `Show in toolbar config`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShowOnHUD](Sandbox.ModAPI.Ingame.IMyTerminalBlock@ShowOnHUD)|Represent terminal gui toggle `Show On HUD`. Gets or sets its value<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[WorldAABB](VRage.Game.ModAPI.Ingame.IMyEntity@WorldAABB)|Gets world axis-aligned bounding box<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldAABBHr](VRage.Game.ModAPI.Ingame.IMyEntity@WorldAABBHr)|Gets world axis-aligned bounding box<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldMatrix](VRage.Game.ModAPI.Ingame.IMyEntity@WorldMatrix)|Gets world matrix of this entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldVolume](VRage.Game.ModAPI.Ingame.IMyEntity@WorldVolume)|Gets bounding sphere of this entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[WorldVolumeHr](VRage.Game.ModAPI.Ingame.IMyEntity@WorldVolumeHr)|Gets bounding sphere of this entity<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|

## Methods

|Member|Description|
|---|---|
|[GetTargetedEntity()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@GetTargetedEntity)|Gets the turret's current detected entity, if any|
|[GetTargetingGroup()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@GetTargetingGroup)|Gets current targeting group|
|[GetTargetingGroups(List<string>)](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@GetTargetingGroups)|Gets all available targeting groups|
|[ResetTargetingToDefault()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@ResetTargetingToDefault)|Resets targeting to default values|
|[SetManualAzimuthAndElevation(float, float)](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@SetManualAzimuthAndElevation)|Sets azimuth and elevation of the turret, this method is not synced, you need to sync it manually. Call SyncAzimuth or SyncElevation.|
|[SetTarget(Vector3D)](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@SetTarget)|Set targets given position|
|[SetTargetingGroup(string)](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@SetTargetingGroup)|Sets current targeting group|
|[SyncAzimuth()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@SyncAzimuth)|Method used to sync azimuth, you need to call it to sync azimuth for other clients/server|
|[SyncElevation()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@SyncElevation)|Method used to sync elevation of turret, you need to call it to sync elevation for other clients/server|
|[SyncEnableIdleRotation()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@SyncEnableIdleRotation)|Method used to sync idle rotation and elevation, you need to call it to sync rotation and elevation for other clients/server|
|[TrackTarget(Vector3D, Vector3)](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@TrackTarget)|Tracks given target with enabled position prediction|
|[GetActions(List<ITerminalAction>, Func<ITerminalAction, bool>)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetActions)|Get all terminal actions available for block<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetActionWithName(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetActionWithName)|Get first found terminal action with name<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetInventory()](VRage.Game.ModAPI.Ingame.IMyEntity@GetInventory)|Simply get the MyInventoryBase component stored in this entity.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[GetInventory(int)](VRage.Game.ModAPI.Ingame.IMyEntity@GetInventory)|Search for inventory component with maching index.<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[GetOwnerFactionTag()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@GetOwnerFactionTag)|Tag of faction owning block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[GetPosition()](VRage.Game.ModAPI.Ingame.IMyEntity@GetPosition)|Gets position in world coordinates<br /><br />_Inherited from [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)_|
|[GetProperties(List<ITerminalProperty>, Func<ITerminalProperty, bool>)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetProperties)|Get all terminal actions available for block.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetProperty(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@GetProperty)|Finds terminal property with provided id<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[GetUserRelationToOwner(long, MyRelationsBetweenPlayerAndBlock)](VRage.Game.ModAPI.Ingame.IMyCubeBlock@GetUserRelationToOwner)|Gets relation to owner of block<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[HasLocalPlayerAccess()](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasLocalPlayerAccess)|Returns if local player can use block. Executes [HasPlayerAccess(long, MyRelationsBetweenPlayerAndBlock)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasPlayerAccess) with local player identityId. On Dedicated Server as identityId it is using 0 as playerId<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[HasNobodyPlayerAccessToBlock()](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasNobodyPlayerAccessToBlock)|Returns if Nobody has access to block.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[HasPlayerAccess(long, MyRelationsBetweenPlayerAndBlock)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasPlayerAccess)|Returns if local player can use block. It is also checking for admin access.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[HasPlayerAccessWithNobodyCheck(long, bool)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@HasPlayerAccessWithNobodyCheck)|Returns if player can use block. If playerId is 0 (Nobody), calls HasNobodyPlayerAccessToBlock instead It is also checking for admin access.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[IsSameConstructAs(IMyTerminalBlock)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@IsSameConstructAs)|Determines whether this block is `Mechanical`<sub>prohibited</sub> connected to the other. This is any block connected with rotors or pistons or other mechanical devices, but not things like connectors. This will in most cases constitute your complete construct.<br /><br />Be aware that using merge blocks combines grids into one, so this function will not filter out grids connected that way. Also be aware that detaching the heads of pistons and rotors will cause this connection to change.<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[SearchActionsOfName(string, List<ITerminalAction>, Func<ITerminalAction, bool>)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@SearchActionsOfName)|Get all terminal actions available for block. NOTE: First called `<br /><br />` and then `<br /><br />` check<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[ShootOnce()](Sandbox.ModAPI.Ingame.IMyUserControllableGun@ShootOnce)|Triggers a single shot.<br /><br />_Inherited from [IMyUserControllableGun](Sandbox.ModAPI.Ingame.IMyUserControllableGun)_|
|[GetTargetingGroups()](Sandbox.ModAPI.Ingame.IMyLargeTurretBase@GetTargetingGroups)|_**Obsolete:** Use GetTargetingGroups with parameter instead._<br /><br />Obsolete|
|[GetPlayerRelationToOwner()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@GetPlayerRelationToOwner)|_**Obsolete:** GetPlayerRelationToOwner() is useless ingame. Mods should use the one in ModAPI.IMyCubeBlock_<br /><br />Relation of local player to the block Should not be called on Dedicated Server.<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[RequestEnable(bool)](Sandbox.ModAPI.Ingame.IMyFunctionalBlock@RequestEnable)|_**Obsolete:** Use the setter of Enabled_<br /><br />Obsolete<br /><br />_Inherited from [IMyFunctionalBlock](Sandbox.ModAPI.Ingame.IMyFunctionalBlock)_|
|[SetCustomName(string)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@SetCustomName)|_**Obsolete:** Use the setter of Customname_<br /><br />Obsolete<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[SetCustomName(StringBuilder)](Sandbox.ModAPI.Ingame.IMyTerminalBlock@SetCustomName)|_**Obsolete:** Use the setter of Customname_<br /><br />Obsolete<br /><br />_Inherited from [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)_|
|[UpdateIsWorking()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@UpdateIsWorking)|_**Obsolete**_<br /><br />Force refresh working state. Call if you change block state that could affect its working status.<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|
|[UpdateVisual()](VRage.Game.ModAPI.Ingame.IMyCubeBlock@UpdateVisual)|_**Obsolete**_<br /><br />Updates block visuals (ie. block emissivity)<br /><br />_Inherited from [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)_|

**Implements:**  
* [IMyCubeBlock](VRage.Game.ModAPI.Ingame.IMyCubeBlock)  
* [IMyEntity](VRage.Game.ModAPI.Ingame.IMyEntity)  
* [IMyFunctionalBlock](Sandbox.ModAPI.Ingame.IMyFunctionalBlock)  
* [IMyTerminalBlock](Sandbox.ModAPI.Ingame.IMyTerminalBlock)  
* [IMyUserControllableGun](Sandbox.ModAPI.Ingame.IMyUserControllableGun)

**Inheritors:**  
* [IMyLargeConveyorTurretBase](SpaceEngineers.Game.ModAPI.Ingame.IMyLargeConveyorTurretBase)  
* [IMyLargeGatlingTurret](SpaceEngineers.Game.ModAPI.Ingame.IMyLargeGatlingTurret)  
* [IMyLargeInteriorTurret](SpaceEngineers.Game.ModAPI.Ingame.IMyLargeInteriorTurret)  
* [IMyLargeMissileTurret](SpaceEngineers.Game.ModAPI.Ingame.IMyLargeMissileTurret)

**Type Definitions:**  
* MyObjectBuilder_InteriorTurret/LargeInteriorTurret  
* MyObjectBuilder_LargeGatlingTurret/  
* MyObjectBuilder_LargeGatlingTurret/AutoCannonTurret  
* MyObjectBuilder_LargeGatlingTurret/LargeGatlingTurretReskin  
* MyObjectBuilder_LargeGatlingTurret/SmallGatlingTurret  
* MyObjectBuilder_LargeGatlingTurret/SmallGatlingTurretReskin

