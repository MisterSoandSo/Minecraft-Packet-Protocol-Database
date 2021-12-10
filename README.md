# Minecraft Packet Protocol Database
 Parsed Protocol Numbers from https://wiki.vg/Protocol_version_numbers

The purpose of this project is to make it easier for modders and client developers to reference Minecraft Protocol numbers in a simple and easy to use fashion. The protocol numbers are stored in a similar structure provided by the wiki.vg documentation website.
All credits for protocol documentation goes to the them, I'm just parsing their information into a json files that can be used for future devlopement and reference.

## Version Changelogs
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
###### ~~~ To be documented on a later date ~~~
