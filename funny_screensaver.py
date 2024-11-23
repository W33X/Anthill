#This file will be merged into ground.py after completion
import random
import os #Temporary, obviouisly
import time
import sys

def gen_noise():
    noise_map = []
    #Since this is a WIP file, I'm going to complain here a lot
    #RN I have no idea what to do ;-;
    for Y in range(os.get_terminal_size()[1]):
        temp = ""
        for X in range(os.get_terminal_size()[0]):
            #Okay so this is like working on a individual line
            #The problem is that I'm trying to make a 2D shape made of 1D shapes that don't connect
            #I think the best approach is to just generate a empty screen with some "seeds"
            #We then, use the already generated screen and we grow those seeds into blobs
            #My brain is fried
            if random.randint(1, 400) == 1:
                temp += "0"
            else:
                temp += " "
        noise_map.append(temp)
    return noise_map

#WTF I just realised that this could be its own screensaver
while True:
    for loop in gen_noise():
        print(loop)
    time.sleep(1)
    if sys.platform == "linux":
        os.system("clear")
    if sys.platform == "windows":
        os.system("cls")
