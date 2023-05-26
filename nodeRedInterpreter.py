import keyboard
import time
import re
from pynput.mouse import Button, Controller

class constants:
    pollRate = .1
    killSwitch = '/'
    mouseSensitivityMult = 1
    #myPathAlt = "C:/Users/manny/AppData/Roaming/npm/node-red"

command_to_key = {
"neutral" : {"input":"","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"push" : {"input":"b","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"pull" : {"input":"c","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"lift" : {"input":"d","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"drop" : {"input":"e","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"left" : {"input":"f","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"right" : {"input":"g","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"rotateRight" : {"input":"h","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"rotateLeft" : {"input":"i","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"rotateCounterClockwise" : {"input":"j","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"rotateClockwise" : {"input":"k","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"rotateReverse" : {"input":"l","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"rotateForwards" : {"input":"m","mouseControl":False,"mouseDxDy":(1.0,1.0)},
"disappear" : {"letter":"n","mouseControl":False,"mouseDxDy":(1.0,1.0)},
}
last_key_pressed = ""
curr_key_pressed = ""
mouse = Controller()
def main():
    myPath = "" 
    with open('myPathInfo.txt', 'r') as file:
        myPath = file.read()
    global curr_key_pressed
    global last_key_pressed
    while(True):
        if last_key_pressed != curr_key_pressed:
            if curr_key_pressed != "":
                keyboard.press(curr_key_pressed)
            if last_key_pressed != "":
                keyboard.release(last_key_pressed)
        

        if keyboard.is_pressed(constants.killSwitch):
            break
        with open(myPath, "r", encoding='utf-16') as f:
            lines = f.readlines()
            if (lines == []):
                time.sleep(constants.pollRate)
                continue        
            pollInput(lines[-1])
        time.sleep(constants.pollRate)

def pollInput(_line : str):
    pattern = r'\[info\] \[debug:debug \d+\] (\w+),(\d+)'
    validLine = re.search(pattern,_line)
    if not validLine:
        print("invalid line")
        return
    matches = re.findall(pattern,_line)
    mouseControl = command_to_key[matches[0][0]]["mouseControl"]
    if mouseControl == True:
        thoughtToMouseMovement(matches[0][0],int(matches[0][1]))
    else:
        thoughtToKeyPress(matches[0][0])
    

def thoughtToMouseMovement(_command, _thinkingIntensity):
    print("debug statement 1")
    if command_to_key.__contains__(_command):
        print("debug statement 2")
        
        mouse.move(command_to_key[_command]["mouseDxDy"][0] * constants.mouseSensitivityMult * _thinkingIntensity
                   ,command_to_key[_command]["mouseDxDy"][1] * constants.mouseSensitivityMult * _thinkingIntensity)

def thoughtToKeyPress(_command):
    print("debug statement 3")
    global curr_key_pressed
    global last_key_pressed
    if command_to_key.__contains__(_command):
        print("debug statement 4")

        last_key_pressed = curr_key_pressed        
        curr_key_pressed = command_to_key[_command]["input"]
    #keyboard.press_and_release(command_to_key[_command])

if __name__ == "__main__":
    main()
