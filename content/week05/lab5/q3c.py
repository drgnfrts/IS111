# Q3 Shopping Cart
# c)
# Write your code below:
##############################################################
def get_items_more_expensive_than(item_list, min_price):
    expensive_items = []
    for item_tuple in item_list:
        if item_tuple[1] > min_price:
            expensive_items.append(item_tuple)
    return expensive_items
##############################################################
# Test Cases to test your code
# DO NOT MODIFY THE TEST CODES


print('Test Case 1')
print('-' * 11)
item_list = [("milk", 5.45, 2), ("eggs", 2.45, 1), ("shampoo", 8.90, 2)]
print("Expected: [('milk', 5.45, 2), ('shampoo', 8.9, 2)]")
print('Actual:   ' + str(get_items_more_expensive_than(item_list, 3.0)))

print('\nTest Case 2')
print('-' * 11)
item_list = []
print("Expected: []")
print('Actual:   ' + str(get_items_more_expensive_than(item_list, 3.0)))
