import os
import sys
import time

screen = []

# This scary looking thing generates the ground
for height in range(os.get_terminal_size()[1]): # We repeat the loop exactly the amount of times as rows on the screen
    temp = "" # We use this variable to generate rows character by character, it gets reset after every loop iteration

    if height < int(os.get_terminal_size()[1] / 2): # We do this if we're above the half of the screen, we append a empty string, so when we read the screen we see it as a empty row
        screen.append("")

    elif height == int(os.get_terminal_size()[1] / 2): # We do this exactly on the half of the screen, we draw a line
        for length in range(os.get_terminal_size()[0]):
            temp += "_"
        screen.append(temp)


    else:
        for length in range(os.get_terminal_size()[0]): # Below the ground, we generate a lot of # to fill the ground
            temp += "#"
        screen.append(temp)

while True:
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")
    for read in screen:
        print(read)
    time.sleep(0.1)
