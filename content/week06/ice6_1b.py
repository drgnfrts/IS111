def merge_list(list1, list2):
    new_list = []
    for i in range(max(len(list1), len(list2))):
        if i < len(list1):
            new_list.append(list1[i])
        if i < len(list2):
            new_list.append(list2[i])
    return new_list


print(merge_list([1, 3, 10, 15, 4, 7, 12], [9, 5, 2]))
