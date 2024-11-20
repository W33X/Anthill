import random
import os

screen = []
chars = ["#", ";", ":", "=", "$"]

def gen_ground():
    for height in range(os.get_terminal_size()[1]):
        temp = ""
        if height < int(os.get_terminal_size()[1] / 2):
            screen.append("")
        elif height == int(os.get_terminal_size()[1] / 2):
            for length in range(os.get_terminal_size()[0]):
                temp += "_"
            screen.append(temp)
        else:
            for length in range(os.get_terminal_size()[0]):
                temp += random.choice(chars)
            screen.append(temp)

def read_screen():
    for read in screen:
        print(read)
