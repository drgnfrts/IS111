# Name:
# Email ID:

def get_sum_of_digits(my_str):
    # Replace the code below with your implementation.
    digits_list = []
    for ch in my_str:
        if ch.isdigit():
            digits_list.append(int(ch))
    if digits_list == []:
        return 0
    return sum(digits_list)
