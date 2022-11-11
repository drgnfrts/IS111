# Name:
# Email ID:

def get_all_third_digits(str_list):
    third_digit_list = []
    for string in str_list:
        digit_count = 0
        for ch in string:
            if ch.isdigit():
                digit_count += 1
                if digit_count == 3:
                    third_digit_list.append(int(ch))
                    break
    return third_digit_list
