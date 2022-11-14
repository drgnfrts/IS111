# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

from itertools import combinations


def find_all_words(word_list, input_str, step):
    # Replace the code below with your implementation.
    r_list = []
    input_list = []
    for i in range(len(input_str)):
        input_list.append(i)
    for word in word_list:
        have_combi = False
        combis = combinations(input_list, len(word))
        for combi in combis:
            combi = list(combi)
            hold = ""
            for num in combi:
                hold += input_str[input_list[num]]
            if hold == word:
                valid = True
                for j in range(len(combi) - 1):
                    if combi[j + 1] - combi[j] < step:
                        valid = False
                if valid:
                    have_combi = True
                    r_list.append(combi)
        if not have_combi:
            r_list.append([])
    return r_list
