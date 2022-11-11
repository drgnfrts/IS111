holding = []
subjects = []
name_list = []
index = 0

with open("eice10-1/grades.txt", "r") as phonebook:
    for line in phonebook:
        newlist = line.strip("\n").split("#")
        holding.append(newlist)


while index < len(holding):
    subject = holding[index][1] + " " + holding[index][2]
    if subject in subjects:
        index += 1
        continue
    name_list.append([subject])
    for entries in holding:
        if entries[1] + " " + entries[2] == subject:
            name_list[-1].append(entries[0])
    name_list[-1].pop(0)
    index += 1
    subjects.append(subject)

counted = []
for k in range(len(name_list)):
    duplicate = False
    if len(name_list[k]) < 2:
        index += 1
        continue
    elif len(name_list[k]) == 2:
        pair = tuple(name_list[k])
        for pairings in counted:
            if pair == pairings or (pairings[0] == pair[1] and pairings[1] == pair[0]):
                duplicate = True
                break
        if not duplicate:
            counted.append(pair)
    else:
        for i in range(len(name_list[k])):
            for j in range(len(name_list[k])):
                if i != j:
                    pair = (name_list[k][i], name_list[k][j])
                for pairings in counted:
                    if pair == pairings or (pairings[0] == pair[1] and pairings[1] == pair[0]):
                        duplicate = True
                        break
                if not duplicate:
                    counted.append(pair)

print(counted)
