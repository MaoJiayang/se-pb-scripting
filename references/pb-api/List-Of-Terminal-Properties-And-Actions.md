## Overview
**Note: Terminal actions and properties are for all intents and purposes obsolete since all vanilla block interfaces now contain proper API access to _most of_ this information. It is highly recommended you use those for less overhead.**

[IMyAirtightHangarDoor](#imyairtighthangardoor)  
[IMyAirtightSlideDoor](#imyairtightslidedoor)  
[IMyAirVent](#imyairvent)  
[IMyArtificialMassBlock](#imyartificialmassblock)  
[IMyAssembler](#imyassembler)  
[IMyBasicMissionBlock](#imybasicmissionblock)  
[IMyBatteryBlock](#imybatteryblock)  
[IMyBeacon](#imybeacon)  
[IMyBroadcastController](#imybroadcastcontroller)  
[IMyButtonPanel](#imybuttonpanel)  
[IMyCameraBlock](#imycamerablock)  
[IMyCargoContainer](#imycargocontainer)  
[IMyCockpit](#imycockpit)  
[IMyCollector](#imycollector)  
[IMyConveyorSorter](#imyconveyorsorter)  
[IMyCryoChamber](#imycryochamber)  
[IMyDecoy](#imydecoy)  
[IMyDefensiveCombatBlock](#imydefensivecombatblock)  
[IMyDoor](#imydoor)  
[IMyEmotionControllerBlock](#imyemotioncontrollerblock)  
[IMyEventControllerBlock](#imyeventcontrollerblock)  
[IMyExtendedPistonBase](#imyextendedpistonbase)  
[IMyFlightMovementBlock](#imyflightmovementblock)  
[IMyFunctionalBlock](#imyfunctionalblock)  
[IMyGasGenerator](#imygasgenerator)  
[IMyGasTank](#imygastank)  
[IMyGravityGenerator](#imygravitygenerator)  
[IMyGravityGeneratorSphere](#imygravitygeneratorsphere)  
[IMyGyro](#imygyro)  
[IMyHeatVent](#imyheatvent)  
[IMyInteriorLight](#imyinteriorlight)  
[IMyJumpDrive](#imyjumpdrive)  
[IMyLandingGear](#imylandinggear)  
[IMyLargeGatlingTurret](#imylargegatlingturret)  
[IMyLargeInteriorTurret](#imylargeinteriorturret)  
[IMyLaserAntenna](#imylaserantenna)  
[IMyMedicalRoom](#imymedicalroom)  
[IMyMotorAdvancedStator](#imymotoradvancedstator)  
[IMyMotorSuspension](#imymotorsuspension)  
[IMyOffensiveCombatBlock](#imyoffensivecombatblock)  
[IMyOreDetector](#imyoredetector)  
[IMyOxygenFarm](#imyoxygenfarm)  
[IMyParachute](#imyparachute)  
[IMyPathRecorderBlock](#imypathrecorderblock)  
[IMyPistonBase](#imypistonbase)  
[IMyProgrammableBlock](#imyprogrammableblock)  
[IMyProjector](#imyprojector)  
[IMyRadioAntenna](#imyradioantenna)  
[IMyReactor](#imyreactor)  
[IMyRefinery](#imyrefinery)  
[IMyReflectorLight](#imyreflectorlight)  
[IMyRemoteControl](#imyremotecontrol)  
[IMySafeZoneBlock](#imysafezoneblock)  
[IMySearchlight](#imysearchlight)  
[IMySensorBlock](#imysensorblock)  
[IMyShipConnector](#imyshipconnector)  
[IMyShipDrill](#imyshipdrill)  
[IMyShipGrinder](#imyshipgrinder)  
[IMyShipMergeBlock](#imyshipmergeblock)  
[IMyShipWelder](#imyshipwelder)  
[IMySmallGatlingGun](#imysmallgatlinggun)  
[IMySmallMissileLauncher](#imysmallmissilelauncher)  
[IMySmallMissileLauncherReload](#imysmallmissilelauncherreload)  
[IMySolarPanel](#imysolarpanel)  
[IMySoundBlock](#imysoundblock)  
[IMySpaceBall](#imyspaceball)  
[IMyStoreBlock](#imystoreblock)  
[IMyTargetDummyBlock](#imytargetdummyblock)  
[IMyTerminalBlock](#imyterminalblock)  
[IMyTextPanel](#imytextpanel)  
[IMyThrust](#imythrust)  
[IMyTimerBlock](#imytimerblock)  
[IMyTransponder](#imytransponder)  
[IMyTurretControlBlock](#imyturretcontrolblock)  
[IMyUpgradeModule](#imyupgrademodule)  
[IMyWarhead](#imywarhead)  
[IMyWindTurbine](#imywindturbine)  

## IMyAirtightHangarDoor

### Actions

|Name|Description|
|-|-|
|AnyoneCanUse|Anyone Can Use On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|Open| Open/Closed|
|Open_Off| Closed|
|Open_On| Open|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AnyoneCanUse|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|Open|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyAirtightSlideDoor

### Actions

|Name|Description|
|-|-|
|AnyoneCanUse|Anyone Can Use On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|Open| Open/Closed|
|Open_Off| Closed|
|Open_On| Open|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AnyoneCanUse|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|Open|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyAirVent

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|Depressurize|Depressurize On/Off|
|Depressurize_Off|Depressurize Off|
|Depressurize_On|Depressurize On|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Depressurize|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyArtificialMassBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyAssembler

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|slaveMode|Cooperative Mode On/Off|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|slaveMode|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyBasicMissionBlock

### Actions

|Name|Description|
|-|-|
|ActivateBehavior|AI Behavior On/Off|
|ActivateBehavior_Off|AI Behavior Off|
|ActivateBehavior_On|AI Behavior On|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFollowDistance|Decrease Follow Distance|
|DecreaseFollowHomeMaxRange|Decrease Max. Range from Home|
|DecreaseFollowHomeMinRange|Decrease Min. Range from Home|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|FollowMe|Follow Me|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFollowDistance|Increase Follow Distance|
|IncreaseFollowHomeMaxRange|Increase Max. Range from Home|
|IncreaseFollowHomeMinRange|Increase Min. Range from Home|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetCurrentGridPositionHome|Set Grid Position|
|SetCurrentPositionHome|Set Player Position|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|StopFollowing|Stop Following|
|Wander|Wander when idle On/Off|

### Properties

|Name|Type|
|-|-|
|ActivateBehavior|bool|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|FollowDistance|float|
|FollowHomeMaxRange|float|
|FollowHomeMinRange|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|ID_MODE_SELECTOR_COMBOBOX|long|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|SelectMission|long|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|Wander|bool|

## IMyBatteryBlock

### Actions

|Name|Description|
|-|-|
|Auto|Enable Auto|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|Discharge|Discharge On/Off|
|Discharge_Off|Discharge Off|
|Discharge_On|Discharge On|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Recharge|Recharge On/Off|
|Recharge_Off|Recharge Off|
|Recharge_On|Recharge On|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|ChargeMode|long|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyBeacon

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRadius|Decrease Broadcast radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseRadius|Increase Broadcast radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetHudText|Set HUD Text|
|SetRadius|Set Broadcast Radius|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|CustomName|StringBuilder|
|Font|long|
|FontColor|Color|
|FontSize|float|
|HudText|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Radius|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyBroadcastController

### Actions

|Name|Description|
|-|-|
|BroadcastTargetEveryone|Enable Everyone|
|BroadcastTargetFaction|Enable Faction Only|
|BroadcastTargetOwner|Enable Owner Only|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SendGps|Send GPS|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|Transmit Message 1|Transmit Message 1|
|Transmit Message 2|Transmit Message 2|
|Transmit Message 3|Transmit Message 3|
|Transmit Message 4|Transmit Message 4|
|Transmit Message 5|Transmit Message 5|
|Transmit Message 6|Transmit Message 6|
|Transmit Message 7|Transmit Message 7|
|Transmit Message 8|Transmit Message 8|
|TransmitRandomMessage|Send Random Message|
|UseAntenna|Use Antenna On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|BroadcastTarget|long|
|ChangeIntervalSlider|float|
|Content|long|
|CustomName|StringBuilder|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Message0|StringBuilder|
|Message1|StringBuilder|
|Message2|StringBuilder|
|Message3|StringBuilder|
|Message4|StringBuilder|
|Message5|StringBuilder|
|Message6|StringBuilder|
|Message7|StringBuilder|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseAntenna|bool|

## IMyButtonPanel

### Actions

|Name|Description|
|-|-|
|AnyoneCanUse|Anyone Can Use On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AnyoneCanUse|bool|
|BackgroundColor|Color|
|ButtonName|StringBuilder|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyCameraBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyCargoContainer

### Actions

|Name|Description|
|-|-|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|Name|StringBuilder|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|

## IMyCockpit

### Actions

|Name|Description|
|-|-|
|ControlGyros|Control Gyros On/Off|
|ControlThrusters|Control thrusters On/Off|
|ControlWheels|Control wheels On/Off|
|DampenersOverride|Inertia dampeners On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|HandBrake|Handbrake On/Off|
|HorizonIndicator|Show horizon and altitude On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|MainCockpit|Main cockpit On/Off|
|Park|Park On/Off|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TargetLocking|Enable target locking On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|ControlGyros|bool|
|ControlThrusters|bool|
|ControlWheels|bool|
|DampenersOverride|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|HandBrake|bool|
|HorizonIndicator|bool|
|MainCockpit|bool|
|Name|StringBuilder|
|Park|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetLocking|bool|
|TextPaddingSlider|float|

## IMyCollector

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyConveyorSorter

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DrainAll|Drain All On/Off|
|DrainAll_Off|Drain All Off|
|DrainAll_On|Drain All On|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|blacklistWhitelist|long|
|ChangeIntervalSlider|float|
|Content|long|
|DrainAll|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|SearchField|StringBuilder|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyCryoChamber

### Actions

|Name|Description|
|-|-|
|ControlGyros|Control Gyros On/Off|
|ControlThrusters|Control thrusters On/Off|
|ControlWheels|Control wheels On/Off|
|DampenersOverride|Inertia dampeners On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|HandBrake|Handbrake On/Off|
|HorizonIndicator|Show horizon and altitude On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|MainCockpit|Main cockpit On/Off|
|Park|Park On/Off|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TargetLocking|Enable target locking On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|ControlGyros|bool|
|ControlThrusters|bool|
|ControlWheels|bool|
|DampenersOverride|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|HandBrake|bool|
|HorizonIndicator|bool|
|MainCockpit|bool|
|Name|StringBuilder|
|Park|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetLocking|bool|
|TextPaddingSlider|float|

## IMyDecoy

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyDefensiveCombatBlock

### Actions

|Name|Description|
|-|-|
|ActivateBehavior|AI Behavior On/Off|
|ActivateBehavior_Off|AI Behavior Off|
|ActivateBehavior_On|AI Behavior On|
|CanTargetCharacters|Target Characters On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseEvasiveManeuverAngle|Decrease Random Deviations Angle|
|DecreaseEvasiveManeuverIntervalRange|Decrease Random Deviations Interval|
|DecreaseFleeDistance|Decrease Flee distance|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseWaypointZoneSize|Decrease Flee waypoint size|
|EvasiveManeuvers|Evasive Maneuvers On/Off|
|EvasiveManeuvers_Off|Evasive Maneuvers Off|
|EvasiveManeuvers_On|Evasive Maneuvers On|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseEvasiveManeuverAngle|Increase Random Deviations Angle|
|IncreaseEvasiveManeuverIntervalRange|Increase Random Deviations Interval|
|IncreaseFleeDistance|Increase Flee distance|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseWaypointZoneSize|Increase Flee waypoint size|
|LockTarget|Lock Target On/Off|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetAttackMode_EnemiesAndNeutrals|Set Attack Mode: Enemies And Neutrals|
|SetAttackMode_EnemiesOnly|Set Attack Mode: Enemies Only|
|SetTargetingGroup_PowerSystems|Target Power systems|
|SetTargetingGroup_Propulsion|Target Propulsion|
|SetTargetingGroup_Weapons|Target Weapons|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|ActivateBehavior|bool|
|alignment|long|
|BackgroundColor|Color|
|CanTargetCharacters|bool|
|ChangeIntervalSlider|float|
|Content|long|
|EvasiveManeuverAngle|float|
|EvasiveManeuverIntervalRange|float|
|EvasiveManeuvers|bool|
|Flee|long|
|FleeDistance|float|
|FleeMode|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|LockTarget|bool|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetingGroup|long|
|TargetLock|long|
|TextPaddingSlider|float|
|WaypointZoneSize|float|

## IMyDoor

### Actions

|Name|Description|
|-|-|
|AnyoneCanUse|Anyone Can Use On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|Open| Open/Closed|
|Open_Off| Closed|
|Open_On| Open|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AnyoneCanUse|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|Open|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyEmotionControllerBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|Textures\Models\Emotes\Angry.dds|Angry|
|Textures\Models\Emotes\Annoyed.dds|Annoyed|
|Textures\Models\Emotes\Confused.dds|Confused|
|Textures\Models\Emotes\Crying.dds|Crying|
|Textures\Models\Emotes\Dead.dds|Dead|
|Textures\Models\Emotes\Evil.dds|Evil|
|Textures\Models\Emotes\Happy.dds|Happy|
|Textures\Models\Emotes\Love.dds|Love|
|Textures\Models\Emotes\Neutral.dds|Neutral|
|Textures\Models\Emotes\Sad.dds|Sad|
|Textures\Models\Emotes\Shocked.dds|Shocked|
|Textures\Models\Emotes\Skeptical.dds|Skeptical|
|Textures\Models\Emotes\Sleepy.dds|Sleepy|
|Textures\Models\Emotes\Suspicious_Left.dds|Suspicious Left|
|Textures\Models\Emotes\Suspicious_Right.dds|Suspicious Right|
|Textures\Models\Emotes\Wink.dds|Wink|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyEventControllerBlock

### Actions

|Name|Description|
|-|-|
|ANDCheckbox|AND Gate On/Off|
|ANDCheckbox_Off|AND Gate Off|
|ANDCheckbox_On|AND Gate On|
|DecreaseAngle|Decrease Angle Threshold|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseNaturalGravityChangedSlider|Decrease Natural gravity:|
|DecreaseNaturalGravityChangedSlider|Decrease Distance to Locked Target|
|DecreaseSpeed|Decrease Speed Threshold|
|DecreaseSurfaceheightSlider|Decrease Altitude|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseThreshold|Decrease Threshold|
|IncreaseAngle|Increase Angle Threshold|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseNaturalGravityChangedSlider|Increase Natural gravity:|
|IncreaseNaturalGravityChangedSlider|Increase Distance to Locked Target|
|IncreaseSpeed|Increase Speed Threshold|
|IncreaseSurfaceheightSlider|Increase Altitude|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseThreshold|Increase Threshold|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|ANDCheckbox|bool|
|Angle|float|
|AvailableEvents|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Condition|long|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|NaturalGravityChangedSlider|float|
|NaturalGravityChangedSlider|float|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|SearchBox|StringBuilder|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|Speed|float|
|SurfaceheightSlider|float|
|TextPaddingSlider|float|
|Threshold|float|

## IMyExtendedPistonBase

### Actions

|Name|Description|
|-|-|
|Add Top Part|Add Piston Head|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseLowerLimit|Decrease Minimum distance|
|DecreaseMaxImpulseAxis|Decrease Max Impulse Axis|
|DecreaseMaxImpulseNonAxis|Decrease Max Impulse NonAxis|
|DecreaseSafetyDetach|Decrease Safety detach|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseUpperLimit|Decrease Maximum distance|
|DecreaseVelocity|Decrease Velocity|
|DecreaseWeld speed|Decrease Safety lock speed|
|Extend|Extend|
|Force weld|Safety lock override On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseLowerLimit|Increase Minimum distance|
|IncreaseMaxImpulseAxis|Increase Max Impulse Axis|
|IncreaseMaxImpulseNonAxis|Increase Max Impulse NonAxis|
|IncreaseSafetyDetach|Increase Safety detach|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseUpperLimit|Increase Maximum distance|
|IncreaseVelocity|Increase Velocity|
|IncreaseWeld speed|Increase Safety lock speed|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ResetVelocity|Reset Velocity|
|Retract|Retract|
|Reverse|Reverse|
|SetAndMove|Set And Move|
|SetVelocity|Set Velocity|
|ShareInertiaTensor|Share inertia tensor On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Force weld|bool|
|LowerLimit|float|
|MaxImpulseAxis|float|
|MaxImpulseNonAxis|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|SafetyDetach|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShareInertiaTensor|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UpperLimit|float|
|Velocity|float|
|Weld speed|float|

## IMyFlightMovementBlock

### Actions

|Name|Description|
|-|-|
|ActivateBehavior|AI Behavior On/Off|
|ActivateBehavior_Off|AI Behavior Off|
|ActivateBehavior_On|AI Behavior On|
|AlignToGravity|Align to P-Gravity On/Off|
|AlignToGravity_Off|Align to P-Gravity Off|
|AlignToGravity_On|Align to P-Gravity On|
|CollisionAvoidance|Collision avoidance On/Off|
|CollisionAvoidance_Off|Collision avoidance Off|
|CollisionAvoidance_On|Collision avoidance On|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseMaxPitchAngle|Decrease Max Pitch Angle|
|DecreaseMaxRollAngle|Decrease Max Roll Angle|
|DecreaseMinHeightAboveTerrain|Decrease Min. altitude|
|DecreaseSpeedLimit|Decrease Speed limit|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DockingMode|Precision Mode On/Off|
|DockingMode_Off|Precision Mode Off|
|DockingMode_On|Precision Mode On|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseMaxPitchAngle|Increase Max Pitch Angle|
|IncreaseMaxRollAngle|Increase Max Roll Angle|
|IncreaseMinHeightAboveTerrain|Increase Min. altitude|
|IncreaseSpeedLimit|Increase Speed limit|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetSpeedLimit|Set Speed Limit|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|ActivateBehavior|bool|
|alignment|long|
|AlignToGravity|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|CollisionAvoidance|bool|
|Content|long|
|DockingMode|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|MaxPitchAngle|float|
|MaxRollAngle|float|
|MinHeightAboveTerrain|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|SpeedLimit|float|
|TextPaddingSlider|float|

## IMyFunctionalBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyGasGenerator

### Actions

|Name|Description|
|-|-|
|Auto-Refill|Auto-Refill On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Refill|Refill Bottles|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|Auto-Refill|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyGasTank

### Actions

|Name|Description|
|-|-|
|Auto-Refill|Auto-Refill On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Refill|Refill Bottles|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|Stockpile|Stockpile On/Off|
|Stockpile_Off|Stockpile Off|
|Stockpile_On|Stockpile On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|Auto-Refill|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|Stockpile|bool|
|TextPaddingSlider|float|

## IMyGravityGenerator

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseDepth|Decrease Field depth|
|DecreaseFontSize|Decrease Font Size|
|DecreaseGravity|Decrease Acceleration|
|DecreaseHeight|Decrease Field height|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseWidth|Decrease Field width|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseDepth|Increase Field depth|
|IncreaseFontSize|Increase Font Size|
|IncreaseGravity|Increase Acceleration|
|IncreaseHeight|Increase Field height|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseWidth|Increase Field width|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetGravityAcceleration|Set Acceleration|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Depth|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Gravity|float|
|Height|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|Width|float|

## IMyGravityGeneratorSphere

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseGravity|Decrease Acceleration|
|DecreaseRadius|Decrease Radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseGravity|Increase Acceleration|
|IncreaseRadius|Increase Radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetGravityAcceleration|Set Acceleration|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Gravity|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Radius|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyGyro

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreasePitch|Decrease Pitch override|
|DecreasePower|Decrease Power|
|DecreaseRoll|Decrease Roll override|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseYaw|Decrease Yaw override|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreasePitch|Increase Pitch override|
|IncreasePower|Increase Power|
|IncreaseRoll|Increase Roll override|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseYaw|Increase Yaw override|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|Override|Override controls On/Off|
|Override_Off|Override controls Off|
|Override_On|Override controls On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetPitch|Set Pitch|
|SetPower|Set Power|
|SetRoll|Set Roll|
|SetYaw|Set Yaw|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|Override|bool|
|Pitch|float|
|Power|float|
|PreserveAspectRatio|bool|
|Roll|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|Yaw|float|

## IMyHeatVent

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFalloff|Decrease Falloff|
|DecreaseFontSize|Decrease Font Size|
|DecreaseIntensity|Decrease Intensity|
|DecreaseOffset|Decrease Offset|
|DecreasePowerDependency|Decrease Power Dependency|
|DecreaseRadius|Decrease Radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFalloff|Increase Falloff|
|IncreaseFontSize|Increase Font Size|
|IncreaseIntensity|Increase Intensity|
|IncreaseOffset|Increase Offset|
|IncreasePowerDependency|Increase Power Dependency|
|IncreaseRadius|Increase Radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetColorMax|Color at maximal load|
|SetColorMin|Color at minimal load|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|ColorMax|Color|
|ColorMin|Color|
|Content|long|
|Falloff|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Intensity|float|
|Name|StringBuilder|
|Offset|float|
|OnOff|bool|
|PowerDependency|float|
|PreserveAspectRatio|bool|
|Radius|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyInteriorLight

### Actions

|Name|Description|
|-|-|
|DecreaseBlink Interval|Decrease Blink Interval|
|DecreaseBlink Lenght|Decrease Blink Length|
|DecreaseBlink Offset|Decrease Blink Offset|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFalloff|Decrease Falloff|
|DecreaseFontSize|Decrease Font Size|
|DecreaseIntensity|Decrease Intensity|
|DecreaseOffset|Decrease Offset|
|DecreaseRadius|Decrease Radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseBlink Interval|Increase Blink Interval|
|IncreaseBlink Lenght|Increase Blink Length|
|IncreaseBlink Offset|Increase Blink Offset|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFalloff|Increase Falloff|
|IncreaseFontSize|Increase Font Size|
|IncreaseIntensity|Increase Intensity|
|IncreaseOffset|Increase Offset|
|IncreaseRadius|Increase Radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetBlinkInterval|Set Blink Interval|
|SetColor|Set Color|
|SetRadius|Set Radius|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|Blink Interval|float|
|Blink Lenght|float|
|Blink Offset|float|
|ChangeIntervalSlider|float|
|Color|Color|
|Content|long|
|Falloff|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Intensity|float|
|Name|StringBuilder|
|Offset|float|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Radius|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyJumpDrive

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseJumpDistance|Decrease Distance|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseJumpDistance|Increase Distance|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Recharge|Recharge On/Off|
|Recharge_Off|Recharge Off|
|Recharge_On|Recharge On|
|SetGravityAcceleration|Set Jump Distance|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|JumpDistance|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Recharge|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|SearchField|StringBuilder|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyLandingGear

### Actions

|Name|Description|
|-|-|
|Autolock|Autolock On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableParking|Used for parking On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|Lock|Lock|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|SwitchLock|Switch lock|
|Unlock|Unlock|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|Autolock|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|EnableParking|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyLargeGatlingTurret

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRange|Decrease AI aiming radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableIdleMovement|Enable idle movement On/Off|
|EnableIdleMovement_Off|Enable idle movement Off|
|EnableIdleMovement_On|Enable idle movement On|
|EnableTargetLocking|Enable target locking On/Off|
|FocusLockedTarget|Focus Locked Target|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseRange|Increase AI aiming radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Shoot|Shoot On/Off|
|Shoot_Off|Shoot Off|
|Shoot_On|Shoot On|
|ShootOnce|Shoot once|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TargetCharacters|Target characters On/Off|
|TargetCharacters_Off|Target characters Off|
|TargetCharacters_On|Target characters On|
|TargetEnemies|Target Enemies On/Off|
|TargetEnemies_Off|Target Enemies Off|
|TargetEnemies_On|Target Enemies On|
|TargetFriends|Target Friends On/Off|
|TargetFriends_Off|Target Friends Off|
|TargetFriends_On|Target Friends On|
|TargetingGroup_CycleSubsystems|Cycle Subsystems|
|TargetingGroup_PowerSystems|Target Power systems|
|TargetingGroup_Propulsion|Target Propulsion|
|TargetingGroup_Weapons|Target Weapons|
|TargetLargeShips|Target large ships On/Off|
|TargetLargeShips_Off|Target large ships Off|
|TargetLargeShips_On|Target large ships On|
|TargetMeteors|Target meteors On/Off|
|TargetMeteors_Off|Target meteors Off|
|TargetMeteors_On|Target meteors On|
|TargetMissiles|Target rockets On/Off|
|TargetMissiles_Off|Target rockets Off|
|TargetMissiles_On|Target rockets On|
|TargetNeutrals|Target neutrals On/Off|
|TargetNeutrals_Off|Target neutrals Off|
|TargetNeutrals_On|Target neutrals On|
|TargetSmallShips|Target small ships On/Off|
|TargetSmallShips_Off|Target small ships Off|
|TargetSmallShips_On|Target small ships On|
|TargetStations|Target stations On/Off|
|TargetStations_Off|Target stations Off|
|TargetStations_On|Target stations On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|EnableIdleMovement|bool|
|EnableTargetLocking|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Range|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|Shoot|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetCharacters|bool|
|TargetEnemies|bool|
|TargetFriends|bool|
|TargetingGroup_Selector|long|
|TargetLargeShips|bool|
|TargetMeteors|bool|
|TargetMissiles|bool|
|TargetNeutrals|bool|
|TargetSmallShips|bool|
|TargetStations|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyLargeInteriorTurret

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRange|Decrease AI aiming radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableIdleMovement|Enable idle movement On/Off|
|EnableIdleMovement_Off|Enable idle movement Off|
|EnableIdleMovement_On|Enable idle movement On|
|EnableTargetLocking|Enable target locking On/Off|
|FocusLockedTarget|Focus Locked Target|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseRange|Increase AI aiming radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Shoot|Shoot On/Off|
|Shoot_Off|Shoot Off|
|Shoot_On|Shoot On|
|ShootOnce|Shoot once|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TargetCharacters|Target characters On/Off|
|TargetCharacters_Off|Target characters Off|
|TargetCharacters_On|Target characters On|
|TargetEnemies|Target Enemies On/Off|
|TargetEnemies_Off|Target Enemies Off|
|TargetEnemies_On|Target Enemies On|
|TargetFriends|Target Friends On/Off|
|TargetFriends_Off|Target Friends Off|
|TargetFriends_On|Target Friends On|
|TargetingGroup_CycleSubsystems|Cycle Subsystems|
|TargetingGroup_PowerSystems|Target Power systems|
|TargetingGroup_Propulsion|Target Propulsion|
|TargetingGroup_Weapons|Target Weapons|
|TargetLargeShips|Target large ships On/Off|
|TargetLargeShips_Off|Target large ships Off|
|TargetLargeShips_On|Target large ships On|
|TargetMeteors|Target meteors On/Off|
|TargetMeteors_Off|Target meteors Off|
|TargetMeteors_On|Target meteors On|
|TargetMissiles|Target rockets On/Off|
|TargetMissiles_Off|Target rockets Off|
|TargetMissiles_On|Target rockets On|
|TargetNeutrals|Target neutrals On/Off|
|TargetNeutrals_Off|Target neutrals Off|
|TargetNeutrals_On|Target neutrals On|
|TargetSmallShips|Target small ships On/Off|
|TargetSmallShips_Off|Target small ships Off|
|TargetSmallShips_On|Target small ships On|
|TargetStations|Target stations On/Off|
|TargetStations_Off|Target stations Off|
|TargetStations_On|Target stations On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|EnableIdleMovement|bool|
|EnableTargetLocking|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Range|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|Shoot|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetCharacters|bool|
|TargetEnemies|bool|
|TargetFriends|bool|
|TargetingGroup_Selector|long|
|TargetLargeShips|bool|
|TargetMeteors|bool|
|TargetMissiles|bool|
|TargetNeutrals|bool|
|TargetSmallShips|bool|
|TargetStations|bool|
|TextPaddingSlider|float|

## IMyLaserAntenna

### Actions

|Name|Description|
|-|-|
|ConnectGPS|Connect to coords|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRange|Decrease Range|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|Idle|Idle|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseRange|Increase Range|
|IncreaseTextPaddingSlider|Increase Text Padding|
|isPerm|Permanent connection On/Off|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PasteGpsCoords|Paste coords|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|gpsCoords|StringBuilder|
|isPerm|bool|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Range|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyMedicalRoom

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|SetFaction|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|SpawnName|StringBuilder|
|TakeOwnership|bool|
|TextPaddingSlider|float|

## IMyMotorAdvancedStator

### Actions

|Name|Description|
|-|-|
|AddHingeTopPart|Add Hinge Head|
|AddMediumHingeTopPart|Add Medium Head|
|AddMediumRotorTopPart|Add Medium Head|
|AddRotorTopPart|Add Rotor Head|
|AddSmallHingeTopPart|Add Small Head|
|AddSmallRotorTopPart|Add Small Head|
|Attach|Attach|
|DecreaseBrakingTorque|Decrease Braking torque|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseDisplacement|Decrease Rotor displacement|
|DecreaseFontSize|Decrease Font Size|
|DecreaseLowerLimit|Decrease Lower limit|
|DecreaseSafetyDetach|Decrease Safety detach|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseTorque|Decrease Torque|
|DecreaseUpperLimit|Decrease Upper limit|
|DecreaseVelocity|Decrease Velocity|
|DecreaseWeld speed|Decrease Safety lock speed|
|Detach|Detach|
|Force weld|Safety lock override On/Off|
|HingeLock|Hinge lock On/Off|
|HingeLock_Off|Hinge lock Off|
|HingeLock_On|Hinge lock On|
|IncreaseBrakingTorque|Increase Braking torque|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseDisplacement|Increase Rotor displacement|
|IncreaseFontSize|Increase Font Size|
|IncreaseLowerLimit|Increase Lower limit|
|IncreaseSafetyDetach|Increase Safety detach|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseTorque|Increase Torque|
|IncreaseUpperLimit|Increase Upper limit|
|IncreaseVelocity|Increase Velocity|
|IncreaseWeld speed|Increase Safety lock speed|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ResetVelocity|Reset Velocity|
|Reverse|Reverse|
|RotateToAngle|Rotate To Angle|
|RotorLock|Rotor lock On/Off|
|RotorLock_Off|Rotor lock Off|
|RotorLock_On|Rotor lock On|
|SetLowerLimit|Set Lower Limit|
|SetUpperLimit|Set Upper Limit|
|SetVelocity|Set Velocity|
|ShareInertiaTensor|Share inertia tensor On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|BrakingTorque|float|
|ChangeIntervalSlider|float|
|Content|long|
|Displacement|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Force weld|bool|
|HingeLock|bool|
|LowerLimit|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|RotorLock|bool|
|SafetyDetach|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShareInertiaTensor|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|Torque|float|
|UpperLimit|float|
|Velocity|float|
|Weld speed|float|

## IMyMotorSuspension

### Actions

|Name|Description|
|-|-|
|Add Top Part|Add Wheel|
|AirShock|AirShock On/Off|
|Braking|Brake On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseFriction|Decrease Friction|
|DecreaseHeight|Decrease Height Offset|
|DecreaseMaxSteerAngle|Decrease Steering Angle|
|DecreasePower|Decrease Power|
|DecreasePropulsion override|Decrease Propulsion override|
|DecreaseSafetyDetach|Decrease Safety detach|
|DecreaseSpeed Limit|Decrease Speed limit|
|DecreaseSteer override|Decrease Steer override|
|DecreaseStrength|Decrease Strength|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseWeld speed|Decrease Safety lock speed|
|EnableParking|Allow Parking Brake On/Off|
|Force weld|Safety lock override On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseFriction|Increase Friction|
|IncreaseHeight|Increase Height Offset|
|IncreaseMaxSteerAngle|Increase Steering Angle|
|IncreasePower|Increase Power|
|IncreasePropulsion override|Increase Propulsion override|
|IncreaseSafetyDetach|Increase Safety detach|
|IncreaseSpeed Limit|Increase Speed limit|
|IncreaseSteer override|Increase Steer override|
|IncreaseStrength|Increase Strength|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseWeld speed|Increase Safety lock speed|
|InvertPropulsion|Invert Propulsion On/Off|
|InvertSteering|Invert Steering On/Off|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Propulsion|Propulsion On/Off|
|ResetHeight|Reset Height Offset|
|ResetMaxSteerAngle|Reset Steering Angle|
|ResetPropulsion override|Reset Propulsion override|
|ResetSpeed Limit|Reset Speed limit|
|ResetSteer override|Reset Steer override|
|SetPropulsionOverride|Set Propulsion Override|
|SetSpeedLimit|Set Speed Limit|
|SetSteerOverride|Set Steer Override|
|ShareInertiaTensor|Share inertia tensor On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|Steering|Steering On/Off|

### Properties

|Name|Type|
|-|-|
|AirShock|bool|
|alignment|long|
|BackgroundColor|Color|
|Braking|bool|
|ChangeIntervalSlider|float|
|Content|long|
|EnableParking|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Force weld|bool|
|Friction|float|
|Height|float|
|InvertPropulsion|bool|
|InvertSteering|bool|
|MaxSteerAngle|float|
|Name|StringBuilder|
|OnOff|bool|
|Power|float|
|PreserveAspectRatio|bool|
|Propulsion|bool|
|Propulsion override|float|
|SafetyDetach|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShareInertiaTensor|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|Speed Limit|float|
|Steer override|float|
|Steering|bool|
|Strength|float|
|TextPaddingSlider|float|
|Weld speed|float|

## IMyOffensiveCombatBlock

### Actions

|Name|Description|
|-|-|
|ActivateBehavior|AI Behavior On/Off|
|ActivateBehavior_Off|AI Behavior Off|
|ActivateBehavior_On|AI Behavior On|
|CanTargetCharacters|Target Characters On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseOffensiveCombatCircleOrbit_CircleDistance|Decrease Circle Distance|
|DecreaseOffensiveCombatHitAndRun_BreakOffDistance|Decrease Break-off distance|
|DecreaseOffensiveCombatHitAndRun_RetreatAngle|Decrease Retreat angle|
|DecreaseOffensiveCombatHitAndRun_RetreatDistance|Decrease Retreat distance|
|DecreaseOffensiveCombatHitAndRun_RetreatTimeout|Decrease Retreat timeout|
|DecreaseOffensiveCombatStayAtRange_MaximalDistance|Decrease Maximal Distance|
|DecreaseOffensiveCombatStayAtRange_MinimalDistance|Decrease Minimal Distance|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseOffensiveCombatCircleOrbit_CircleDistance|Increase Circle Distance|
|IncreaseOffensiveCombatHitAndRun_BreakOffDistance|Increase Break-off distance|
|IncreaseOffensiveCombatHitAndRun_RetreatAngle|Increase Retreat angle|
|IncreaseOffensiveCombatHitAndRun_RetreatDistance|Increase Retreat distance|
|IncreaseOffensiveCombatHitAndRun_RetreatTimeout|Increase Retreat timeout|
|IncreaseOffensiveCombatStayAtRange_MaximalDistance|Increase Maximal Distance|
|IncreaseOffensiveCombatStayAtRange_MinimalDistance|Increase Minimal Distance|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OffensiveCombatCircleOrbit_CircleInPGravity|Circle in P-Gravity On/Off|
|OffensiveCombatCircleOrbit_FacingBack|Backward On/Off|
|OffensiveCombatCircleOrbit_FacingDown|Down On/Off|
|OffensiveCombatCircleOrbit_FacingFront|Front On/Off|
|OffensiveCombatCircleOrbit_FacingLeft|Left On/Off|
|OffensiveCombatCircleOrbit_FacingRight|Right On/Off|
|OffensiveCombatCircleOrbit_FacingUp|Up On/Off|
|OffensiveCombatIntercept_OverrideCollisionAvoidance|Override Collision Avoidance On/Off|
|OffensiveCombatStayAtRange_EvasiveManeuvers|Evasive Maneuvers On/Off|
|OffensiveCombatStayAtRange_EvasiveManeuvers_Off|Evasive Maneuvers Off|
|OffensiveCombatStayAtRange_EvasiveManeuvers_On|Evasive Maneuvers On|
|OffensiveCombatStayAtRange_FacingBack|Backward On/Off|
|OffensiveCombatStayAtRange_FacingDown|Down On/Off|
|OffensiveCombatStayAtRange_FacingFront|Front On/Off|
|OffensiveCombatStayAtRange_FacingLeft|Left On/Off|
|OffensiveCombatStayAtRange_FacingRight|Right On/Off|
|OffensiveCombatStayAtRange_FacingUp|Up On/Off|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetAttackMode_EnemiesAndNeutrals|Set Attack Mode: Enemies And Neutrals|
|SetAttackMode_EnemiesOnly|Set Attack Mode: Enemies Only|
|SetTargetingGroup_PowerSystems|Target Power systems|
|SetTargetingGroup_Propulsion|Target Propulsion|
|SetTargetingGroup_Weapons|Target Weapons|
|SetTargetPriority_Closest|Set Target Priority: Closest|
|SetTargetPriority_Largest|Set Target Priority: Largest|
|SetTargetPriority_Smallest|Set Target Priority: Smallest|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|ActivateBehavior|bool|
|alignment|long|
|AttackPattern|long|
|BackgroundColor|Color|
|CanTargetCharacters|bool|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OffensiveCombatCircleOrbit_CircleDistance|float|
|OffensiveCombatCircleOrbit_CircleInPGravity|bool|
|OffensiveCombatCircleOrbit_FacingBack|bool|
|OffensiveCombatCircleOrbit_FacingDown|bool|
|OffensiveCombatCircleOrbit_FacingFront|bool|
|OffensiveCombatCircleOrbit_FacingLeft|bool|
|OffensiveCombatCircleOrbit_FacingMode|long|
|OffensiveCombatCircleOrbit_FacingRight|bool|
|OffensiveCombatCircleOrbit_FacingUp|bool|
|OffensiveCombatHitAndRun_BreakOffDistance|float|
|OffensiveCombatHitAndRun_RetreatAngle|float|
|OffensiveCombatHitAndRun_RetreatDistance|float|
|OffensiveCombatHitAndRun_RetreatTimeout|float|
|OffensiveCombatIntercept_GuidanceType|long|
|OffensiveCombatIntercept_OverrideCollisionAvoidance|bool|
|OffensiveCombatStayAtRange_EvasiveManeuvers|bool|
|OffensiveCombatStayAtRange_FacingBack|bool|
|OffensiveCombatStayAtRange_FacingDown|bool|
|OffensiveCombatStayAtRange_FacingFront|bool|
|OffensiveCombatStayAtRange_FacingLeft|bool|
|OffensiveCombatStayAtRange_FacingMode|long|
|OffensiveCombatStayAtRange_FacingRight|bool|
|OffensiveCombatStayAtRange_FacingUp|bool|
|OffensiveCombatStayAtRange_MaximalDistance|float|
|OffensiveCombatStayAtRange_MinimalDistance|float|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetingGroup|long|
|TargetLock|long|
|TargetPriority|long|
|TextPaddingSlider|float|
|UpdateInterval|float|

## IMyOreDetector

### Actions

|Name|Description|
|-|-|
|BroadcastUsingAntennas|Broadcast using antennas On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|BroadcastUsingAntennas|bool|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Range|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyOxygenFarm

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyParachute

### Actions

|Name|Description|
|-|-|
|AnyoneCanUse|Anyone Can Use On/Off|
|AutoDeploy|Auto deploy On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|Open| Open/Closed|
|Open_Off| Closed|
|Open_On| Open|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AnyoneCanUse|bool|
|AutoDeploy|bool|
|AutoDeployHeight|float|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|Open|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyPathRecorderBlock

### Actions

|Name|Description|
|-|-|
|ActivateBehavior|AI Behavior On/Off|
|ActivateBehavior_Off|AI Behavior Off|
|ActivateBehavior_On|AI Behavior On|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseID_MINIMAL_DISTANCE_SLIDER|Decrease Minimal distance|
|DecreaseID_RECORD_STEPS_SLIDER|Decrease Record interval|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|ID_ADD_WAYPOINT|Add Waypoint|
|ID_PLAY_CHECKBOX|Play On/Off|
|ID_PLAY_CHECKBOX_Off|Play Off|
|ID_PLAY_CHECKBOX_On|Play On|
|ID_RECORD_CHECKBOX|Record On/Off|
|ID_REPEAT_CHEKBOX|Repeat On/Off|
|ID_REPEAT_CHEKBOX_Off|Repeat Off|
|ID_REPEAT_CHEKBOX_On|Repeat On|
|ID_SHOW_PATH_CHECKBOX|Show path on HUD On/Off|
|ID_SHOW_POINTS_CHECKBOX|Show selected points On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseID_MINIMAL_DISTANCE_SLIDER|Increase Minimal distance|
|IncreaseID_RECORD_STEPS_SLIDER|Increase Record interval|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ReversePath|Reverse order|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|ActivateBehavior|bool|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|ID_MINIMAL_DISTANCE_SLIDER|float|
|ID_PLAY_CHECKBOX|bool|
|ID_RECORD_CHECKBOX|bool|
|ID_RECORD_STEPS_SLIDER|float|
|ID_REPEAT_CHEKBOX|bool|
|ID_SHOW_PATH_CHECKBOX|bool|
|ID_SHOW_POINTS_CHECKBOX|bool|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyPistonBase

### Actions

|Name|Description|
|-|-|
|Add Top Part|Add Piston Head|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseLowerLimit|Decrease Minimum distance|
|DecreaseMaxImpulseAxis|Decrease Max Impulse Axis|
|DecreaseMaxImpulseNonAxis|Decrease Max Impulse NonAxis|
|DecreaseSafetyDetach|Decrease Safety detach|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseUpperLimit|Decrease Maximum distance|
|DecreaseVelocity|Decrease Velocity|
|DecreaseWeld speed|Decrease Safety lock speed|
|Extend|Extend|
|Force weld|Safety lock override On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseLowerLimit|Increase Minimum distance|
|IncreaseMaxImpulseAxis|Increase Max Impulse Axis|
|IncreaseMaxImpulseNonAxis|Increase Max Impulse NonAxis|
|IncreaseSafetyDetach|Increase Safety detach|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseUpperLimit|Increase Maximum distance|
|IncreaseVelocity|Increase Velocity|
|IncreaseWeld speed|Increase Safety lock speed|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ResetVelocity|Reset Velocity|
|Retract|Retract|
|Reverse|Reverse|
|SetAndMove|Set And Move|
|SetVelocity|Set Velocity|
|ShareInertiaTensor|Share inertia tensor On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Force weld|bool|
|LowerLimit|float|
|MaxImpulseAxis|float|
|MaxImpulseNonAxis|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|SafetyDetach|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShareInertiaTensor|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UpperLimit|float|
|Velocity|float|
|Weld speed|float|

## IMyProgrammableBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Run|Run|
|RunWithDefaultArgument|Run with default argument|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|ConsoleCommand|StringBuilder|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyProjector

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRotX|Decrease Pitch|
|DecreaseRotY|Decrease Yaw|
|DecreaseRotZ|Decrease Roll|
|DecreaseScale|Decrease Scale|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseX|Decrease Horizontal offset|
|DecreaseY|Decrease Vertical offset|
|DecreaseZ|Decrease Forward offset|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseRotX|Increase Pitch|
|IncreaseRotY|Increase Yaw|
|IncreaseRotZ|Increase Roll|
|IncreaseScale|Increase Scale|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseX|Increase Horizontal offset|
|IncreaseY|Increase Vertical offset|
|IncreaseZ|Increase Forward offset|
|KeepProjection|Keep Projection On/Off|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|SpawnProjection|Spawn projection|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|GetOwnership|bool|
|InstantBuilding|bool|
|KeepProjection|bool|
|MarkMissingBlocks|bool|
|MarkUnfinishedBlocks|bool|
|Name|StringBuilder|
|NumberOfBlocks|float|
|NumberOfProjections|float|
|OnOff|bool|
|PreserveAspectRatio|bool|
|RotX|float|
|RotY|float|
|RotZ|float|
|Scale|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|ShowOnlyBuildable|bool|
|TextPaddingSlider|float|
|X|float|
|Y|float|
|Z|float|

## IMyRadioAntenna

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRadius|Decrease Broadcast radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableBroadCast|Enable broadcasting On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseRadius|Increase Broadcast radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetHudText|Set HUD Text|
|SetRadius|Set Broadcast Radius|
|ShowShipName|Show ship name On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|CustomName|StringBuilder|
|EnableBroadCast|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|HudText|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Radius|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowShipName|bool|
|TextPaddingSlider|float|

## IMyReactor

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyRefinery

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyReflectorLight

### Actions

|Name|Description|
|-|-|
|DecreaseBlink Interval|Decrease Blink Interval|
|DecreaseBlink Lenght|Decrease Blink Length|
|DecreaseBlink Offset|Decrease Blink Offset|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFalloff|Decrease Falloff|
|DecreaseFontSize|Decrease Font Size|
|DecreaseIntensity|Decrease Intensity|
|DecreaseOffset|Decrease Offset|
|DecreaseRadius|Decrease Radius|
|DecreaseRotationSpeed|Decrease Rotation speed|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseBlink Interval|Increase Blink Interval|
|IncreaseBlink Lenght|Increase Blink Length|
|IncreaseBlink Offset|Increase Blink Offset|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFalloff|Increase Falloff|
|IncreaseFontSize|Increase Font Size|
|IncreaseIntensity|Increase Intensity|
|IncreaseOffset|Increase Offset|
|IncreaseRadius|Increase Radius|
|IncreaseRotationSpeed|Increase Rotation speed|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetBlinkInterval|Set Blink Interval|
|SetColor|Set Color|
|SetRadius|Set Radius|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|Blink Interval|float|
|Blink Lenght|float|
|Blink Offset|float|
|ChangeIntervalSlider|float|
|Color|Color|
|Content|long|
|Falloff|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Intensity|float|
|Name|StringBuilder|
|Offset|float|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Radius|float|
|RotationSpeed|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyRemoteControl

### Actions

|Name|Description|
|-|-|
|AutoPilot|Autopilot On/Off|
|AutoPilot_Off|Autopilot Off|
|AutoPilot_On|Autopilot On|
|Backward|Backward|
|CollisionAvoidance|Collision avoidance On/Off|
|CollisionAvoidance_Off|Collision avoidance Off|
|CollisionAvoidance_On|Collision avoidance On|
|ControlGyros|Control Gyros On/Off|
|ControlThrusters|Control thrusters On/Off|
|ControlWheels|Control wheels On/Off|
|DampenersOverride|Inertia dampeners On/Off|
|DecreaseSpeedLimit|Decrease Speed limit|
|DockingMode|Precision Mode On/Off|
|DockingMode_Off|Precision Mode Off|
|DockingMode_On|Precision Mode On|
|Down|Down|
|Forward|Forward|
|HandBrake|Handbrake On/Off|
|HorizonIndicator|Show horizon and altitude On/Off|
|IncreaseSpeedLimit|Increase Speed limit|
|Left|Left|
|MainCockpit|Main cockpit On/Off|
|MainRemoteControl|Main Remote Control On/Off|
|Park|Park On/Off|
|Reset|Reset waypoint|
|Right|Right|
|SetFlightMode_BlockPropertyTitle_FlightMode_Circle|Set Flight Mode: Circle|
|SetFlightMode_BlockPropertyTitle_FlightMode_OneWay|Set Flight Mode: One Way|
|SetFlightMode_BlockPropertyTitle_FlightMode_Patrol|Set Flight Mode: Patrol|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TargetLocking|Enable target locking On/Off|
|Up|Up|

### Properties

|Name|Type|
|-|-|
|AutoPilot|bool|
|CameraList|long|
|CollisionAvoidance|bool|
|ControlGyros|bool|
|ControlThrusters|bool|
|ControlWheels|bool|
|DampenersOverride|bool|
|Direction|long|
|DockingMode|bool|
|FlightMode|long|
|HandBrake|bool|
|HorizonIndicator|bool|
|MainCockpit|bool|
|MainRemoteControl|bool|
|Name|StringBuilder|
|Park|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|SpeedLimit|float|
|TargetLocking|bool|

## IMySafeZoneBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseSafeZoneXSlider|Decrease Set Width|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseSafeZoneXSlider|Increase Set Width|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|SafeZoneBuildingCb|bool|
|SafeZoneBuildingProjectionCb|bool|
|SafeZoneColor|Color|
|SafeZoneConvertToStationCb|bool|
|SafeZoneCreate|bool|
|SafeZoneDamageCb|bool|
|SafeZoneDrillingCb|bool|
|SafeZoneGrindingCb|bool|
|SafeZoneLandingGearCb|bool|
|SafeZoneShapeCombo|long|
|SafeZoneShootingCb|bool|
|SafeZoneSlider|float|
|SafeZoneTextureCombo|long|
|SafeZoneVoxelHandCb|bool|
|SafeZoneWeldingCb|bool|
|SafeZoneXSlider|float|
|SafeZoneYSlider|float|
|SafeZoneZSlider|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMySearchlight

### Actions

|Name|Description|
|-|-|
|DecreaseBlink Interval|Decrease Blink Interval|
|DecreaseBlink Lenght|Decrease Blink Length|
|DecreaseBlink Offset|Decrease Blink Offset|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFalloff|Decrease Falloff|
|DecreaseFontSize|Decrease Font Size|
|DecreaseIntensity|Decrease Intensity|
|DecreaseOffset|Decrease Offset|
|DecreaseRadius|Decrease Radius|
|DecreaseRange|Decrease AI aiming radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableIdleMovement|Enable idle movement On/Off|
|EnableIdleMovement_Off|Enable idle movement Off|
|EnableIdleMovement_On|Enable idle movement On|
|EnableTargetLocking|Enable target locking On/Off|
|FocusLockedTarget|Focus Locked Target|
|IncreaseBlink Interval|Increase Blink Interval|
|IncreaseBlink Lenght|Increase Blink Length|
|IncreaseBlink Offset|Increase Blink Offset|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFalloff|Increase Falloff|
|IncreaseFontSize|Increase Font Size|
|IncreaseIntensity|Increase Intensity|
|IncreaseOffset|Increase Offset|
|IncreaseRadius|Increase Radius|
|IncreaseRange|Increase AI aiming radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetBlinkInterval|Set Blink Interval|
|SetColor|Set Color|
|SetRadius|Set Radius|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TargetCharacters|Target characters On/Off|
|TargetCharacters_Off|Target characters Off|
|TargetCharacters_On|Target characters On|
|TargetEnemies|Target Enemies On/Off|
|TargetEnemies_Off|Target Enemies Off|
|TargetEnemies_On|Target Enemies On|
|TargetFriends|Target Friends On/Off|
|TargetFriends_Off|Target Friends Off|
|TargetFriends_On|Target Friends On|
|TargetingGroup_CycleSubsystems|Cycle Subsystems|
|TargetingGroup_PowerSystems|Target Power systems|
|TargetingGroup_Propulsion|Target Propulsion|
|TargetingGroup_Weapons|Target Weapons|
|TargetLargeShips|Target large ships On/Off|
|TargetLargeShips_Off|Target large ships Off|
|TargetLargeShips_On|Target large ships On|
|TargetMeteors|Target meteors On/Off|
|TargetMeteors_Off|Target meteors Off|
|TargetMeteors_On|Target meteors On|
|TargetMissiles|Target rockets On/Off|
|TargetMissiles_Off|Target rockets Off|
|TargetMissiles_On|Target rockets On|
|TargetNeutrals|Target neutrals On/Off|
|TargetNeutrals_Off|Target neutrals Off|
|TargetNeutrals_On|Target neutrals On|
|TargetSmallShips|Target small ships On/Off|
|TargetSmallShips_Off|Target small ships Off|
|TargetSmallShips_On|Target small ships On|
|TargetStations|Target stations On/Off|
|TargetStations_Off|Target stations Off|
|TargetStations_On|Target stations On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|Blink Interval|float|
|Blink Lenght|float|
|Blink Offset|float|
|ChangeIntervalSlider|float|
|Color|Color|
|Content|long|
|EnableIdleMovement|bool|
|EnableTargetLocking|bool|
|Falloff|float|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Intensity|float|
|Name|StringBuilder|
|Offset|float|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Radius|float|
|Range|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TargetCharacters|bool|
|TargetEnemies|bool|
|TargetFriends|bool|
|TargetingGroup_Selector|long|
|TargetLargeShips|bool|
|TargetMeteors|bool|
|TargetMissiles|bool|
|TargetNeutrals|bool|
|TargetSmallShips|bool|
|TargetStations|bool|
|TextPaddingSlider|float|

## IMySensorBlock

### Actions

|Name|Description|
|-|-|
|DecreaseBack|Decrease Back extent|
|DecreaseBottom|Decrease Bottom extent|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseFront|Decrease Front extent|
|DecreaseLeft|Decrease Left extent|
|DecreaseRight|Decrease Right extent|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseTop|Decrease Top extent|
|Detect Asteroids|Detect asteroids On/Off|
|Detect Asteroids_Off|Detect asteroids Off|
|Detect Asteroids_On|Detect asteroids On|
|Detect Enemy|Detect enemy On/Off|
|Detect Enemy_Off|Detect enemy Off|
|Detect Enemy_On|Detect enemy On|
|Detect Floating Objects|Detect floating objects On/Off|
|Detect Floating Objects_Off|Detect floating objects Off|
|Detect Floating Objects_On|Detect floating objects On|
|Detect Friendly|Detect friendly On/Off|
|Detect Friendly_Off|Detect friendly Off|
|Detect Friendly_On|Detect friendly On|
|Detect Large Ships|Detect large ships On/Off|
|Detect Large Ships_Off|Detect large ships Off|
|Detect Large Ships_On|Detect large ships On|
|Detect Neutral|Detect neutral On/Off|
|Detect Neutral_Off|Detect neutral Off|
|Detect Neutral_On|Detect neutral On|
|Detect Owner|Detect owner On/Off|
|Detect Owner_Off|Detect owner Off|
|Detect Owner_On|Detect owner On|
|Detect Players|Detect players On/Off|
|Detect Players_Off|Detect players Off|
|Detect Players_On|Detect players On|
|Detect Small Ships|Detect small ships On/Off|
|Detect Small Ships_Off|Detect small ships Off|
|Detect Small Ships_On|Detect small ships On|
|Detect Stations|Detect stations On/Off|
|Detect Stations_Off|Detect stations Off|
|Detect Stations_On|Detect stations On|
|Detect Subgrids|Detect subgrids On/Off|
|Detect Subgrids_Off|Detect subgrids Off|
|Detect Subgrids_On|Detect subgrids On|
|IncreaseBack|Increase Back extent|
|IncreaseBottom|Increase Bottom extent|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseFront|Increase Front extent|
|IncreaseLeft|Increase Left extent|
|IncreaseRight|Increase Right extent|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseTop|Increase Top extent|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetBack|Set Sensor Back Extent|
|SetBottom|Set Sensor Bottom Extent|
|SetFront|Set Sensor Front Extent|
|SetLeft|Set Sensor Left Extent|
|SetRight|Set Sensor Right Extent|
|SetTop|Set Sensor Top Extent|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|Audible Proximity Alert|bool|
|Back|float|
|BackgroundColor|Color|
|Bottom|float|
|ChangeIntervalSlider|float|
|Content|long|
|Detect Asteroids|bool|
|Detect Enemy|bool|
|Detect Floating Objects|bool|
|Detect Friendly|bool|
|Detect Large Ships|bool|
|Detect Neutral|bool|
|Detect Owner|bool|
|Detect Players|bool|
|Detect Small Ships|bool|
|Detect Stations|bool|
|Detect Subgrids|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Front|float|
|Left|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Right|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|Top|float|

## IMyShipConnector

### Actions

|Name|Description|
|-|-|
|CollectAll|Collect All On/Off|
|CollectAll_Off|Collect All Off|
|CollectAll_On|Collect All On|
|DecreaseAutoUnlockTime|Decrease Autounlock Time|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseStrength|Decrease Strength|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableParking|Used for parking On/Off|
|IncreaseAutoUnlockTime|Increase Autounlock Time|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseStrength|Increase Strength|
|IncreaseTextPaddingSlider|Increase Text Padding|
|Lock|Lock|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PowerTransferOverride|Override Power Transfer On/Off|
|PowerTransferOverride_Off|Override Power Transfer Off|
|PowerTransferOverride_On|Override Power Transfer On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|SwitchLock|Switch lock|
|ThrowOut|Throw Out On/Off|
|ThrowOut_Off|Throw Out Off|
|ThrowOut_On|Throw Out On|
|Trading|Trading Mode On/Off|
|Trading_Off|Trading Mode Off|
|Trading_On|Trading Mode On|
|Unlock|Unlock|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AutoUnlockTime|float|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|CollectAll|bool|
|Content|long|
|EnableParking|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PowerTransferOverride|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|Strength|float|
|TextPaddingSlider|float|
|ThrowOut|bool|
|Trading|bool|

## IMyShipDrill

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|TerrainClearingMode|Terrain Clearing Mode On/Off|
|TerrainClearingMode_Off|Terrain Clearing Mode Off|
|TerrainClearingMode_On|Terrain Clearing Mode On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TerrainClearingMode|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyShipGrinder

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyShipMergeBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyShipWelder

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|helpOthers|Help Others On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|helpOthers|bool|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMySmallGatlingGun

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Shoot|Shoot On/Off|
|Shoot_Off|Shoot Off|
|Shoot_On|Shoot On|
|ShootOnce|Shoot once|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|Shoot|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMySmallMissileLauncher

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Shoot|Shoot On/Off|
|Shoot_Off|Shoot Off|
|Shoot_On|Shoot On|
|ShootOnce|Shoot once|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|Shoot|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMySmallMissileLauncherReload

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|Shoot|Shoot On/Off|
|Shoot_Off|Shoot Off|
|Shoot_On|Shoot On|
|ShootOnce|Shoot once|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|Shoot|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|
|UseConveyor|bool|

## IMySolarPanel

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMySoundBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseLoopableSlider|Decrease Loop time|
|DecreaseRangeSlider|Decrease Range|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseVolumeSlider|Decrease Volume|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseLoopableSlider|Increase Loop time|
|IncreaseRangeSlider|Increase Range|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseVolumeSlider|Increase Volume|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PlaySound|Play|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|StopSound|Stop|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|LoopableSlider|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|RangeSlider|float|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|VolumeSlider|float|

## IMySpaceBall

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseVirtualMass|Decrease Virtual mass|
|EnableBroadCast|Enable broadcasting On/Off|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseVirtualMass|Increase Virtual mass|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|EnableBroadCast|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|VirtualMass|float|

## IMyStoreBlock

### Actions

|Name|Description|
|-|-|
|AnyoneCanUse|Anyone Can Use On/Off|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|UseConveyor|Automatic Push/Pull On/Off|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|AnyoneCanUse|bool|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|UseConveyor|bool|

## IMyTargetDummyBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseDelay|Decrease Regeneration delay|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseDelay|Increase Regeneration delay|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Delay|float|
|Enable Restoration|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyTerminalBlock

### Actions

|Name|Description|
|-|-|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|Name|StringBuilder|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|

## IMyTextPanel

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseFontSize|Decrease Font Size|
|DecreaseRotate|Decrease Rotation|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseFontSize|Increase Font Size|
|IncreaseRotate|Increase Rotation|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|alignment|long|
|BackgroundColor|Color|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|ChangeIntervalSlider|float|
|Content|long|
|Content|long|
|Font|long|
|Font|long|
|FontColor|Color|
|FontColor|Color|
|FontSize|float|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|PreserveAspectRatio|bool|
|Rotate|float|
|ScriptBackgroundColor|Color|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|
|TextPaddingSlider|float|
|Title|StringBuilder|

## IMyThrust

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseOverride|Decrease Thrust override|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseOverride|Increase Thrust override|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetOverride|Set Override Percentage|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|Override|float|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyTimerBlock

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|DecreaseTriggerDelay|Decrease Delay|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|IncreaseTriggerDelay|Increase Delay|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|Silent|Silent On/Off|
|Start|Start|
|Stop|Stop|
|TriggerNow|Trigger now|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|Silent|bool|
|TextPaddingSlider|float|
|TriggerDelay|float|

## IMyTransponder

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseChannel|Decrease Channel|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseChannel|Increase Channel|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SendSignal|Send Signal|
|SetChannelValue|Set Channel|
|SetChannelValue_SendSignal|Set Channel and Send Signal|
|SetFilter_Everyone|Enable Everyone|
|SetFilter_Faction|Enable Faction Only|
|SetFilter_Owner|Enable Owner Only|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Channel|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ReceiveFrom|long|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyTurretControlBlock

### Actions

|Name|Description|
|-|-|
|AI|Enable AI On/Off|
|AI_Off|Enable AI Off|
|AI_On|Enable AI On|
|DecreaseAngleDeviation|Decrease Angle deviation|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseMultiplierAz|Decrease Azimuth velocity multiplier|
|DecreaseMultiplierEl|Decrease Elevation velocity multiplier|
|DecreaseRange|Decrease AI aiming radius|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|EnableIdleMovement|Enable idle movement On/Off|
|EnableIdleMovement_Off|Enable idle movement Off|
|EnableIdleMovement_On|Enable idle movement On|
|EnableTargetLocking|Enable target locking On/Off|
|FocusLockedTarget|Focus Locked Target|
|IncreaseAngleDeviation|Increase Angle deviation|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseMultiplierAz|Increase Azimuth velocity multiplier|
|IncreaseMultiplierEl|Increase Elevation velocity multiplier|
|IncreaseRange|Increase AI aiming radius|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|SetAngleDeviation|Set Angle Deviation|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|SunTracking|Always aim at sun On/Off|
|SunTracking_Off|Always aim at sun Off|
|SunTracking_On|Always aim at sun On|
|TargetCharacters|Target characters On/Off|
|TargetCharacters_Off|Target characters Off|
|TargetCharacters_On|Target characters On|
|TargetEnemies|Target Enemies On/Off|
|TargetEnemies_Off|Target Enemies Off|
|TargetEnemies_On|Target Enemies On|
|TargetFriends|Target Friends On/Off|
|TargetFriends_Off|Target Friends Off|
|TargetFriends_On|Target Friends On|
|TargetingGroup_CycleSubsystems|Cycle Subsystems|
|TargetingGroup_PowerSystems|Target Power systems|
|TargetingGroup_Propulsion|Target Propulsion|
|TargetingGroup_Weapons|Target Weapons|
|TargetLargeShips|Target large ships On/Off|
|TargetLargeShips_Off|Target large ships Off|
|TargetLargeShips_On|Target large ships On|
|TargetMeteors|Target meteors On/Off|
|TargetMeteors_Off|Target meteors Off|
|TargetMeteors_On|Target meteors On|
|TargetMissiles|Target rockets On/Off|
|TargetMissiles_Off|Target rockets Off|
|TargetMissiles_On|Target rockets On|
|TargetNeutrals|Target neutrals On/Off|
|TargetNeutrals_Off|Target neutrals Off|
|TargetNeutrals_On|Target neutrals On|
|TargetSmallShips|Target small ships On/Off|
|TargetSmallShips_Off|Target small ships Off|
|TargetSmallShips_On|Target small ships On|
|TargetStations|Target stations On/Off|
|TargetStations_Off|Target stations Off|
|TargetStations_On|Target stations On|

### Properties

|Name|Type|
|-|-|
|AI|bool|
|alignment|long|
|AngleDeviation|float|
|BackgroundColor|Color|
|CameraList|long|
|ChangeIntervalSlider|float|
|Content|long|
|EnableIdleMovement|bool|
|EnableTargetLocking|bool|
|Font|long|
|FontColor|Color|
|FontSize|float|
|MultiplierAz|float|
|MultiplierEl|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|Range|float|
|RotorAzimuth|long|
|RotorElevation|long|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|SunTracking|bool|
|TargetCharacters|bool|
|TargetEnemies|bool|
|TargetFriends|bool|
|TargetingGroup_Selector|long|
|TargetLargeShips|bool|
|TargetMeteors|bool|
|TargetMissiles|bool|
|TargetNeutrals|bool|
|TargetSmallShips|bool|
|TargetStations|bool|
|TextPaddingSlider|float|

## IMyUpgradeModule

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

## IMyWarhead

### Actions

|Name|Description|
|-|-|
|DecreaseDetonationTime|Decrease Detonation time|
|Detonate|Detonate|
|IncreaseDetonationTime|Increase Detonation time|
|Safety|Arm warhead On/Off|
|Safety_Off|Arm warhead Off|
|Safety_On|Arm warhead On|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|
|StartCountdown|Start countdown|
|StopCountdown|Stop countdown|

### Properties

|Name|Type|
|-|-|
|DetonationTime|float|
|Name|StringBuilder|
|Safety|bool|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|

## IMyWindTurbine

### Actions

|Name|Description|
|-|-|
|DecreaseChangeIntervalSlider|Decrease Image change interval|
|DecreaseFontSize|Decrease Font Size|
|DecreaseTextPaddingSlider|Decrease Text Padding|
|IncreaseChangeIntervalSlider|Increase Image change interval|
|IncreaseFontSize|Increase Font Size|
|IncreaseTextPaddingSlider|Increase Text Padding|
|OnOff|Toggle block On/Off|
|OnOff_Off|Toggle block Off|
|OnOff_On|Toggle block On|
|PreserveAspectRatio|Preserve aspect ratio On/Off|
|ShowOnHUD|Show on HUD On/Off|
|ShowOnHUD_Off|Show on HUD Off|
|ShowOnHUD_On|Show on HUD On|

### Properties

|Name|Type|
|-|-|
|alignment|long|
|BackgroundColor|Color|
|ChangeIntervalSlider|float|
|Content|long|
|Font|long|
|FontColor|Color|
|FontSize|float|
|Name|StringBuilder|
|OnOff|bool|
|PreserveAspectRatio|bool|
|ScriptBackgroundColor|Color|
|ScriptForegroundColor|Color|
|ShowInInventory|bool|
|ShowInTerminal|bool|
|ShowInToolbarConfig|bool|
|ShowOnHUD|bool|
|TextPaddingSlider|float|

