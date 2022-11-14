# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def get_n_odd_numbers(filename, n):
    r_list = []
    num_list = []
    with open(filename, "r") as input_file:
        for line in input_file:
            stripped = int(line.strip("\n"))
            num_list.append(stripped)
    for num in num_list:
        if len(r_list) >= n:
            break
        if num % 2 == 1:
            r_list.append(num)
    return r_list
