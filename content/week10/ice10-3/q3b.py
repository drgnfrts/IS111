holding = []
names = []
index = 0

with open("phone_book.txt", "r") as phonebook:
    for line in phonebook:
        newlist = line.strip("\n").split("|")
        holding.append(newlist)

while index < len(holding):
    name = holding[index][0]
    if name in names:
        index += 1
        continue
    with open("phone_book_reorganised.txt", "a") as output_book:
        output_book.write(name + "\n")
        for entries in holding:
            if entries[0] == name:
                output_book.write(entries[1] + "\n")
        output_book.write("\n")
    index += 1
    names.append(name)
