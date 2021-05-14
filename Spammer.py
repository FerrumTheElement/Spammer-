import time, os

def clear():
    os.system("cls")

os.system('python -m pip install -U pip')
os.system('pip install keyboard')
clear()
#====================================================================================================
print(" █████   █████   ████    ████    █   █  █        █")
print("█       █       █    █  █    █   █   █  ██      ██")
print("██████  ██████  █████   █████    █   █  █ █    █ █")
print("█       █        █ █     █ █     █   █  █  █  █  █")
print("█       █        █  █    █  █    █   █  █   ██   █")
print(" █        █████   █   █   █   █    ███   █        █")
print("------------------------------------------------------------")
print("{███████████████████████████████████████████████████████████}")
#====================================================================================================
import keyboard


a = input("What do You want to SPAM?: ")
b = float(input("Type the delay you want to input per word IN SECONDS: "))
print("1. Press enter afterwards")
print("2. DONT press enter afterwards")
z = input("Press enter after each word? PRESS 1 if yes and 2 if no: ")
hotkey = input("What keybind do you want to stop the program at will?(1 letter/character): ")
timer = float(input("Amount of time before the program starts: "))
time.sleep(timer)

if z == '1':
    while True:
        keyboard.write(a)
        time.sleep(b)
        keyboard.press_and_release('enter')
        if keyboard.is_pressed(hotkey):
            1
            1
            exit(-1)
if z == '2':
    while True:
        keyboard.write(a)
        time.sleep(b)
        if keyboard.is_pressed(hotkey):
            exit(-1)
