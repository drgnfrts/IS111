# Q4 Students and Schools
# write your code below
def get_students_by_school(input_dict):
    r_dict = {}
    for name, school in input_dict.items():
        if school in r_dict:
            r_dict[school].append(name)
        else:
            r_dict[school] = [name]
    return r_dict
