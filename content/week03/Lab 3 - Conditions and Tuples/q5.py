# Q5
# The following function is provided to you.
# Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# Write your code below:

user_name, user_gender, user_age, student = get_user_info()

if user_gender == "M":
    address = "Mr."
else:
    address = "Ms."

if user_age <= 6:
    print(f"{user_name}, you can travel for free.")
elif 6 < user_age < 60 and student:
    print(f"{address} {user_name}, you can get concessionary fare for students.")
elif user_age >= 60:
    print(f"{address} {user_name}, you can get concessionary fare for senior citizens.")
else:
    print(f"{address} {user_name}, you need to pay full fare.")
