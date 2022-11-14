# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def find_words(word_list, input_str, step):
    r_list = []
    for each_word in word_list:
        hold = ""
        indexes_found = []
        i = 0
        for k in range(len(each_word)):
            while i < len(input_str):  # or each_word[k] != input_str[i]:
                if input_str[i] == each_word[k]:
                    if indexes_found == []:
                        indexes_found.append(i)
                        hold += input_str[i]
                        i += 1
                        break
                    elif i - indexes_found[-1] >= step:
                        indexes_found.append(i)
                        hold += input_str[i]
                        i += 1
                        break
                i += 1
        if hold == each_word:
            r_list.append(indexes_found)
        else:
            r_list.append([])
    return r_list
