def sum_up(filename):
    total_list = []
    with open(filename, "r") as new_file:
        for line in new_file:
            total_list.append(float(line))
    return sum(total_list)


# Test cases
print('Test case 1')
print('===========')
your_sum = sum_up('q1-1.txt')
print('Expected: ', 55.4)
print('Actual:   ', round(your_sum, 1))

print('\nTest case 2')
print('===========')
your_sum = sum_up('q1-2.txt')
print('Expected: ', 55.0)
print('Actual:   ', round(your_sum, 1))
