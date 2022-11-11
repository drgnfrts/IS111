# Q2 List of Numbers
# e)
# Write your code below:
##############################################################

def calculate_sums(num_list):
    summed_list = []
    for i in range(len(num_list)):
        summed_list.append(num_list[:i + 1])
        # summed_list.append(num_list[i])
        # for j in range(i):
        #     summed_list[i] += num_list[j]
    return summed_list


##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES
print('Test Case 1')
print('-' * 11)
print('Expected: [2, 5, 11, 12, 17]')
print('Actual:   ' + str(calculate_sums([2, 3, 6, 1, 5])))

print('\nTest Case 2')
print('-' * 11)
print('Expected: []')
print('Actual:   ' + str(calculate_sums([])))
