from q5a import count_words_in_file


def get_words_by_count(input_dict):
    r_dict = {}
    for word, num in input_dict.items():
        if num in r_dict:
            r_dict[num].append(word)
        else:
            r_dict[num] = [word]
    return r_dict


mydict = get_words_by_count(count_words_in_file("spam_sms.txt"))
highest_to_lowest = sorted(mydict.items())[-1::-1]
print(highest_to_lowest[0:10])
