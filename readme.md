This will interpret messages from node-red and convert them into clicks and keyboard presses

requirements:
pip install keyboard
update the myPath in the constants class. (this can be anywhere but I recommend making it the same folder as this script + /output.txt)

have the corresponding flow for node-red running and use the command
run this command: node-red > myPath
open the local server: http://127.0.0.1:1880/