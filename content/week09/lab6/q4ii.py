total = 0
longest = 0
reciept = []
while True:
    anything_left = input(
        "Do you have any item left in your shopping cart? Please enter Y or N: ")
    if anything_left == "N":
        print()
        break
    name = input("Please enter the name of the item : ")
    if len(name) > longest:
        longest = len(name)
    price = float(input("Please enter the price of the item : "))
    qty = int(input("Please enter the quantity of the item : "))
    total += (price * qty)
    reciept.append((name, price, qty))
    print()

print("You've entered the following items:")
for each_tuple in reciept:
    item_name, item_price, item_qty = each_tuple
    mid_gap = 2 + (longest - len(item_name))
    print("    " + item_name + mid_gap * " " + "$" +
          str(item_price) + "    " + str(item_qty))
    print(f"Total price: ${total}")
