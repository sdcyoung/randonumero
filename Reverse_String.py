# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:22:24 2018

@author: danie
"""

print("Hey, type in a word so we can reverse it!")
while True:
    user_word = input("go ahead and type a word here: ")
    if user_word.isalpha():
        reversed_result = str(user_word[::-1])
        print(reversed_result)
    else:
        print("Yikes, try typing in letters...no numbers!!!")
        break