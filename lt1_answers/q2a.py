# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def trim_number(num1, num2):
    # Replace the code below with your implementation.
    str2 = str(num2)
    str1 = str(num1)[:-1]
    transformed_int = int(str1 + str2)
    if transformed_int < num1:
        return transformed_int
    else:
        return num1
