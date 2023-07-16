# Minecraft Packet Protocol Database
 Parsed Protocol Numbers from https://wiki.vg/Protocol_version_numbers

The purpose of this project is to make it easier for modders and client developers to reference Minecraft Protocol numbers in a simple and easy to use fashion. The protocol numbers are stored in a similar structure provided by the wiki.vg documentation website.
All credits for protocol documentation goes to the them, I'm just parsing their information into a json files that can be used for future devlopement and reference.

## Usage
To run the script, provide the link and version numder for filename. Input when prompted.
```
python main.py
Url Link: https://wiki.vg/index.php?title=Protocol&oldid=18242
Version Number: 762
```

## Setup Virtual Environment
In the console or terminal, type `python -m venv venv` to initialize the python virtual environment. In linux, you might have to run `sudo apt update && apt update -y` to install pip for later uses.
```
# Windows Users
.\venv\Scripts\activate

# Unix/ Mac Users
source venv/bin/activate

# Exit venv Command
deactivate

```

## Requirements
Using ``pip install -r requirements.txt`` should cover everything.

## License
This project is licensed under the GNU v3 License.