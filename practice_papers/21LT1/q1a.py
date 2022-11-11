# Name:
# Email ID:

def get_area_difference(width1, length1, width2, length2):
    # Replace the code below with your implementation.
    rec1 = width1 * length1
    rec2 = width2 * length2
    return max(rec1, rec2) - min(rec1, rec2)