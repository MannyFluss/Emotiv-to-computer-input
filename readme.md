Author

Manny Fluss

Description:
This will interpret emotiv-bci commands from the node-red library and convert them into clicks and keyboard presses

requirements:

    -python3 https://www.python.org/downloads/ 
    -pip install keyboard
    -pip install pydirectinput
    -download and install [node-red] (https://nodered.org/docs/getting-started/local)
    -download and install the [emotiv launcher](https://flows.nodered.org/node/node-red-contrib-emotiv-bci) and its [node red components](https://www.emotiv.com/emotiv-launcher/)

instructions for use:

    -open nodeRedInterpreter.py
    -update the myPath in the constants class to your desired location. 
        -(this can be anywhere but I recommend making it the same folder as this script + /output.txt)
    -open a terminal and run the following command : node-red > (the myPath put into the script)
    -open the local server in your browser : http://127.0.0.1:1880/
    -run nodeRedInterpreter.py
    -in the node-red flow, there are two buttons to enable and disable input from flowing, if you press enable, after 5 seconds input will flow
    -press the kill switch key to turn off this script at any time. (default binding is '/')
    -you can edit the script in order to get different functionality from different commands, or change the hotkey for the killswitch

 Extra:

    technically this program is doomed to fail after the output.txt gets too large, to prevent this delete the output.txt when you arent using the program