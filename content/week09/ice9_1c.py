import string


def check_name(name):
    pool = string.ascii_letters + " "
    for ch in name:
        if ch not in pool:
            return False
    return True


while True:
    name = input("Enter your name: ")
    if check_name(name):
        print("Thank you!")
        break
    print("Please enter a valid name!")
