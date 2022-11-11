'''
Write a piece of code that prompts the user for a positive integer. (You can assume that the user is always going to input a positive integer.) Call this integer n. The code then displays a random integer between 1 and n (both inclusive).
'''
import random

positive_integer = int(input("Enter a postive integer: "))
# generated_integer = random.randint(1, positive_integer) -> exclusive of the +ve last integer
generated_integer = random.randrange(1, positive_integer)
print(generated_integer)
