# Name:
# Email ID:

def get_longer_words(file_name):
    r_list = []
    with open(file_name, "r") as input_file:
        for line in input_file:
            stripped = line.strip("\n").split("&")
            word1, word2 = stripped
            if len(word1) >= len(word2):
                r_list.append(word1)
            else:
                r_list.append(word2)
    return r_list