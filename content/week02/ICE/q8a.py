'''
Implement a function called calculate_tax_1 that takes in a float value which represents a person's taxable income. The function returns the total tax the person needs to pay. In this function, it is assumed that the taxable income passed to the function is between $20,000 and $30,000 (both inclusive).

After you implement this function, call calculate_tax_1(25000.0) and check whether the function returns 100.0
'''
# ################################################################################
# This function is for you to implement!


def calculate_tax_1(income):
    """
    This function assumes that the income is between $20,000 and $30,000.
    """
    # Modify the code below to return the right amount of tax.
    taxable_amount = income - 20000
    tax = taxable_amount * 0.02
    return tax
# ################################################################################


# Call the function above to test whether it works.
print(calculate_tax_1(25000.0))
