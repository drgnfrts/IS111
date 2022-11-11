def get_larger_values(list_of_values):
    total = 0
    larger_values = []
    for value in list_of_values:
        total += value
    average = total / len(list_of_values)
    for value in list_of_values:
        if value > average:
            larger_values.append(value)
    return larger_values


print(get_larger_values([2.5, 3.5, 5.5, 1.0]))
