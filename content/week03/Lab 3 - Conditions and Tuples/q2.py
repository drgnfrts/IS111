# Q2 PART 1
# These variables are defined for you to use.
MEMBER_DISCOUNT_RATE = 0.10
SALE_ITEM_DISCOUNT_RATE = 0.05

# This function is for you to implement!


def calculate_price(orig_price, is_member, is_on_sale):

    # ################################################################################
    # Modify the code below to return the correct discounted price.
    discount_rate = 0
    if is_member:
        discount_rate += 0.1
    if is_on_sale:
        discount_rate += 0.05

    orig_price = orig_price * (1 - discount_rate)

    return orig_price
    # ################################################################################

# Q2 PART 2
# Write your code below to prompt the user for the following information:
# (1) The original price of the item.
# (2) Whether the user is a member or not.
# (3) Whether the item is on sale or not.:


input_original = float(input("What's the original price of the item: "))

if input("Are you a member [yes|no]? ") == "yes":
    input_member = True
else:
    input_member = False

if input("Is this item on sale [yes|no]? ") == "yes":
    input_sale = True
else:
    input_sale = False

print(
    f"The final price of the item is ${calculate_price(input_original, input_member, input_sale)}")
