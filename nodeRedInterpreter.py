import keyboard
import time
import re
import asyncio
import pyautogui

class constants:
    pollRate = .1
    killSwitch = '/'
    mouseSensitivityMult = 1
    toggleSwitch = '='
    interpCount = 16
    #myPathAlt = "C:/Users/manny/AppData/Roaming/npm/node-red"

command_to_key = {
"neutral" : {"input":"a","mouseControl":True,"mouseDxDy":(20.0,20.0),"held":False},
"push" : {"input":"b","mouseControl":True,"mouseDxDy":(100.0,100.0),"held":False},
"pull" : {"input":"c","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"lift" : {"input":"d","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"drop" : {"input":"e","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"left" : {"input":"f","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False}, 
"right" : {"input":"g","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"rotateRight" : {"input":"h","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"rotateLeft" : {"input":"i","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"rotateCounterClockwise" : {"input":"j","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"rotateClockwise" : {"input":"k","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"rotateReverse" : {"input":"l","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"rotateForwards" : {"input":"m","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
"disappear" : {"letter":"n","mouseControl":False,"mouseDxDy":(1.0,1.0),"held":False},
}


#make it so that keys can be held and pressed rather than just repeatedly clicked

last_key_pressed = ""
curr_key_pressed = ""
last_input_detected = ""


enabled = True
def main():
    myPath = "" 
    with open('myPathInfo.txt', 'r') as file:
        myPath = file.read()
    global curr_key_pressed
    global last_key_pressed
    global last_input_detected
    global enabled

    while(True):
        if keyboard.is_pressed(constants.killSwitch):
            break
        if keyboard.is_pressed(constants.toggleSwitch):
            enabled = not enabled
            continue
        if enabled == False:
            time.sleep(constants.pollRate)
            continue
        with open(myPath, "r", encoding='utf-8') as f:
            lines = f.readlines()
            #no new input has been detected:
            if (lines == []) or lines[-1] == last_input_detected:
                time.sleep(constants.pollRate)
                #this means no new inputs, release key press
                release_held_key()
                continue
            last_input_detected = lines[-1]
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
    print(matches)
    mouseControl = command_to_key[matches[0][0]]["mouseControl"]
    if mouseControl == True:
        thoughtToMouseMovement(matches[0][0],int(matches[0][1]))
    else:
        thoughtToKeyPress(matches[0][0])
    

def thoughtToMouseMovement(_command, _thinkingIntensity):
    if command_to_key.__contains__(_command):
        
        movX = command_to_key[_command]["mouseDxDy"][0] * constants.mouseSensitivityMult * _thinkingIntensity
        movY = command_to_key[_command]["mouseDxDy"][1] * constants.mouseSensitivityMult * _thinkingIntensity
        
        movX = int(command_to_key[_command]["mouseDxDy"][0])
        movY = int(command_to_key[_command]["mouseDxDy"][1])
        #smoothly interpolate over pollRate amount of time, interpolationcount    

        pyautogui.moveRel(int(movX),int(movY),constants.pollRate-.001,tween=pyautogui.linear)

        #smoothlyInterpolateMouseMovement(movX,movY,constants.pollRate,constants.interpCount)





def thoughtToKeyPress(_command):
    global curr_key_pressed
    global last_key_pressed

    if curr_key_pressed != last_key_pressed:
        release_held_key()
    if command_to_key.__contains__(_command):

        if command_to_key[_command]["held"]:
            press_and_hold(command_to_key[_command]["input"])
        else:
            asyncio.run(press_and_release_time(command_to_key[_command]["input"],constants.pollRate))
        pass

async def press_and_release_time(key,_holdTime):
    print(key)
    keyboard.press(key)
    await asyncio.sleep(_holdTime)
    keyboard.release(key)


held_key = ''
def press_and_hold(key):
    global held_key
    held_key = key
    keyboard.press(held_key)

def release_held_key():
    global held_key
    if held_key == '':
        return
    keyboard.release(held_key)
    held_key = ''


if __name__ == "__main__":
    main()
