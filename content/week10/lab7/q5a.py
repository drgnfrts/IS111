### Q5a: Matrix

# Write your code below:
def get_matrix(file):
    matrix = []
    with open(file, "r") as input_file:
        for line in input_file:
            stripped = line.strip("\n").split()
            for i in range(len(stripped)):
                stripped[i] = float(stripped[i])
            matrix.append(stripped)
    return matrix
