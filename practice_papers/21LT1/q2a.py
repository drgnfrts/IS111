# Name:
# Email ID:

def get_right_most_even_digit(number):
    # Replace the code below with your implementation.
    dump_list = []
    dump_list[:0] = str(number)
    for i in range(-1, -(len(dump_list) + 1), -1):
        if int(dump_list[i]) % 2 == 0:
            return int(dump_list[i])
    return None
