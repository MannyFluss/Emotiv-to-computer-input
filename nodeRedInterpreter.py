import keyboard
import time
import re
import asyncio
from pynput.mouse import Button, Controller

class constants:
    pollRate = .1
    killSwitch = '/'
    mouseSensitivityMult = 1
    toggleSwitch = '.'
    #myPathAlt = "C:/Users/manny/AppData/Roaming/npm/node-red"

command_to_key = {
"neutral" : {"input":"a","mouseControl":False,"mouseDxDy":(1.0,1.0)},
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
last_input_detected = ""
mouse = Controller()
def main():
    myPath = "" 
    with open('myPathInfo.txt', 'r') as file:
        myPath = file.read()
    global curr_key_pressed
    global last_key_pressed
    while(True):
        if keyboard.is_pressed(constants.killSwitch):
            break
        if keyboard.is_pressed(constants.toggleSwitch):
            time.sleep(constants.pollRate)
            continue

        with open(myPath, "r", encoding='utf-16') as f:
            lines = f.readlines()
            if (lines == []) or lines[-1] == last_input_detected:
                time.sleep(constants.pollRate)
                continue
            #no new input has been detected:

            pollInput(lines[-1])
        time.sleep(constants.pollRate)




def pollInput(_line : str):
    print(_line)
    pattern = r'\[info\] \[debug:debug \d+\] (\w+),(\d+)'
    validLine = re.search(pattern,_line)
    if not validLine:
        #print("invalid line")
        return
    matches = re.findall(pattern,_line)
    mouseControl = command_to_key[matches[0][0]]["mouseControl"]
    #print("mouse control = " +str(mouseControl))
    if mouseControl == True:
        thoughtToMouseMovement(matches[0][0],int(matches[0][1]))
    else:
        thoughtToKeyPress(matches[0][0])
    

def thoughtToMouseMovement(_command, _thinkingIntensity):
    if command_to_key.__contains__(_command):
        
        mouse.move(command_to_key[_command]["mouseDxDy"][0] * constants.mouseSensitivityMult * _thinkingIntensity
                   ,command_to_key[_command]["mouseDxDy"][1] * constants.mouseSensitivityMult * _thinkingIntensity)

def thoughtToKeyPress(_command):
    global curr_key_pressed
    global last_key_pressed
    if command_to_key.__contains__(_command):
        #print("pressing key " + command_to_key[_command]["input"])
        asyncio.run(press_and_release_time(command_to_key[_command]["input"],constants.pollRate))
        pass
        # if last_key_pressed != curr_key_pressed:
        #     if curr_key_pressed != "":
        #         keyboard.press(curr_key_pressed)
        #     if last_key_pressed != "":
        #         keyboard.release(last_key_pressed)
        # last_key_pressed = curr_key_pressed        
        # curr_key_pressed = command_to_key[_command]["input"]

    #keyboard.press_and_release(command_to_key[_command])

async def press_and_release_time(key,_holdTime):
    print(key)
    keyboard.press(key)
    await asyncio.sleep(_holdTime)
    keyboard.release(key)


if __name__ == "__main__":
    main()
