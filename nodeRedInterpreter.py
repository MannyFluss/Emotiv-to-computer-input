import keyboard
import time
import re

class constants:
    myPath = "C:/Users/manny/Desktop/work4Dom/output.txt"
    pollRate = .1
    killSwitch = '/'
    #myPathAlt = "C:/Users/manny/AppData/Roaming/npm/node-red"
command_to_key = {
"neutral" : "a",
"push" : "b",
"pull" : "c",
"lift" : "d",
"drop" : "e",
"left" : "f",
"right" : "g",
"rotateRight" : "h",
"rotateLeft" : "i",
"rotateCounterClockwise" : "j",
"rotateClockwise" : "k",
"rotateReverse" : "l",
"rotateForwards" : "m",
"disappear" : "n",
}
    

def main():
    while(True):
        if keyboard.is_pressed(constants.killSwitch):
            break
        with open(constants.myPath, "r", encoding='utf-16') as f:
            lines = f.readlines()
            pollInput(lines[-1])
            if len(lines) == 0:
                time.sleep(constants.pollRate)
                continue
        time.sleep(constants.pollRate)

def pollInput(_line : str):
    pattern = r'\[info\] \[debug:debug \d+\] (\w+),(\d+)'
    validLine = re.search(pattern,_line)
    if not validLine:
        print("invalid line")
        return
    matches = re.findall(pattern,_line)
    thoughtToKeyPress(matches[0][0])
    

def thoughtToKeyPress(_command):
    if command_to_key.__contains__(_command):
        print(command_to_key[_command])
        keyboard.press_and_release(command_to_key[_command])


if __name__ == "__main__":
    main()
