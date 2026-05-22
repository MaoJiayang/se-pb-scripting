**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyOffensiveCombatHitAndRun: IMyAttackPatternComponent
```

Describes entity component for AttackPattern of offensive combat block

## Properties

|Member|Description|
|---|---|
|[BreakOffDistance](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@BreakOffDistance)|Gets or sets break off distance (in meters)|
|[IsMovingAwayFromTarget](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@IsMovingAwayFromTarget)|Gets if grid is moving away from target|
|[IsMovingToTarget](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@IsMovingToTarget)|Gets if grid is moving to target|
|[RetreatAngle](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@RetreatAngle)|Gets or sets retreat angle (in degrees)|
|[RetreatDistance](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@RetreatDistance)|Gets or sets max distance that grid can run away from target|
|[RetreatTimeout](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@RetreatTimeout)|Gets or sets max time that grid can run away from target|
|[AttackPatternId](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent@AttackPatternId)|Gets attack pattern id<br /><br />_Inherited from [IMyAttackPatternComponent](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent)_|
|[AttackPatternName](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent@AttackPatternName)|Gets attack pattern name<br /><br />_Inherited from [IMyAttackPatternComponent](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent)_|
|[AttackPatternTooltip](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent@AttackPatternTooltip)|Gets attack pattern tooltip<br /><br />_Inherited from [IMyAttackPatternComponent](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent)_|
|[HasEnemy](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent@HasEnemy)|Gets if attack pattern has enemy in range<br /><br />_Inherited from [IMyAttackPatternComponent](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent)_|
|[IsSelected](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent@IsSelected)|Gets if attack pattern is selected<br /><br />_Inherited from [IMyAttackPatternComponent](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent)_|

## Methods

|Member|Description|
|---|---|
|[GetSelectedWeapons(List<long>)](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@GetSelectedWeapons)|Gets weapons that should be used to damage to attack enemy May return also modded guns EntityId.|
|[IsWeaponSelected(long)](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@IsWeaponSelected)|Gets if weapon is selected|
|[SetSelectedWeapons(List<long>)](Sandbox.ModAPI.Ingame.IMyOffensiveCombatHitAndRun@SetSelectedWeapons)|Sets weapons EntityIds that can would be used to damage to attack enemy Modded gun are allowed, but you need override `IMyOffensiveCombatHitAndRun.BlockValidation`<sub>prohibited</sub> and `IMyOffensiveCombatHitAndRun.SetShooting`<sub>prohibited</sub> |

**Implements:**  
* [IMyAttackPatternComponent](Sandbox.ModAPI.Ingame.IMyAttackPatternComponent)

