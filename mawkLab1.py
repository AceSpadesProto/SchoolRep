''' 
-----------------------------------------------------------------------------
Solution:       Lab 1 
-----------------------------------------------------------------------------
Developer:     Tanner Mawk
Course:         Intro to Programming & Logic – CITC-1301
Creation Date:  9/12/24 (e.g., 1/11/2019)
Last Mod Date:  9/12/24 (e.g., 1/11/2019)
E-mail Address: tbmawk@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - To display user's stats, gold, and food
-----------------------------------------------------------------------------
Description of input:
User imputs stats and gold
Description of output:
Outputs user's stats, hp, gold, ammount of food, and leftover gold
-----------------------------------------------------------------------------
'''

#Variables
user_nameFirst = input("What is your first name: ")
user_nameLast = input("What is your last name: ")
user_level = int(input("What is your level: "))
user_gold = int(input("How much gold do you have: "))
buyable_food = user_gold // 5
gold_left = user_gold % 5

#Name Listing
print("Name:",user_nameFirst, user_nameLast)

#Level Listing
print("Level:", user_level)

#Calcuation for User's HP stat
print("HP:", user_level*1.6)

#Gold Listing
print("Gold:", user_gold)

#Food Listing
print("Weeks of food you may buy:",buyable_food)\

#Leftover Gold Listing
print("Leftover Gold:",gold_left)

'''
TESTING PURPOSES ONLY
'''

'''
This is some cool stuff that I worked on, realised it was part of the project, but wanted to show it off! 
So, here's some randomized stats! 
Feel free to delete the triple appostrophes to view it!
'''

'''
#Random Stat Calculations
import random

num_str = random.randint(3,20)
num_con = random.randint(3,20)
num_dex = random.randint(3,20)
num_int = random.randint(3,20)
num_wis = random.randint(3,20)
num_cha = random.randint(3,20)

#Random Stat Listings
print("STR:", num_str)
print("CON:", num_con)
print("DEX:", num_dex)
print("INT:", num_int)
print("WIS:", num_wis)
print("CHA:", num_cha)
'''

'''
#Charisma test (was using this for teaching purposes)
import random
print("CHA:",random.randint(3,20))
'''




