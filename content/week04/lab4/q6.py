# Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
def calculate_price_after_discount(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    return (unit_price * quantity * (1 - discount_rate/100))


def final_price_plus_savings(unit_price, quantity, discount_rate):
    return (unit_price * quantity * (1 - discount_rate/100)), (unit_price * quantity * (discount_rate/100))

######################################################################################
# Write your solution below for Part A:
# in function so that i can keep the different parts from running


def part_a():
    number_of_items = int(input("How many items do you want to check out? "))
    total_amt = 0
    for i in range(number_of_items):
        item_name = input("What's this item? ")
        item_price = float(input("What's the unit price of this item? "))
        item_qty = int(input("What's the quantity of this item? "))
        if input("Does this item have any discount? [yes|no] ") == "yes":
            item_discount = float(
                input("What's the percentage of discount (%)? "))
        else:
            item_discount = 0
        total_amt += calculate_price_after_discount(
            item_price, item_qty, item_discount)
    return total_amt

# print(f"The total amount you have to pay is {round(part_a(), 2)}")

######################################################################################
# Write your solution below for Part B:
# in function so that i can keep the different parts from running


def part_b():
    number_of_items = int(input("How many items do you want to check out? "))
    total_amt = 0
    total_savings = 0
    for i in range(number_of_items):
        item_name = input("What's this item? ")
        item_price = float(input("What's the unit price of this item? "))
        item_qty = int(input("What's the quantity of this item? "))
        if input("Does this item have any discount? [yes|no] ") == "yes":
            item_discount = float(
                input("What's the percentage of discount (%)? "))
        else:
            item_discount = 0
        st_amt, st_savings = final_price_plus_savings(
            item_price, item_qty, item_discount)
        total_amt += st_amt
        total_savings += st_savings
    return total_amt, total_savings


total, saved = part_b()
print(f"The total amount you have to pay is ${round(total, 2)}.")
print(f"You have saved ${round(saved, 2)}")

# for self note/revision: can be modified such that the print statements remain inside the function, and no need for return. but this is fine as well.
