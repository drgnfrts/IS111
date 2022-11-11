def min_and_max(file):
    persons = []
    with open(file, "r") as newfile:
        for line in newfile:
            stripped = line.strip("\n").split("\t")
            persons.append(stripped)
    for person in persons:
        name = person[0]
        readings = []
        for i in range(1, len(person)):
            readings.append(float(person[i]))
        print(f"{name}: {min(readings)}, {max(readings)}")


min_and_max("temperatures.txt")
