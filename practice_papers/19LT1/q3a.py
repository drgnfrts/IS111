# Name:
# Email ID:

def calculate_entrance_fees_1(n):

    # These variables are defined for you to use.
    PACKAGE_B = 110
    PACKAGE_C = 200
    num_b = n % 2
    num_c = n // 2

    # Modify the code below.
    return num_b * PACKAGE_B + num_c * PACKAGE_C
        