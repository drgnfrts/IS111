# Q6 More on Lists
# c)
# Write your code below:
##############################################################
def get_non_common_strings(str_list1, str_list2):
    return_list = str_list1
    for item in str_list2:
        if item not in return_list:
            return_list.append(item)
        else:
            return_list.remove(item)
    return return_list

##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES


r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()
