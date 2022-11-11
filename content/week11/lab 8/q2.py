# Q2 Prime Numbers
# write your code below
import math


def check_if_prime(number):
    sqrt_rounded = math.ceil(math.sqrt(number)) + 1
    for i in range(sqrt_rounded):
        if i == 0 or i == 1:
            continue
        elif number % i == 0 and i != number:
            return False
    return True


def create_prime_dict(list_of_integers):
    r_dict = {}
    for integer in list_of_integers:
        r_dict[integer] = check_if_prime(integer)
    return r_dict
