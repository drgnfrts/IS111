def common_words(dict, key1, key2):
    common = 0
    list1 = dict[key1]
    list2 = dict[key2]
    for word in list1:
        if word in list2:
            common += 1
    return common


def get_document_pair(filename):
    # Modify the code below.
    with open(filename, "r") as input_file:
        hold_dict = {}
        docs = []
        for line in input_file:
            stripped = line.strip("\n").split()
            strkey = stripped[0]
            words = stripped[1::]
            docs.append(strkey)
            hold_dict[strkey] = list(set(words))
    highest = ["", "", 0]
    for i in range(len(docs)):
        for j in range(len(docs)):
            if i != j and common_words(hold_dict, docs[i], docs[j]) > highest[2]:
                highest = [docs[i], docs[j], common_words(
                    hold_dict, docs[i], docs[j])]
    return tuple(highest)


# Do not modify the code below!!!
if __name__ == '__main__':
    print("Test Case for Q3")
    print('-' * 10)
    print('Test case 1')
    print('Expected:', ('D2', 'D4', 3), 'or', ('D4', 'D2', 3))
    result = get_document_pair('documents.txt')
    print('Actual:  ', result)
    print()
