# Q1 Reading Files
# Write your code below:
##############################
def print_alternate_lines(file):
    count = 0
    with open(file, "r") as newfile:
        for line in newfile:
            strip = line.strip('\n')
            if count % 2 == 0:
                print(strip)
            count += 1

# def print_alternate_lines(file):
#     lines = []
#     with open(file, "r") as newfile:
#         for line in newfile:
#             strip = line.strip('\n')
#             lines.append(strip)
#     for i in range(len(lines)):
#         if i % 2 == 0:
#             print(lines[i])