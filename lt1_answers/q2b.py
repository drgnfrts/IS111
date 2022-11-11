# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

import q2a


def trim_number_with_list(num, num_list):
    # Replace the code below with your implementation.
    for single_digit in num_list:
        if q2a.trim_number(num, single_digit) != num:
            return q2a.trim_number(num, single_digit)
    return num
