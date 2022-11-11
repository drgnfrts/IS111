# Name:
# Email ID:

def transform(str1, str2):
    # Modify the code below.
    answers = [str1]
    list1 = list(str1)
    list2 = list(str2)
    for i in range(len(list2)):
        if list2[i] == list1[i]:
            continue
        org_pos = list1.index(list2[i])
        difference = org_pos - i
        for j in range(difference):
            swap_left = list1[org_pos - j]
            swap_right = list1[org_pos - j - 1]
            list1[org_pos - j] = swap_right
            list1[org_pos - j - 1] = swap_left
            answers.append("".join(list1))
    return answers
