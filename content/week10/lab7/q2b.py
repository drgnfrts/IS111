### Q2b: Universities
# Write your code below:
def get_average_num_students(file):
    unis = []
    total_students = 0
    avg_students = 0
    with open(file, "r") as newfile:
        for line in newfile:
            stripped = line.strip("\n").split("\t")
            unis.append(stripped)
    for uni in unis:
        total_students += int(uni[3])
    if len(unis) != 0:
        avg_students = total_students / len(unis)
    return avg_students
