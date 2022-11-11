'''
The function above cannot handle an income value that is below $20,000. To make the function more flexible, now implement another function called calculate_tax_2 that takes in a float value which represents a person's taxable income. The function returns the total tax the person needs to pay. In this function, it is assumed that the taxable income passed to the function is between $0 and $30,000 (both inclusive). Use the max() function.

After you implement this function, call calculate_tax_2(25000.0) and check whether the function returns 100.0. Also call calculate_tax_2(10000.0) and check whether the function returns 0.0.

max(a, b) will return the higher of the iterables
'''

# ################################################################################
# This function is for you to implement!


def calculate_tax_2(income):
    """
    This function assumes that the income is between $0 and $30,000.
    """
    # Modify the code below to return the right amount of tax.
    taxable_amount = max(income - 20000, 0)
    tax = taxable_amount * 0.02
    return tax

# ################################################################################


# Call the function above to test whether it works.
print(calculate_tax_2(25000.0))
print(calculate_tax_2(10000.0))
