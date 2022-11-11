# Q4
# PART 1
# The following function is for you to implement.
def get_ticket_info(age):
    # Modify the code below to return the right value
    if 12 < age < 60:
        return 33, False
    elif age < 3:
        return 0, True
    elif 3 < age < 12:
        return 22, True
    else:
        return 15, True


# ################################################################################
# The code below is to test your implementation of the function above.
# DO NOT MODIFY THE CODE BELOW!

# The following line of code should display (33, False)
print(get_ticket_info(40))

# The following line of code should display (22, True)
print(get_ticket_info(10))


# PART 2
# Write your code below to prompt the user for age
# and print the expected output

input_age = int(input("How old are you? "))
payment_due, discount = get_ticket_info(input_age)

if discount:
    print("Congratulations! You qualify for a discount.")

print(f"You need to pay ${payment_due}")
