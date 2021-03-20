#!/usr/bin/env python3 

#This tells the system which version of Python to use

#Program Notes
#TODO Fill out the program notes
"""
Aurthor : [Courtney Heba]
Email   : [Courtney.heba@gmail.com]
Purpose : [Random password generator]
Date    : [3/20/2021]
"""


import argparse
import random

password_length = int(input("How many charaters would you like your password? "))

# create lists
list_symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

list_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lowercase_list = ["a", "b", "c", "v", "q", "u", "x", "p", "q", "y"]

uppercase_list = ["A", "B", "S", "C", "T", "W", "R", "M", "N", "J"]

# create a join to join the 4 lists together
password_character_bank = list_symbols + list_num + lowercase_list + uppercase_list
# loop over password character bank and choose a character at random
# that character will be added to our password
password = []

# loop over password character bank and choose a character at random
for x in range(password_length):
    password.append(random.choice(password_character_bank))

# print random password to user
print(password)

#BONUS
How many charaters would you like your password? 4
['@', 'x', 'W', 'B']
