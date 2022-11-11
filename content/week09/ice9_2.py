num_str = ""

while True:
    num = int(input("Enter a number: "))
    if num % 2 == 1 and num > 0:
        num_str += str(num) + ", "
    if num <= 0:
        num_str = num_str[:-2]
        print("Thanks")
        break

print("The odd positive integers you have entered are the following: " + num_str)
