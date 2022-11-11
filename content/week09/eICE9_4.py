def group_numbers(list_of_ints, threshold):
    groupings = []
    index = 0
    while index < len(list_of_ints):
        total = 0
        subgroup = []
        while total <= threshold and index < len(list_of_ints):
            total += list_of_ints[index]
            if total <= threshold:
                subgroup.append(list_of_ints[index])
                index += 1
        groupings.append(subgroup)
    return groupings


list1 = [1, 3, 2, 4, 3, 2, 3, 6]
print(group_numbers(list1, 6))
