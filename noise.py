#This file will be merged into ground.py after completion
import random
import os #Temporary, obviouisly
import time
import sys

grow area = 5

def noise_start():
    noise_map = []
    for Y in range(os.get_terminal_size()[1]):
        temp = ""
        for X in range(os.get_terminal_size()[0]):
            if random.randint(1, 400) == 1:
                temp += "0"
            else:
                temp += " "
        noise_map.append(temp)
    return noise_map

def noise_grow():
    noise = noise_start()
    for grow in range(grow_area)

#Cannot finish this right now, what I'm going for here
#Is a basic system where we iterate through every character of the noise map
#And we check for neighboring seeds, if there are any we simply turn that char into
#A new part of the blob, I'm probably going to use a different character
#So we can basically do like a age system where the oldest parts are different chars
#Something we can use to make it look like a actual blob, so we can avoid overgrowing
#Like, if there's a charcter but not proper oldness, we don't grow, this would prevent
#Blobs of different stages from groving into each other
#So the rooms can stay separate
#God why is this so long? ;-;
