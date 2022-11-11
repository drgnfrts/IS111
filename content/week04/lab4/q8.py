# Q8
# ################################################################################
# The function below is for you to implement!
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn't return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers
    for i in range(n):
        if i == 0:
            return_string = "1"
        elif i == 1:
            return_string = "1 1"
            f_tuple = (1, 1)
        else:
            current_value = f_tuple[i - 1] + f_tuple[i - 2]
            f_tuple += current_value,
            return_string += str(f" {current_value}")

    print(return_string)
