# =====
# q2.py
# =====
# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def add_first_odd_digits(str_list):
    odd_digits = []
    # OR sum_digits = 0
    for word_str in str_list:
        for ch in word_str:
            if ch.isdigit() and int(ch) % 2 == 1:
                # OR if ch in (1, 3, 5, 7, 9)
                odd_digits.append(int(ch))
                # OR sum_digits += int(ch)
                break
    return sum(odd_digits)  # OR sum_digits
