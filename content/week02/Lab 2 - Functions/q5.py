# Lab2_Q5
# ########################################
# # lab2_Q5_part1: Write your code below:
def calculate_price_after_discount(unit_price, quantity, discount):
    return round(unit_price * quantity * (1 - discount / 100), 2)
    
# print(calculate_price_after_discount(1.50, 5, 10))

# ########################################
# lab2_Q5_part2: Write your code below:
milk = calculate_price_after_discount(5.95, 2, 10)
rice = calculate_price_after_discount(6.50, 1, 5)
eggs = calculate_price_after_discount(2.40, 2, 0)
kaya = calculate_price_after_discount(3.95, 3, 15)

total = round(milk + rice + eggs + kaya, 2)
print(f"The total of your shopping cart is {total}")
