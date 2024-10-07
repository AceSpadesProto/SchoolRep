''' 
-----------------------------------------------------------------------------
Solution:       Lab 3
-----------------------------------------------------------------------------
Developer:     Tanner Mawk
Course:         Intro to Programming & Logic – CITC-1301
Creation Date:  9/26/24 (e.g., 1/11/2019)
Last Mod Date:  9/26/24 (e.g., 1/11/2019)
E-mail Address: tbmawk@senators.ws.edu
-----------------------------------------------------------------------------
Purpose - To display how many dog years are in imputed human years
-----------------------------------------------------------------------------
Description of input:
User inputs number of human years
Description of output:
Outputs calculation of dog years from inputed human years
-----------------------------------------------------------------------------
'''

print("This program calculates a dog's approximate age in 'dog years' based on human years.")
print("....................................................................................")

#Variables
humanYears = float(input("Imput Human Years:"))
dogYears = 10

#human years to dog years calculations
if humanYears <= 0.0:
    print("Human years may not be zero or negative")
else:
    if humanYears <= 1:
        dogYears = 15*humanYears
    elif humanYears <= 2:
        dogYears = 15+9*(humanYears-1)
    else:
        dogYears = 15+9+5*(humanYears-2) 

    #final print function
    print("Dog Years =",dogYears)