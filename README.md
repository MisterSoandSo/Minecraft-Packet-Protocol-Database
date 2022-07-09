# Minecraft Packet Protocol Database
 Parsed Protocol Numbers from https://wiki.vg/Protocol_version_numbers

The purpose of this project is to make it easier for modders and client developers to reference Minecraft Protocol numbers in a simple and easy to use fashion. The protocol numbers are stored in a similar structure provided by the wiki.vg documentation website.
All credits for protocol documentation goes to the them, I'm just parsing their information into a json files that can be used for future devlopement and reference.

## Version Changelogs
### 1.19+
#### Renamed
- 0x04 `Statistics` renamed to `Award Statistics`
- 0x05 `Acknowledge Player Digging` renamed to `Acknowledge Block Change`
- 0x06 `Block Break Animation` renamed to `Set Block Destroy Stage`
- 0x09 `Block Change` renamed to `Block Update`
- 0x0E `Tab-Complete` renamed to `Command Suggestions Response`
- 0x0F `Declare Commands` renamed to `Commands`
- 0x10 `Close Window` renamed to `Close Container`
- 0x11 `Window Items` renamed to `Set Container Content`
- 0x12 `Window Property` renamed to `Set Container Property`
- 0x13 `Set Slot` renamed to `Set Container Slot`
- 0x16 `Named Sound Effect` renamed to `Custom Sound Effect`
- 0x18 `Entity Status` renamed to `Entity Event`
- 0x1B `Change Game State` renamed to `Game Event`
- 0x1C `Open Horse Window` renamed to `Open Horse Screen`
- 0x20 `Effect` renamed to `World Event`
- 0x23 `Join Game` renamed to `Login`
- 0x25 `Trade List` renamed to `Merchant Offers`
- 0x26 `Entity Position` renamed to `Update Entity Position`
- 0x27 `Update Entity Position and Rotation` renamed to `Update Entity Position and Rotation`
- 0x28 `Entity Rotation` renamed to `Update Entity Rotation`
- 0x29 `Vehicle Move ` renamed to `Move Vehicle`
- 0x2B `Open Window` renamed to `Open Screen`
- 0x2E `CraftRecipeResponse` renamed to `Place Ghost Recipe`
- 0x33 `Death Combat` renamed to `Combat Death`
- 0x35 `Face Player` renamed to `Look At`
- 0x36 `Player Position And Look ` renamed to `Synchronize Player Position`
- 0x37 `Unlock Recipes` renamed to `Unlock Recipe Book`
- 0x38 `Destroy Entities` renamed to `Remove Entities`
- 0x3A `Resource Pack Send` renamed to `Resource Pack`
- 0x3C `Entity Head Look` renamed to `Set Head Rotation`
- 0x3D `Multi Block Change` renamed to `Update Section Blocks`
- 0x40 `Action Bar` renamed to `Set Action Bar Text`
- 0x41 `World Border Center` renamed to `Set Border Center`
- 0x42 `World Border Lerp Size` renamed to `Set Border Lerp Size`
- 0x43 `World Border Size` renamed to `Set Border Size`
- 0x44 `World Border Warning Delay` renamed to `Set Border Warning Delay`
- 0x45 `World Border Warning Reach` renamed to `Set Border Warning Distance`
- 0x46 `Camera` renamed to `Set Camera`
- 0x47 `Held Item Change` renamed to `Set Held Item`
- 0x48 `Update View Position` renamed to `Set Center Chunk`
- 0x49 `Update View Distance` renamed to `Set Render Distance`
- 0x4A `Spawn Position` renamed to `Set Default Spawn Position`
- 0x4C `Display Scoreboard` renamed to `Display Objective`
- 0x4D `Entity Metadata` renamed to `Set Entity Metadata`
- 0x4E `Attach Entity` renamed to `Link Entities`
- 0x4F `Entity Velocity` renamed to `Set Entity Velocity`
- 0x50 `Entity Equipment` renamed to `Set Equipment`
- 0x51 `Experience` renamed to `Set Experience`
- 0x52 `Update Health` renamed to `Set Health`
- 0x53 `Scoreboard Objective` renamed to `Update Objectives`
- 0x55 `Teams` renamed to `Update Teams`
- 0x57 `Update Simulation Distance` renamed to `Set Simulation Distance`
- 0x58 `Set Title SubTitle` renamed to `Set Subtitle Text`
- 0x59 `Time Update` renamed to `Update Time`
- 0x5B `Set Title Times` renamed to `Set Title Animation Times`
- 0x60 `Player List Header And Footer` renamed to `Set Tab List Header And Footer`
- 0x61 `NBT Query Response` renamed to `Tag Query Response`
- 0x62 `Collect Item` renamed to `Pickup Item`
- 0x63 `Entity Teleport` renamed to `Teleport Entity`
- 0x64 `Advancements` renamed to `Update Advancements`
- 0x65 `Entity Properties` renamed to `Update Attributes`
- 0x67 `Declare Recipes` renamed to `Update Recipes`
- 0x68 `Tags` renamed to `Update Tags`


