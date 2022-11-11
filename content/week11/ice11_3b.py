def read_into_dict(filename):
    mydict = {}
    with open(filename, "r") as input_file:
        for line in input_file:
            stripped = line.strip("\n").split("\t")
            mydict[stripped[0]] = stripped[1]
    return mydict


print(read_into_dict("acronyms.txt"))
