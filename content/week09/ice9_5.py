def count_digits(input_string):
    digit_count = 0
    for ch in input_string:
        if ch.isdigit():
            digit_count += 1
    return digit_count


def get_strings_with_digits(str_list, t):
    r_list = []
    count = 0
    n = 0
    while count <= t and n < len(str_list):
        if count_digits(str_list[n]) != 0:
            r_list.append(str_list[n])
        count += count_digits(str_list[n])
        n += 1
    return r_list


test = ['ab12', 'IS111', '9', 'X7Z', 'k', 'lmn']
test2 = ["a1", "b2"]
print(get_strings_with_digits(test, 5))
print(get_strings_with_digits(test2, 5))
