import atexit
import datetime
from pynput import keyboard
import random
from save import *
import sys
import termios
from utils import *

playerStats = loadSave()

def startload():
    # call the enableEcho function when the program exits and set it to true
    atexit.register(enableEcho, sys.stdin.fileno(), True)

    enableEcho(sys.stdin.fileno(), False)
    from title import startscreen
    startscreen()
    
def printPlayerStats():
    print(' health | ', playerStats.Health)
    print('     mp | ', playerStats.Mp)
    print('     xp | ', playerStats.Xp)
    print('    lvl | ', playerStats.Lvl)
    print('defence | ', playerStats.Defence)
    print(' damage | ', playerStats.Damage)
    print('\n')
    
# def PlayerInvo():   
def main():
    startload()

    printPlayerStats()

    userInput = getchar()

    if userInput == ('p'):
        print("placeholder text")
    elif userInput == ('.'):
        saveFunction(playerStats)
        
    exit(0)

if __name__ == "__main__":
    main()          