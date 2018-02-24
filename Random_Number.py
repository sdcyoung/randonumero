# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:46:37 2018

@author: danie
"""

import random
import time

print("what's good my friends, want to play a game?")

while True:
    button = input("press 'y' if you want, but if you're boujee press 'n'")
    if button[0].lower() == 'y':
        print("Nice, let's get rolling then...")
        time.sleep(2)
        num = random.randint(1,11)
        print(num)
    elif button[0].lower() == 'n':
        print("Damn, you boujee! You gotta leave now...")
        time.sleep(2)
        break
    else:
        print("Nah bruh you gotta type either 'y' or 'n'")
        continue