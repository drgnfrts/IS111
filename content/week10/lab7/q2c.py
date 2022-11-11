### Q2c: Universities
# Write your code below:
def search_with_keyword(file, keyword):
    unis = []
    r_list = []
    with open(file, "r") as newfile:
        for line in newfile:
            stripped = line.strip("\n").split("\t")
            unis.append(stripped)
    for uni in unis:
        if keyword.lower() in uni[0].lower():
            r_list.append(uni[1])
    return r_list
