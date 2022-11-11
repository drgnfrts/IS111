def check_numbers(int_list_1, int_list_2):
    for integer1 in int_list_1:
        divisible = False  # need this line of code to reset the "divisible status"
        for integer2 in int_list_2:
            if integer1 % integer2 == 0:
                divisible = True
                break
        if not divisible:
            return False
    return True


print(check_numbers([3, 8, 10, 15, 16], [9, 3, 2, 5]))
print(check_numbers([3, 8, 10, 6, 2, 5], [9, 3, 7]))
