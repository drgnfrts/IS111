### Q5b: Matrix

# Write your code below:
from q5a import get_matrix


def get_matrix_transpose(file):
    transposed = []
    index = 0
    original = get_matrix(file)
    while index < len(original):
        new_row = []
        for row in original:
            new_row.append(row[index])
        transposed.append(new_row)
        index += 1
    return transposed
