import math # Imports the maths module from the Python Library
# Capstone Project I


invest = False #Declares the invest variable as False
bond = False #Declares the bond variable as False


calculate = input("Welcome\nWhat calculator would you like to access?\nA calculator for an Investment or a calculator for a Bond?\n") #Asks for users input 

if calculate == "investment" or calculate == "Investment" or calculate == "INVESTMENT": # Accounts for typing style
    invest = True

elif calculate == "Bond" or calculate == "bond" or calculate == "BOND": # Accounts for typing style
    bond = True

else:
    print("Error!!!\nYour input is invalid\nPlease make an appropriate selection")

#The above if-elif-else statement helps in the decision making process,
#if  the users input is investmet, then invest becomes True,
#if  the users input is bond, then bond becomes True



if invest == True:
    amount = float(input("How mauch money are you depositing?\nR"))
    interest_rate = float(input("What is the percentage (%) interest rate(Enter the numer only)?\n"))
    time = float(input("How many years do you intend on investing for?\n"))
    invest =input("Would you like 'simple' interest or 'compound' interest?\n")

    P = amount # Simplifies amount variable in order to reduce error in the calculation step
    r = interest_rate/100 # Converts value entered for interest into a percenteage
    t = time # Simplifies time variable in order to reduce error in the calculation step
    if invest == "simple" or invest == "Simple" or invest == "SIMPLE":    
        A = P*(1+r*t) #Equates amount variable to simple interest formula
        
    elif invest == "compound" or invest == "Compound" or invest == "COMPOUND":
        A = P* math.pow((1+r),t) #Define Amount by the equation for compound interest  using an equation with the assistance of a module from the Python Library
        
    else:
        print("Error!!!\nYour input is invalid\nPlease make an appropriate selection")    
    
    interest_earned = A - P #Calculates the amount earned as interest 
    
    print ("The accumulated amount of your investment is R{}\nThe interest earned is R{}".format(A,interest_earned))



if bond == True:
    prsnt_value = float(input("What is the present value of the house?\nR"))
    int_rate = float(input("What is the percentage (%) interest rate(Enter the number only)?\n"))
    months = int(input("How many months do you plan to repay the bond?\n"))

    P = prsnt_value # Simplifies prsnt_value variable in order to reduce error in the calculation step
    i = (int_rate/100)/12 # converts value entered for interest into a percenteage followed by dividing by 12 months
    n = months # Simplifies months variable in order to reduce error in the calculation step

    x = (i*P)/(1-math.pow((1+i),-n))

    print("The monthly Bond repayment is:\nR{}" .format(x))
    
