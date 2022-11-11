'''
Write a Python function sum_of_neighbours that takes in a single list parameter input_list. The function returns a list with the same number of elements as the original list, such that each integer in the new list is the sum of its immediate neighbours and itself in the original list.

If input_list = [10, 20, 30, 40, 50] return list should be [30, 60, 90, 120, 90]
'''


def sum_of_neighbours(input_list):
    if len(input_list) == 0 or len(input_list) == 1:
        return input_list
    # if len(input_list) == 2: -> no need, handled by the for loop scenarios
    #     sum_of_two = input_list[0] + input_list[1]
    #     return [sum_of_two, sum_of_two]
    return_list = []
    for i in range(len(input_list)):
        if i == 0:
            return_list.append(input_list[i] + input_list[i + 1])
            # OR return_list.append(sum(input_list[i:i+2]))
        elif i == len(input_list) - 1:
            return_list.append(input_list[i - 1] + input_list[i])
            # OR return_list.append(sum(input_list[i-1:i+1]))
        else:
            return_list.append(
                input_list[i - 1] + input_list[i] + input_list[i + 1])
            # OR return_list.append(sum(input_list[i-1:i+2]))
    return return_list


''' 
# ALTERNATE TO FOR LOOP

return list = [input_list[i] + input_list[i + 1]]
for i in range(len(input_list)):
    if i == len(input_list) - 1:
        return_list.append(sum(input_list[i-1:i+1]))
    return_list.append(input_list[i - 1] + input_list[i] + input_list[i + 1])

# PROF'S SOLUTION - OPTIMAL
def sum_of_neighbours(input_list):
    x = []
    for i in range(len(input_list)):
        x.append(input_list[i])
        if 0 <= i + 1 < len(input_list):
            x[i] += input_list[i + 1]
        if 0 <= i - 1 < len(input_list):
            x[i] += input_list[i - 1]
    return x

# for challenging problems, write out the comments for the steps then code
'''


print(sum_of_neighbours([10, 20, 30, 40, 50]) == [30, 60, 90, 120, 90])
print(sum_of_neighbours([23]) == [23])
print(sum_of_neighbours([56, -10, 25, -32]) == [46, 71, -17, -7])
print(sum_of_neighbours([12, 12]))
