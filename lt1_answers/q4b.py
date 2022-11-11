# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

import q4a


def find_overlapping_pairs(rect_list):
    # Replace the code below with your implementation.
    correct_list = []
    tested_list = []
    for i in range(len(rect_list)):
        for j in range(len(rect_list)):
            if i != j and (rect_list[i][0], rect_list[j][0]) not in tested_list:
                if q4a.is_overlapping(rect_list[i], rect_list[j]):
                    correct_list.append((rect_list[i][0], rect_list[j][0]))
                    tested_list += [(rect_list[i][0], rect_list[j][0]),
                                    (rect_list[j][0], rect_list[i][0])]
    return correct_list
