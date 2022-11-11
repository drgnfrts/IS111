import week2_utility

user_age = int(input("What is your age?: "))
user_gender = input("What is your gender? (M / F): ")

premium = week2_utility.get_insurance_premium(user_age, user_gender)
print(f"Your premium is {premium}.")
