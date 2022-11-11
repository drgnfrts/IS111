# Lab2_Q4
# #####################################
# Write your code below to first define
# the function calculate_interest()

def generate_interest_compounded(principal, years):
    ANNUAL_INTEREST_RATE = 0.005
    FREQUENCY_OF_COMPOUNDING = 12
    compound_interest = round((principal * (1 + ANNUAL_INTEREST_RATE/FREQUENCY_OF_COMPOUNDING)
                               ** (years * FREQUENCY_OF_COMPOUNDING)) - principal, 2)
    return compound_interest

# ################################################################
# The default annual interest rate of 0.5%, compounded
# monthly, has been provided for you.

# Annual interest rate (which is fixed)
# ANNUAL_INTEREST_RATE = 0.005
# Number of times the interest is compounded per year
# FREQUENCY_OF_COMPOUNDING = 12

# ################################################################
# Write your code below to prompt the user and display the
# interest earned.


user_principal = float(input("What's the amount of your principal? "))
user_years = float(input("How many years do you want to deposit the money? "))

interest = generate_interest_compounded(user_principal, user_years)
print(interest)

'''
Q4: The generate_interest_compounded function should take in a total of 4 parameters (principal, annual_interest_rate, frequency_of_compounding, years) as specified in the question. Also, format your output as per the sample output in the question. Try this code:  print("\nThe interest you will earn is $" + str(interest))
'''