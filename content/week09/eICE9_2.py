while True:
    pw = input("Enter a password: ")
    if len(pw) < 6 or len(pw) > 10:
        print("The password entered is not valid!")
        continue
    lower = False
    upper = False
    special = False
    digit = False
    nospace = True
    for ch in pw:
        if ch.isalpha():
            if ch.islower():
                lower = True
            if ch.isupper():
                upper = True
        elif ch.isdigit():
            digit = True
        elif ch == " ":
            nospace = False
        else:
            special = True
    if lower and upper and special and digit and nospace:
        break
    print("The password entered is not valid!")
print("Thank you!")
