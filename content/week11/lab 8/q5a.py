# Q5a Word Counts
# write your code below
def count_words_in_file(filename):
    r_dict = {}
    with open(filename, "r") as input_file:
        for line in input_file:
            stripped = line.strip().split()
            for word in stripped:
                check = word.lower()
                if check in r_dict:
                    r_dict[check] += 1
                else:
                    r_dict[check] = 1
    return r_dict
