# Q3 Shopping Cart
# a)
# Write your code below:
##############################################################
def calculate_total_price(item_list):
    total_price = 0
    for item_tuple in item_list:
        total_price += item_tuple[1] * item_tuple[2]
    return total_price
##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES


print('Test Case 1')
print('-' * 11)
item_list = [("milk", 5.45, 2), ("eggs", 2.45, 1), ("shampoo", 8.90, 2)]
print('Expected: 31.15')
print('Actual:   ' + str(round(calculate_total_price(item_list), 2)))
