from pynput.keyboard import Key, Controller
import time
import subprocess
import os

clear = lambda : os.system('cls')
def clear():
    os.system( 'cls' )
keyboard = Controller()

subprocess.run('python -m pip install -U pip')
subprocess.run('pip install pynput')
clear()


print(" █████   █████   ████    ████    █   █  █        █")
print("█       █       █    █  █    █   █   █  ██      ██")
print("██████  ██████  █████   █████    █   █  █ █    █ █")
print("█       █        █ █     █ █     █   █  █  █  █  █")
print("█       █        █  █    █  █    █   █  █   ██   █")
print(" █        █████   █   █   █   █    ███   █        █")
print("------------------------------------------------------------")
print("{███████████████████████████████████████████████████████████}")







a = input("What do You want to SPAM?: ")
b = float(input("Type the delay you want to input per word IN SECONDS: "))
print("1. Press enter afterwards")
print("2. DONT press enter afterwards")
z = input("Press enter after each word? PRESS 1 if yes and 2 if no: ")

if z == '1':
    while True:

        keyboard.type(a)
        time.sleep(b)
        keyboard.press(Key.enter)

if z == '2':
    while True:
        keyboard.type(a)
        time.sleep(b)
print("Spamming started")
g = input("Press 'a' to stop spamming")

