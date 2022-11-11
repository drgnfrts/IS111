# Q1b Reading Files
# Write your code below:
def print_alternate_columns(file):
    grid = []

    with open(file, "r") as newfile:
        for line in newfile:
            row = line.strip("\n").split("&")
            grid.append(row)
    for row in grid:
        printout = []
        for j in range(0, len(row), 2):
            printout.append(row[j])
        for i in range(len(printout)):
            if i == len(printout) - 1:
                print(printout[i])
            else:
                print(printout[i], end="&")
