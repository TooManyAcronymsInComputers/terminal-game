import os
import sys
import termios

# Write to standard error stream and exit with error code 1. (Use this for error messages)
def die(message):
    print(message, file=sys.stderr)
    exit(1)

# Enable/Disable echo and cannonical mode (uninterrupted input and no input characters on screen).
def enableEcho(fd, enabled):
    (iflag, oflag, cflag, lflag, ispeed, ospeed, cc) = termios.tcgetattr(fd)
    if enabled:
        lflag |= termios.ECHO
        lflag |= termios.ICANON
    else:
        lflag &= ~termios.ECHO
        lflag &= ~termios.ICANON
    new_attr = [iflag, oflag, cflag, lflag, ispeed, ospeed, cc]
    termios.tcsetattr(fd, termios.TCSANOW, new_attr)

# Check if file is empty (useful for player stats and other things in the future maybe)
def isFileEmpty(file):
    if not os.path.isfile(file):
        die("Save file not found. (playerstats.py)")

    fileSize = os.path.getsize(file)

    if(fileSize == 0):
        return True
    else:
        return False

# Get character using the read system call. shorter name for ease of use
def getchar():
    return sys.stdin.read(1)

# clear the screen
def clearScreen():
    print("\033c")
