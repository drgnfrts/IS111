# Q2 List of Numbers
# d)
# Write your code below:
##############################################################
'''
note to self: this question was not that easy because of the figuring out of the algorithm for prime numbers.

in checking of prime numbers, only need to check up to sqrt of number. rounded up the sqrt and +1 to ensure that it checks properly especially for small numbers like 2, 3, 4 where a small difference in iterable range can cause the algorithm to not check certain numbers (e.g. sqrt 4 is 2, we need 2 to be included in checks, hence +1)

also join() only takes in if all items are strings

'''

import math


def check_if_prime(number):
    sqrt_rounded = math.ceil(math.sqrt(number)) + 1
    for i in range(sqrt_rounded):
        if i == 0 or i == 1:
            continue
        elif number % i == 0 and i != number:
            return False
    return True


def get_prime_numbers(num_list, sep):
    primes_list = []
    for num in num_list:
        if check_if_prime(num):
            primes_list.append(str(num))
    return sep.join(primes_list)


    ##############################################################
    # Test Cases to test your code
    # DO NOT MODIFY THE TEST CODES
print('Test Case 1')
print('-' * 11)
print('Expected: 2-7-11-19')
print('Actual:   ' + str(get_prime_numbers([2, 4, 7, 9, 11, 16, 19, 21], '-')))

print('\nTest Case 2')
print('-' * 11)
print('Expected: 3')
print('Actual:   ' + str(get_prime_numbers([3, 4, 8, 9, 12, 16], '*')))
