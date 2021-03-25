
import time
import os

clear = lambda : os.system('cls')
def clear():
    os.system( 'cls' )


os.system('python -m pip install -U pip')
os.system('pip install pynput')
clear()


print(" █████   █████   ████    ████    █   █  █        █")
print("█       █       █    █  █    █   █   █  ██      ██")
print("██████  ██████  █████   █████    █   █  █ █    █ █")
print("█       █        █ █     █ █     █   █  █  █  █  █")
print("█       █        █  █    █  █    █   █  █   ██   █")
print(" █        █████   █   █   █   █    ███   █        █")
print("------------------------------------------------------------")
print("{███████████████████████████████████████████████████████████}")

from pynput.keyboard import Key, Controller
keyboard = Controller()

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


