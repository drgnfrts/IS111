holding = []
subjects = []
index = 0

with open("eice10-1/grades.txt", "r") as phonebook:
    for line in phonebook:
        newlist = line.strip("\n").split("#")
        if newlist[3] == "A":
            holding.append(newlist)


while index < len(holding):
    subject = holding[index][1]
    if subject in subjects:
        index += 1
        continue
    print(subject)
    for entries in holding:
        if entries[1] == subject:
            print(entries[0])
    print()
    index += 1
    subjects.append(subject)
