detail_dict = {}
with open("employees.txt") as input_file:
    for line in input_file:
        stripped = line.strip("\n").split("\t")
        id_field, id_num = stripped[0].split(":")
        detail_dict[id_num] = {}
        for detail in stripped[1::]:
            newkey, newvalue = detail.split(":")
            detail_dict[id_num][newkey] = newvalue

start = "Y"

while start == "Y":
    id_search = input("Enter an employee ID: ")
    print(f"This employee is {detail_dict[id_search]['name']}")
    field = input("Enter a field name or 'S' to stop: ")
    while field != "S":
        print(f"\tThe {field} is {detail_dict[id_search][field]}")
        field = input("Enter a field name or 'S' to stop: ")
    start = input("Do you want to search for another employee? [Y|N]: ")
