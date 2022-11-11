def pin_check(pin):
    if len(pin) != 6:
        return False
    for ch in pin:
        if not ch.isdigit():
            return False
    return True


while True:
    first = input("Enter your new PIN: ")
    second = input("Confirm your new PIN: ")
    if pin_check(first) and first == second:
        print()
        break
    print("Sorry! There is an error!")
    print()

print("Thanks! You new PIN has been set")
