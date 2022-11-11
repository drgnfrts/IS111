# Name:
# Email ID:

def get_number_of_long_strings(str_list, n):
    # Modify the code below.
    count = 0
    for diff_string in str_list:
        if len(diff_string) > n:
            count += 1
    return count