# =====
# q3.py
# =====
# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def pad_strings(str_list, ch):
    # modify the code below
    padded_strs = []
    longest_word = 0
    for i in range(len(str_list)):
        if len(str_list[i]) > longest_word:
            longest_word = len(str_list[i])
    for j in range(len(str_list)):
        front_pad_len = len(str_list) - 1 - j
        back_pad_len = longest_word - len(str_list[j])
        padded_word = (front_pad_len * " ") + str_list[j] + (back_pad_len * ch)
        padded_strs.append(padded_word)

    return padded_strs
