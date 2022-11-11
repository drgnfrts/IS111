user_input = int(input("Enter Month: "))

thirty_days = (4, 6, 9, 11)

if not 1 <= user_input <= 12:
    print("Enter a number between 1 and 12 only!")
else:
    if user_input == 2:
        days = 28
    elif user_input in thirty_days:
        days = 30
    else:
        days = 31
    print(f"There are {days} days in this month.")
