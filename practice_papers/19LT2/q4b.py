# Name:
# Email ID:

def get_relation_through_link(family_dict, link):
    # Modify the code below.
    rs_dict = {}
    with open("relation_mapping.txt", "r") as input_f:
        for line in input_f:
            stripped = line.strip("\n").split("):")
            rs1, rs2 = stripped[0].split(",")
            rs1 = rs1.strip("(")
            rs_dict[(rs1, rs2)] = stripped[1]
    final_rs = ""
    hold_rs = ""
    for i in range(len(link) - 1):
        if hold_rs == "":
            hold_rs = family_dict[(link[i], link[i + 1])]
        else:
            hold_rs = rs_dict[hold_rs, family_dict[(link[i], link[i + 1])]]
    return hold_rs
