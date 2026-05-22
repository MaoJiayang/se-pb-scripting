**Assembly:** Sandbox.Common.dll

```csharp
public interface IMyChatBroadcastControllerComponent
```

Describes entity component for broadcast controller

## Properties

|Member|Description|
|---|---|
|[BroadcastTarget](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@BroadcastTarget)|Gets or sets target for messages send from broadcast controller|
|[CustomName](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@CustomName)|Custom name that will be visible in chat|
|[MaxMessageCount](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@MaxMessageCount)|Number of messages that can be stored in this broadcast controller|
|[UseAntenna](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@UseAntenna)|Determines if broadcast controller should try to use antenna for broadcasting messages or sent message only to local cube grid|

## Methods

|Member|Description|
|---|---|
|[GetMessage(int)](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@GetMessage)|Gets message at given index|
|[SendGps()](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@SendGps)|Sends current position as a message|
|[SendMessage(int)](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@SendMessage)|Sends message|
|[SendMessage(string)](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@SendMessage)|Sends custom message|
|[SendRandomMessage()](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@SendRandomMessage)|Sends randomly one of stored messages|
|[SetMessage(int, string)](Sandbox.ModAPI.Ingame.IMyChatBroadcastControllerComponent@SetMessage)|Sets message at given index|

