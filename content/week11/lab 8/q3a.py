facilities = {}
with open("facilities.txt", "r") as input_file:
    for line in input_file:
        school, room, capacity, projector = line.strip("\n").split("\t")
        if school not in facilities:
            facilities[school] = {room: (capacity, projector)}
        else:
            facilities[school][room] = (capacity, projector)

search = input("Do you want to search for a facility? [Y|N] :")
while search == "Y":
    school_search = input("Enter the school [LKCSB|SOE|SOL|SOA|SIS] :")
    room_search = input("Enter the room number :")
    if facilities[school_search][room_search][1] == "yes":
        has_projector = "has"
    else:
        has_projector = "does not have"
    print(
        f"{school_search} {room_search} has a capacity of {facilities[school_search][room_search][0]} and {has_projector} a projector")
    search = input("Do you want to continue the search? [Y|N] :")
print("Thank you for using our system!")
