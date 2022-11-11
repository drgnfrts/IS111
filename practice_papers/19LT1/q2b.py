# Name:
# Email ID:

def add_even_numbers(str_list):
    # Modify the code below.
    number_list = []
    even_sum = 0
    if str_list == []:
        return 0
    for item in str_list:
        number_list = item.split("|")
        for number in number_list:
            num = int(number)
            if num % 2 == 0:
                even_sum += num
    return even_sum
