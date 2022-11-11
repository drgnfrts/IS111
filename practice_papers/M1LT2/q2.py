def get_reversed_list(num_list):
    # Modify the code below.
    r_list = []
    for num in num_list:
        if num == 0 or num == 0.0:
            r_list.append(num)
        else:
            r_list.append(-num)
    return r_list[-1::-1]


# do not modify this test code
if __name__ == "__main__":
    # Test Cases of Q2

    print('\nTestcase 1')
    print('-' * 10)
    my_list = [1.5, 2.5, 3.9]
    print("Expected: [-3.9, -2.5, -1.5]")
    print('Actual:   ' + str(get_reversed_list(my_list)))

    print('\nTestcase 2')
    print('-' * 10)
    my_list = [4.5, 0.0]
    print("Expected: [0.0, -4.5]")
    print('Actual:   ' + str(get_reversed_list(my_list)))

    print('\nTestcase 3')
    print('-' * 10)
    my_list = []
    print("Expected: []")
    print('Actual:   ' + str(get_reversed_list(my_list)))
