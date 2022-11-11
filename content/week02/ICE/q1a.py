'''
You are given a function called compute_average(). Read the docstring of the
function to understand what it does. Write a piece of code that prompts the user for three numbers
and displays the average of the three numbers by calling compute_average().
'''
# ################################################################################
# The following code is given to you.


def compute_average(a, b, c):
    """ 
    This function returns the average of the three numbers a, b and c.
    """
    return (a + b + c)/3


# ################################################################################
# Write your code below:
first_num = float(input("Enter 1st number: "))
second_num = float(input("Enter 2nd number: "))
third_num = float(input("Enter 3rd number: "))

print(f"Average: {compute_average(first_num, second_num, third_num)}")
