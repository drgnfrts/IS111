### Q2a: Universities
# Write your code below:
def get_universities_founded_before(file, year):
    unis = []
    r_list = []
    with open(file, "r") as newfile:
        for line in newfile:
            stripped = line.strip("\n").split("\t")
            unis.append(stripped)
    for uni in unis:
        if year > int(uni[2]):
            r_list.append(uni[0])
    return r_list
