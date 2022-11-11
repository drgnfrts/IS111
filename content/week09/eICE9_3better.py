def merge_by_age(list1, list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i][1] < list2[j][1]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    if len(list1) > i:
        merged += list1[i:len(list1)]
    elif len(list2) > j:
        merged += list2[j:len(list2)]
    return merged


list1 = [("John", 12), ("Kate", 15), ("Henry", 35)]
list2 = [("Mike", 18), ("Scott", 20), ("Joseph", 48), ("Larry", 54)]
print(merge_by_age(list1, list2))
