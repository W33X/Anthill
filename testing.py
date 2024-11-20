#This file is a experimental version of anthill.py
#We basically use this script to slap all the other files together
#Useful for testing
#Canapca

#Lib imports
import sys
import os
import random
import time

#File imports
#TODO remove lib imports from the files, won't need when running under this script
#Though let's leave them for now to remember what we need to run each file
import ant as ants
import ground as ground

#Screen init
ground.gen_ground()
ground.read_screen()
