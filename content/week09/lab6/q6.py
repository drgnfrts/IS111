import random

start = input(
    "Do you want to practice multiplication table? Please enter Y or N: ")
while start == "Y":
    first = random.randint(1, 9)
    second = random.randint(1, 9)
    multiply_input = int(
        input(f"What's the result of {first} times {second}? "))
    while multiply_input != first * second:
        multiply_input = int(input("Wrong answer! Please try again: "))
    print("You are right!")
    print()
    start = input(
        "Do you want to continue your practice? Please enter Y or N: ")
    print()
print("Good-bye!")
