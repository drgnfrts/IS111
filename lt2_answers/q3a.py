# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def read_courses(filename):
    r_dict = {}
    with open(filename, "r") as input_file:
        for line in input_file:
            stripped = line.strip("\n").split("|")
            year_term, name, course, credit, score = stripped
            credit = int(credit)
            score = float(score)
            year, term = year_term.split("-")
            year = int(year)
            term = int(term[-1])
            if name in r_dict:
                r_dict[name].append((course, year, term, credit, score))
            else:
                r_dict[name] = [(course, year, term, credit, score)]
    return r_dict
