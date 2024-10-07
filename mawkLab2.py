''' 
-----------------------------------------------------------------------------
Solution:       Lab 2 
-----------------------------------------------------------------------------
Developer:     Tanner Mawk
Course:         Intro to Programming & Logic – CITC-1301
Creation Date:  9/18/24 (e.g., 1/11/2019)
Last Mod Date:  9/18/24 (e.g., 1/11/2019)
E-mail Address: tbmawk@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - To display user's score
-----------------------------------------------------------------------------
Description of input:
User imputs Magic Mushroom Count
Description of output:
Outputs user's score and leftover Magic Mushrooms
-----------------------------------------------------------------------------
'''

#Variables
shroom_count = int(input("How many magic mushrooms do you have?"))
shroom_left = shroom_count - 4

#Mushroom Count = 0
if shroom_count == 0:
    print("You have 0 Magic Mushrooms, and have 0 points!")

#Mushroom Count = 1
elif shroom_count == 1:
    print("You have 1 Magic Mushroom, and have 5 points!")

#Mushroom Count = 2
elif shroom_count == 2:
    print("You have 2 Magic Mushrooms, and have 10 points!")

#Mushroom Count = 3
elif shroom_count == 3:
    print("You have 3 Magic Mushrooms, and have 20 points!")

#Mushroom Count = 4+
else:
    print("You have", shroom_count,"Magic Mushrooms! 4 of them have been turned into 50 points!")

#Mushroom's Left
if shroom_count >= shroom_left:
    print("You have", shroom_left, "Magic Mushrooms left!")