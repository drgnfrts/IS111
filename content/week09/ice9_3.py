voucher = 100
book = float(input("Please pick a book. How much left is in it (in $)? "))
voucher -= book
while voucher > 0:
    print(f"You still have ${voucher:.2f} left")
    book = float(
        input("Please pick another book. How much left is in it (in $)? "))
    voucher -= book

print("You are done!")
print(f"The total price is ${100 + -(voucher)}")
