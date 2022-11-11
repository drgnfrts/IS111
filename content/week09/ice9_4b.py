def check_diff(pin1, pin2):
    if pin1 == pin2:
        return False
    return True


def check_short(pin1):
    if len(pin1) < 6:
        return True
    return False


def check_long(pin1):
    if len(pin1) > 6:
        return True
    return False


def check_not_digit(pin1):
    for ch in pin1:
        if not ch.isdigit():
            return True
    return False


def check(pin1, pin2):
    if check_diff(pin1, pin2) or check_short(pin1) or check_long(pin1) or check_not_digit(pin1):
        return False
    return True


while True:
    first = input("Enter your new PIN: ")
    second = input("Confirm your new PIN: ")
    if check(first, second):
        print()
        break
    print("Sorry! The following errors are detected")
    if check_long(first):
        print("    - The PIN number is too long.")
    if check_short(first):
        print("    - The PIN number is too short.")
    if check_not_digit(first):
        print("    - The PIN number contains a non digit character")
    if check_diff(first, second):
        print("    - The second PIN doesn't match the first PIN.")
    print()
print("Thanks! Your new PIN has been set!")
