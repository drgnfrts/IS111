def retrieve_numbers(input_string):
    digits_list = []
    digit_sequence = ""
    for i in range(len(input_string)):
        ch = input_string[i]
        if ch.isdigit():
            digit_sequence += ch
        elif not ch.isdigit() and input_string[i - 1].isdigit():
            digits_list.append(digit_sequence)
            digit_sequence = ""
    if digits_list == []:
        return ""
    return " ".join(digits_list)


print(retrieve_numbers("12abc600$##0900AB 100X"))
print(retrieve_numbers("34.5689abc980"))
print(retrieve_numbers("xyz"))
print(retrieve_numbers("abc25xyz"))


