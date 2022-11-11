valid_responses = ("M", "F")
while True:
    user_input = input("What's your gender? Please enter M or F: ")
    if user_input in valid_responses:
        print("Thanks! Your gender is ", end="")
        break
    print("Wrong input!")

if user_input == "M":
    print("male.")
else:
    print("female.")