- 0x00 `Teleport Confirm` renamed to `Confirm Teleportation`
- 0x02 `Set Difficulty` renamed to `Change Difficulty`
- 0x03 `Chat Message (serverbound)` renamed to `Chat Command`
- 0x06 `Client Status` renamed to `Client Command`
- 0x07 `Client Settings` renamed to `Client Information`
- 0x08 `Tab-Complete` renamed to `Command Suggestions Request`
- 0x09 `Click Window Button` renamed to `Click Container Button`
- 0x0A `Click Window` renamed to `Click Container`
- 0x0B `Close Window` renamed to `Close Container`
- 0x0E `Query Entity NBT` renamed to `Query Entity Tag`
- 0x0F `Interact Entity` renamed to `Interact`
- 0x10 `Generate Structure` renamed to `Jigsaw Generate`
- 0x13 `Player Position` renamed to `Set Player Position`
- 0x14 `Player Position and Rotation` renamed to `Set Player Position and Rotation`
- 0x15 `Player Rotation` renamed to `Set Player Rotation`
- 0x16 `Player Movement` renamed to `Set Player On Ground`
- 0x17 `Vehicle Move ` renamed to `Move Vehicle`
- 0x18 `Steer Boat` renamed to `Paddle Boat`
- 0x1A `Craft Recipe Request` renamed to `Place Recipe`
- 0x1C `Player Digging` renamed to `Player Action`
- 0x1D `Entity Action` renamed to `Player Command`
- 0x1E `Steer Vehicle` renamed to `Player Input`
- 0x20 `Set Recipe Book State` renamed to `Change Recipe Book Settings`
- 0x21 `Set Displayed Recipe` renamed to `Set Seen Recipe`
- 0x22 `Name Item` renamed to `Rename Item`
- 0x23 `Resource Pack Status` renamed to `Resource Pack`
- 0x24 `Advancement Tab` renamed to `Seen Advancements`
- 0x27 `Held Item` renamed to `Set Held Item`
- 0x28 `Update Command Block` renamed to `Program Command Block`
- 0x29 `Update Command Block Minecart` renamed to `Program Command Block Minecart`
- 0x2A `Creative Inventory Action` renamed to `Set Creative Mode Slot`
- 0x2B `Update Jigsaw Block` renamed to `Program Jigsaw Block`
- 0x2C `Update Structure Block` renamed to `Program Structure Block`
- 0x2E `Animation` renamed to `Swing Arm`
- 0x2F `Spectate` renamed to `Teleport To Entity`
- 0x30 `Player Block Placement` renamed to `Use Item On`


#### Added
- 0x0C - Chat Preview
- 0x30 - Player Chat Message
- 0x3F - Server Data
- 0x4B - Set Display Chat Preview

- 0x04 - Chat Message
- 0x05 - Chat Preview (serverbound)
#### Removed
- 0x02 - Spawn Living Entity
- 0x03 - Spawn Painting
- 0x05 - Sculk Vibration Signal
- 0x0F - Chat Message `Legacy <= 1.18.2 Packet`


### 1.18+
#### Renamed
- 0X22 `Chunk Data` renamed to `Chunk Data and Update Light`
#### Added
- 0x57 - Update Simulated Distance

### 1.17+
#### Added
- 0x05 - Sculk Vibration Signal
- 0x0F - Clear Titles
- 0x1F - Initialize World Border
- 0x30 - Ping
- 0x33 - End Combat Event
- 0x34 - Enter Combat Event
- 0x35 - Death Combat Event
- 0x41 - Action Bar
- 0x42 - World Border Center
- 0x43 - World Border Lerp Size
- 0x44 - World Border Size
- 0x45 - World Border Warning Delay
- 0x46 - World Border Warning Reach
- 0x57 - Set Title SubTitle
- 0x59 - Set Title Text
- 0x5A - Set Title Times

- 0x07 - Click Window Button 
- 0x1D - Pong

#### Removed
- 0x11 - Window Confirmation
- 0x2A - Entity Movement
- 0x31 - Combat Event
- 0x3D - World Border
- 0x4F - Title

- 0x07 - Window Confirmation (serverbound)
- 0x08 - Click Window Button

### Pre 1.16.5
###### ~~~ To be documented on a later date ~~~ Probably not gonna happen ... -_- 
