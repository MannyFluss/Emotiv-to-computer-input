## Description
This program interprets emotiv-bci commands from the node-red library and converts them into clicks and keyboard presses.

## Requirements
- Python3
- keyboard
- pydirectinput 
- Node-RED
- Emotiv Launcher and its Node-RED components

## Instructions for Use
1. Open `nodeRedInterpreter.py`.
2. Update the `myPath` in the `Constants` class to your desired location.
3. Open a terminal and run the following command: `node-red > (the myPath put into the script)`.
4. Open the local server in your browser: `http://127.0.0.1:1880/`.
5. Run `nodeRedInterpreter.py`.
6. In the Node-RED flow, there are two buttons to enable and disable input from flowing. If you press enable, after 5 seconds input will flow.
7. Press the kill switch key to turn off this script at any time (default binding is `/`).
8. You can edit the script to get different functionality from different commands or change the hotkey for the killswitch.

Note: This program started as a Node-RED program that transferred to a Python project. The data stream can be replicated here: https://github.com/Emotiv/cortex-v2-example/tree/master/python.
