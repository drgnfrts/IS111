# Q6 More on Lists
# b)
# Write your code below:
##############################################################
def get_larger_numbers(num_list1, num_list2):
    return_list = []
    for num1 in num_list1:
        for num2 in num_list2:
            if num1 > num2:
                bigger = True
            else:
                bigger = False
                break
        if bigger:
            return_list.append(num1)
    return return_list


    ##############################################################
    # Test Cases to test your code
    # DO NOT MODIFY THE TEST CODES
r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()
