while True:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    if first > 0 and second > 0 and first + second < 100:
        print("Thanks!")
        break
    print("Conditions not satisfied!")
    print()
