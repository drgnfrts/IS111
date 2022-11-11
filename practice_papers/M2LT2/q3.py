def check_age(student_list):
    # Modify the code below.
    check = True
    for each_tuple in student_list:
        name, gender, age = each_tuple
        if gender == "M" and int(age) < 20:
            return False
    return check


# Do not modify the code below!!!
if __name__ == '__main__':
    print("Test Case for Q3")

    print('\nTestcase 1')
    print('-' * 10)
    my_list = [('John', 'M', '21'), ('Kate', 'F', '19'), ('Eric', 'M', '23')]
    print("Expected: True")
    print('Actual:   ' + str(check_age(my_list)))

    print('\nTestcase 2')
    print('-' * 10)
    my_list = [('John', 'M', '21'), ('Kate', 'F', '19'), ('Jerry', 'M', '19')]
    print("Expected: False")
    print('Actual:   ' + str(check_age(my_list)))

    print('\nTestcase 3')
    print('-' * 10)
    my_list = [('Kate', 'F', '19')]
    print("Expected: True")
    print('Actual:   ' + str(check_age(my_list)))
