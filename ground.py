import random
import os
import sys

screen = []
chars = ["#", ";", ":", "=", "$"]

#I've done my part, I made it colored on linux, your turn

def gen_ground():
    for height in range(os.get_terminal_size()[1]):
        temp = ""
        if height < int(os.get_terminal_size()[1] / 2):
            screen.append("")
        elif height == int(os.get_terminal_size()[1] / 2):
            for length in range(os.get_terminal_size()[0]):
                if sys.platform == "linux":
                    temp += "\033[32m_\033[m"
                else:
                    temp += "\033[32m_\033[m"
            screen.append(temp)
        else:
            for length in range(os.get_terminal_size()[0]):
                if sys.platform == "linux":
                    temp += "\033[33m"
                    temp += random.choice(chars)
                    temp += "\033[m"
                else:
                    temp += random.choice(chars)
            screen.append(temp)

def read_screen():
    for read in screen:
        print(read)
