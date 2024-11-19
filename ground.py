import random
import os

screen = []
chars = ["#", ";", ":", "=", "$"]

#NOTE: Yes, I removed the comments, no need to explain the basics
# I do NOT care if you don't get it
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

# FOR TESTING ONLY
gen_ground()
for read in screen:
    print(read)
