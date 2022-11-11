import random

correct_num = random.randint(1, 100)
while True:
    guess = int(input("Enter your guess (between 1 and 100) :"))
    if guess == correct_num:
        print("Bingo!")
        break
    elif guess < correct_num:
        print("Your guess is too low!")
    else:
        print("Your guess is too high!")
    print()
