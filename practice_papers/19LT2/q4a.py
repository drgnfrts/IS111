# Name:
# Email ID:

def bracket_remover(name):
    return str(name.strip("(").strip(")"))


def store_family_relations(family_file):
    # Modify the code below.
    fam_dict = {}
    with open(family_file, "r") as input_f:
        for line in input_f:
            parents, kids = line.strip("\n").split(":")
            parents = parents.split(",")
            if ";" in kids:
                kids = kids.split(";")
                for k in range(len(kids)):
                    kids[k] = bracket_remover(kids[k])
            else:
                kids = [str(bracket_remover(kids))]
            print(kids, type(kids))
            for i in range(len(parents)):
                for j in range(len(kids)):
                    p = bracket_remover(parents[i])
                    cgender = kids[j][-1]
                    cname = kids[j][0:len(kids[j]) - 1]
                    print(cgender, cname)
                    if cgender == "M":
                        fam_dict[(cname, p)] = "Son"
                    else:
                        fam_dict[(cname, p)] = "Daughter"
                    if i == 0:
                        fam_dict[(p, cname)] = "Father"
                    else:
                        fam_dict[(p, cname)] = "Mother"
    return fam_dict
