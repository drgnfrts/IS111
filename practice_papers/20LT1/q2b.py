# TO REVISE THIS QN

# Name:
# Email ID:

def get_max_of_min(list_of_num_tuples):
    # Replace the code below with your implementation.

    # Note: You’re NOT allowed to use either min()or max()to solve this problem.
    min_nos = []
    for num_tuple in list_of_num_tuples:
        min_nos = []
        num1, num2, num3 = num_tuple
        if num1 <= num2:
            if num1 <= num3:
                min_nos.append(num1)
            else:
                min_nos.append(num3)
        elif num2 <= num3:
            if num2 <= num1:
                min_nos.append(num2)
            else:
                min_nos.append(num1)
        elif num3 <= num1:
            if num3 <= num2:
                min_nos.append(num3)
            else:
                min_nos.append(num2)
    if min_nos == []:
        return None
    for i in range(len(min_nos)):
        lowest = 0
        if min_nos[i] <= lowest or i == 0:
            lowest = min_nos[i]
    return lowest
