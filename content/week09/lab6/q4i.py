total = 0
while True:
    anything_left = input(
        "Do you have any item left in your shopping cart? Please enter Y or N: ")
    if anything_left == "N":
        print(f"Total price: ${total}")
        break
    name = input("Please enter the name of the item : ")
    price = float(input("Please enter the price of the item : "))
    qty = int(input("Please enter the quantity of the item : "))
    total += (price * qty)
    print()
