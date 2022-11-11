def transform_string(string):
    transformed_string = ""
    uppercase = 0
    lowercase = 0
    digits = 0
    symbols = 0
    for ch in string:
        if ch.isupper():
            transformed_string += "L"
            uppercase += 1
        elif ch.islower():
            transformed_string += "l"
            lowercase += 1
        elif ch.isdigit():
            transformed_string += "d"
            digits += 1
        else:
            transformed_string += "s"
            symbols += 1
    print(uppercase, lowercase, digits, symbols)
    return transformed_string


print(transform_string("IS111 is a fun module."))
print(transform_string("ABC123^&*xyz"))
