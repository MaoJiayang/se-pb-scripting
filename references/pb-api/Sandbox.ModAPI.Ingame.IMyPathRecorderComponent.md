**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyPathRecorderComponent
```

Ingame interfave for PB and mods

## Properties

|Member|Description|
|---|---|
|[BeaconDisplayText](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@BeaconDisplayText)|Gets Beacon display text|
|[BeaconEntityId](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@BeaconEntityId)|Entity of beacon in which the waypoints are in relation to|
|[BeaconWorldPosition](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@BeaconWorldPosition)|Gets BeaconWorldPosition|
|[IsPlaying](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@IsPlaying)|Gets bool if the PR block is playing|
|[IsRecording](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@IsRecording)|Get bool if the PR block is recording|
|[MinimalDistance](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@MinimalDistance)|Gets/sets minimal distance between waypoints for automatic recording to record new waypoint|
|[RecordInterval](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@RecordInterval)|Gets/sets record interval. Sets how often the block tries to records its position as a waypoint. Operates every 100 frames|
|[RepeatPath](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@RepeatPath)|Repeat path toggle|
|[ShowPath](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@ShowPath)|Gets/sets if block is showing path on clients screen|
|[ShowSelectedPoints](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@ShowSelectedPoints)|Gets/sets if block is showing points, selected by client on his screen|

## Methods

|Member|Description|
|---|---|
|[Play()](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@Play)|Starts playing current waypoints|
|[Record()](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@Record)|Starts recording|
|[RemoveBeacon()](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@RemoveBeacon)|Sets BeaconEntityId = 0|
|[StopPlay()](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@StopPlay)|Stops playing current waypoints|
|[StopRecord()](Sandbox.ModAPI.Ingame.IMyPathRecorderComponent@StopRecord)|Stops recording|

