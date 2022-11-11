user_input = input("What's the original message? ")
encrypted_string = ""
consonants = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
for letter in user_input:
    if letter not in consonants:
        encrypted_string += letter
    elif letter == "u":
        encrypted_string += "a"
    elif letter == "U":
        encrypted_string += "A"
    else:
        t_index = consonants.index(letter) + 1
        encrypted_string += consonants[t_index]

# Q4b
reversed_string = encrypted_string[-1::-1]

print(encrypted_string)
print(reversed_string)
