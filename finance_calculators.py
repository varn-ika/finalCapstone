##### CAPSTONE PROJECT #####

import math

#Uisng print function to inform the user about the available options
print("Investment - To calculate the amount of interest you'll earn on your investment.")
print("Bond - To calculate the amount you'll have to pay on a home loan.")

#Creating variable "calculation" and asking user to enter one of the two options
calculation = str(input("Please enter either 'investment' or 'bond' from the menu above to proceed: "))

#Creating variable option_1 and option_2 
option_1 = 'investment'
option_2 = 'bond'

#Using if statement to calculate the amount user will get back when enters investment
if calculation.upper() == option_1.upper():

    #Creating variable "P" to get the principal amount depositing
    P = float(input("Please enter the amount of money you are depositing: "))

    #Creating variable "R" to get the interest rate
    R = float(input("Please enter the interest rate: "))

    #Converting the interest rate into percentage
    r = R/100

    #Creating variable "t" and using input function to ask the user number of years they wanna invest
    t = int(input("Please enter the number of years you plan to invest: "))

    #Creating variable "interest" to ask the user to choose one of the two types of interest
    interest = str(input("Please enter the type of interest you want - 'simple' or 'compound': "))

    #Using if statement if the user enters simple interest
    if interest.upper() == 'simple'.upper():

        #Calculating as per simple interest
        A1 = int(P*(1 + r*t))

        #Rounding up the amount to two decimal places
        a1 = round(A1, 2)

        #Printing the amount user earns after t years
        print("The amount you will get back after", t, "years is", a1)

    #Using elif statement if the user enters compound interest    
    elif interest.upper() == 'compound'.upper():

        #Calculating as per compound interest
        A2 = P * math.pow((1+r),t)

        #Rounding up the amount to two decimal places
        a2 = round(A2, 2)

        #Printing the amount user earns after t years
        print("The amount you will get back after", t, "years is", a2)

    #Using else statement and printing so the user chooses one of the two when enters wrong type of interest
    else:
        print("Please enter either 'simple' or 'compound'!")

#Using elif statement to Calculate EMI when user enters bond
elif calculation.upper() == option_2.upper():

    #Creating variable "p" to get the present value of the house
    p = float(input("Please enter the present value of the house: "))

    #Creating variable "I" to get the interest rate
    I = float(input("Please enter the interest rate: "))

    #Converting the interest rate into percentage and calculating monthly interest
    i = (I/100)/12

    #Creating variable "n" and using input function to ask the user number of months they want to take to repay the amount
    n = int(input("Please enter the number of months you plan to take to repay the bond: "))

    #Calculating EMI
    repayment = int((i * p)/(1 - (1 + i)**(-n)))

    #Rounding up the amount of repayment to two decimal places
    Repayment = round(repayment, 2)


    #Printing the amount of EMI 
    print("The amount you will have to repay each month for", n, "months is", Repayment)

#Using else statement and printing error message when the user enters wrong value
else:
    print("Please enter a valid input, either 'investment' or 'bond'!")

##### END OF PROJECT #####