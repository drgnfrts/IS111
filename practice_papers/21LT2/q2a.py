# Name:
# Email ID:
def extract_names_1(str_name):
    r_list = []
    splitted = str_name.split("#")
    for each_str in splitted:
        if each_str != "":
            r_list.append(each_str)
    return r_list
