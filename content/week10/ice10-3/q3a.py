holding = []
longest = 0
with open("phone_book.txt", "r") as phonebook:
    for line in phonebook:
        newlist = line.strip("\n").split("|")
        if "+65" in newlist[1] or (len(newlist[1]) == 8 and "+" not in newlist[1]):
            holding.append(newlist)
        if len(newlist[0]) > longest and newlist in holding:
            longest = len(newlist[0])
for item in holding:
    print(item[0] + (longest - len(item[0])) * " " + "\t" + item[1])
