'''
Now let us further improve the function. Let us implement a third function called calculate_tax_3 that takes in a float value which represents a person's taxable income. The function returns the total tax the person needs to pay. In this function, it is assumed that the taxable income passed to the function is between $0 and $40,000 (both inclusive). Note that you need to consider two possible tax rates (2% and 3.5%).

After you implement this function, call calculate_tax_3(25000.0) and check whether the function returns 100.0. Also call calculate_tax_3(10000.0) and check whether the function returns 0.0. Call calculate_tax_3(35000.0) and check whether the function returns 375.0.

Can you further improve the function so that it can handle any amount of taxable income as its argument?

Solve the question without using if/else, use max().
'''

# ################################################################################
# This function is for you to implement!


def calculate_tax_3(income):
    """
    This function assumes that the income is between $0 and $40,000.
    """
    # Modify the code below to return the right amount of tax.
    # first find amount between 30-40k, if any. max() will make zero if there is no such amount
    amount_30k_to_40k = max(income - 30000, 0)
    taxable_30_to_40k = amount_30k_to_40k * 0.0350
    # harder to generate amount between 20-30k since its a bracket in between. so we take 20-30k as the amount above 20k, capped at 10k using min(amount_above_20k, 10k)
    amount_above_20k = max(income - 20000, 0)
    taxable_20_to_30k = min(amount_above_20k, 10000) * 0.02
    tax = taxable_20_to_30k + taxable_30_to_40k
    return tax


'''
ANSWER

def calculate_tax_3(income):
    return (max(income - 20000, 0) * 0.02) + (max(income - 30000, 0) * (0.035 - 0.02))

OR

def calcuate_tax_3(income):
    above_30k = (max(0, income - 30000) * 0.035) + 200
    from_20k_to_30k = max (0, income - 20000) * 0.02
    return (max(above_30k, 20k_to_30k))
'''


# ################################################################################
# Call the function above to test whether it works.
print(calculate_tax_3(25000.0))
print(calculate_tax_3(10000.0))
print(calculate_tax_3(35000.0))

# ################################################################################

# up to 80k tax braket cos laze


def calculate_all_tax_brackets(income):
    rate_20k = max(income - 20000, 0) * 0.02
    additional_rate_30k = max(income - 30000, 0) * 0.015
    additional_rate_40k = max(income - 40000, 0) * 0.035
    additional_rate_80k = max(income - 80000, 0) * 0.045
    tax = rate_20k + additional_rate_30k + additional_rate_40k + additional_rate_80k
    return tax


print(calculate_all_tax_brackets(80001))
