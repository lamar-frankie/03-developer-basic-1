#!/usr/bin/env python3 

#This tells the system which version of Python to use

#Program Notes
#TODO Fill out the program notes
"""
Author  : Lauren
Email   : laurenchristianson@live.com
Purpose : Random password generator
Date    : 2021-03-23
"""


import argparse
import random


#-------------------------------------------------------------------------
#Ask the user how long they would like their new password to be
password_length = int(input("Enter password length: ") or 8 ) #default length is 8

#A list if symbols we can use in our password
symbols_list = ['!', '@', '#', '%', '&', '*']

#Create a list of numbers 0 - 9
numbers_list = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Create a list of the 10 least used lowercase letters in the english language
lowercase_list = ['z', 'x', 'j', 'q', 'k', 'v', 'b', 'g', 'p', 'w']

#Create a list of the 10 most use used uppercase letters in the english language
uppercase_list = ['E', 'T', 'A', 'I', 'N', 'O', 'S', 'H', 'R', 'D']

#Join the 4 lists together to form a password character banks
password_character_bank = symbols_list + numbers_list + lowercase_list + uppercase_list

#We are going to loop over the password character bank and choose a character at random
#That character will be asdded to our password
password = []

#Loop over password character bank and choose a character at random
for x in range(password_length):
    password.append(random.choice(password_character_bank))

#print the password out to the user
print(''.join(str(password)))

#Bonus
#TODO: Copy the generated password to the users clip board