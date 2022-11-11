# Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):

    # This variable is defined for you to use.
    BASE_SALARY = 2000.0

    # ################################################################################
    # Modify the code below to return the right amount of salary.
    if monthly_sales < 10000:
        total_salary = BASE_SALARY + monthly_sales * 0.05
    elif 10000 <= monthly_sales < 15000:
        total_salary = BASE_SALARY + monthly_sales * 0.10
    elif 15000 <= monthly_sales < 18000:
        total_salary = BASE_SALARY + monthly_sales * 0.15
    else:
        total_salary = BASE_SALARY + monthly_sales * 0.18

    return round(total_salary, 2)
    # ################################################################################

# Q3 PART 2
# Write your code below


input_sales = float(input("Enter monthly sales amount($): "))
print(
    f"The monthly pay for the salesperson is ${calculate_salary(input_sales)}")
