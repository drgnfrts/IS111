def display_all_gpas(dictionary):
    print("Student Name\tStudent GPA")
    print("------------\t-----------")
    for the_items in dictionary.items():
        name, gpa = the_items
        print(f"{name}{(12 - len(name)) * ' '}\t{gpa}")


gpa_dict = {'George Leung': 3.4, 'Eric Wong': 3.9, 'Michelle Lee': 3.1}

display_all_gpas(gpa_dict)
