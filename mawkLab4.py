''' 
-----------------------------------------------------------------------------
Solution:       Lab 4 
-----------------------------------------------------------------------------
Developer:      Tanner Mawk
Course:         Intro to Programming & Logic – CITC-1301
Creation Date:  10/2/24 (e.g., 1/11/2019)
Last Mod Date:  10/2/24 (e.g., 1/11/2019)
E-mail Address: tbmawk@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - To display user's money after x number of years
-----------------------------------------------------------------------------
Description of input:
User imputs x number of years
Description of output:
Outputs user's money count after x years
-----------------------------------------------------------------------------
'''

#This took far longer than I expected it to lol
#Yes, this works infinitely

#Variables
numberValue = int(input("Number of years: "))
semiValue = 1

#Header Information and Printing
#Empty space for pretty factor
print("                                           ")
print ("Year        Total")
print ("---------------------")


#Calculation based on year number
for semiValue in range(numberValue+1):
    trueValue = 3000*2**(semiValue)
    print(semiValue, "         $",float(trueValue))
    semiValue = semiValue + 1
#if there is any way to make this code more compact/efficient, I would love to know, really just wanted to mess around with for loops.

#Final footer printing/final calculation/Final output/note
print("After",numberValue,"years, you have $",(trueValue))

#Empty space to make it pretty
print("                                 ")


#This was testing. What eventually helped finally get correct code. Prints almost correct, just backwards order.
'''
while numberValue != 0:
    trueValue = 3000*2**(numberValue)
    print(numberValue, "          ", trueValue)
    numberValue = numberValue - 1
    
'''