# write a function to sequentially print out each element in a list which is a parameter of the function. you should ensure that a while loop is used and the code only has 1 line except the function definition line

def print_elements(my_list, index):
    while index < len(my_list):
        print(my_list[index])
        index += 1


print_elements([1, 2, 3, 4], 0)
