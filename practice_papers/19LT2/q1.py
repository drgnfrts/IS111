# Name:
# Email ID:

def compute_product(num_list):
    product = 1
    for num in num_list:
        if num % 2 == 1:
            product *= num
    return product
