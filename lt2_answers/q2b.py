# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def filter_words(filename, end):
    # Replace the code below with your implementation.
    r_list = []
    word_list = []
    with open(filename, "r") as input_file:
        for line in input_file:
            stripped = line.strip("\n").split()
            for stripped_word in stripped:
                word_list.append(stripped_word)
    for word in word_list:
        if word[-1] == end:
            r_list.append(word)
    return r_list
