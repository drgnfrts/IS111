# Name:
# Email ID:

def check_sum(n1, n2, n3):
    # Modify the code below.
    if n1 + n2 == n3:
        return True
    if n2 + n3 == n1:
        return True
    if n1 + n3 == n2:
        return True
    return False
    