# Q5 Tax Calculation

'''
note the algorithm used

case 1: <20000 - just return 0
case 2: 20000 to 320k - check for the ceiling (i), then use the previous bracket (i + 1)'s values
case 3 > 320k: use the last bracket's values
'''

TAX_INFO = [
    (20000, 0, 0.02),
    (30000, 200, 0.035),
    (40000, 550, 0.07),
    (80000, 3350, 0.115),
    (120000, 7950, 0.15),
    (160000, 13950, 0.18),
    (200000, 21150, 0.19),
    (240000, 28750, 0.195),
    (280000, 36550, 0.2),
    (320000, 44550, 0.22)
]

# Write your code below:
##############################################################


def calculate_tax(income):
    if income < 20000:
        return 0.0

    for i in range(len(TAX_INFO)):
        if income < TAX_INFO[i][0]:
            return TAX_INFO[i - 1][1] + ((income - TAX_INFO[i - 1][0]) * TAX_INFO[i - 1][2])

        elif i == (len(TAX_INFO)) - 1:
            return TAX_INFO[i][1] + ((income - TAX_INFO[i][0]) * TAX_INFO[i][2])


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES
tax = calculate_tax(15000)
print("Expected: 0.0")
print("Actual  : " + str(tax))
print()

tax = calculate_tax(35000)
print("Expected: 375.0")
print("Actual  : " + str(tax))
print()

tax = calculate_tax(100000)
print("Expected: 5650.0")
print("Actual  : " + str(tax))
print()

tax = calculate_tax(350000)
print("Expected: 51150.0")
print("Actual  : " + str(tax))
print()
