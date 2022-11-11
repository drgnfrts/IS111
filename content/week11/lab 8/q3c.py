facilities = {}
with open("facilities.txt", "r") as input_file:
    for line in input_file:
        school, room, capacity, projector = line.strip("\n").split("\t")
        if school not in facilities:
            facilities[school] = {room: (int(capacity), projector)}
        else:
            facilities[school][room] = (int(capacity), projector)

search = input("Do you want to search for a facility? [Y|N] :")
while search == "Y":
    school_search = input("Enter the school [LKCSB|SOE|SOL|SOA|SIS] :")
    capacity_search = int(input("Enter the minimum capacity you need:"))
    print(
        f"The following facilities with a capacity of {capacity_search} or above are found in {school_search}:")
    print("\tRoom #\tCap\tProjector?")
    print("\t------\t---\t----------")
    for room, details in facilities[school_search].items():
        if details[0] >= capacity_search:
            print(f"\t{room}\t{details[0]}\t{details[1]}")
    print()
    search = input("Do you want to continue the search? [Y|N] :")
print("Good-bye!")
