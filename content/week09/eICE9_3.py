def merge_by_age(list1, list2):
    merged = []
    while not(len(list1) == 0 or len(list2) == 0):
        if list1[0][1] < list2[0][1]:
            merged.append(list1[0])
            list1.pop(0)
        else:
            merged.append(list2[0])
            list2.pop(0)
    if len(list1) > 0:
        merged += list1
    elif len(list2) > 0:
        merged += list2
    return merged


list1 = [("John", 12), ("Kate", 15), ("Henry", 35)]
list2 = [("Mike", 18), ("Scott", 20), ("Joseph", 48), ("Larry", 54)]
print(merge_by_age(list1, list2))
