# Q2 List of Numbers
# a)
# Write your code below:
##############################################################
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

def get_leap_years(list_of_years):
    leap_years = []
    for year in list_of_years:
        if year % 4 == 0:
            if year % 400 == 0 or year % 100 != 0:
                leap_years.append(year)
    return leap_years


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES
print('Test Case 1')
print('-' * 11)
print('Expected: [2000, 2020]')
print('Actual:   ' + str(get_leap_years([2018, 2000, 1800, 1900, 2011, 2020])))

print('\nTest Case 2')
print('-' * 11)
print('Expected: []')
print('Actual:   ' + str(get_leap_years([2018, 2001, 1800, 1900, 2011, 2100])))
