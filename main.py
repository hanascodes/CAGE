# -*- coding: utf-8 -*-
import subprocess
from playsound import playsound
import os
import time as money

def sihir1():
    money.sleep(2)
    subprocess.run("clear")

#input name
#name has to be tested - can't be a shell command to prevent cheating

print("You're an intern at P-Corp.")
sihir1()

print("Hello world")
sihir1()

print("Or should I say")
sihir1()

print("Hello friend.")
sihir1()

#game only accepts yes as an answer as inputted lowercase "y". otherwise it just shuts down
answer = input("Would you like to play a game?")

if answer == "y":
    print("Okie dokie.")
    playsound("venv/test_file.wav")
else:
    exit()
#hard mode: shuts down PC via sudopoweroff or even reboot
#idea - keeps the system locked until all the correct steps were taken
#it's a labyrinth.
#idea - iExist script found on Desktop, script leads to old 
#project website - digging through my own past to create
#a brighter future
#idea - when user inputs data (name), data purges after the game ends
