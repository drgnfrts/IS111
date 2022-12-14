'''
(b) Define a function called compute_geometric_mean(). This function should take in three numbers and return the geometric mean of the three numbers. The geometric mean of three numbers x, y and z is defined as 3√(x * y * z) or (x * y * z) **(1/3).
'''
# ################################################################################
# Implement the function below:


def compute_geometric_mean(x, y, z):
    """
    This function returns the geometric mean of the three numbers x, y and z.
    """
    # Write your code here:
    return (x * y * z) ** (1/3)


# ################################################################################
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!
print("The geometric mean of 2, 4 and 6 is:", compute_geometric_mean(2, 4, 6))
