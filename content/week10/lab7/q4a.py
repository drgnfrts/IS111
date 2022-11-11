def above_thirty(file):
    transactions = []
    eligible = ""
    with open(file, "r") as newfile:
        for line in newfile:
            stripped = line.strip("\n").split("\t")
            transactions.append(stripped)
    for transaction in transactions:
        cost = float(transaction[2].strip("$"))
        if cost > 30:
            eligible += "\t".join(transaction) + "\n"
    with open("transactions-output-1.txt", "w") as output_file:
        output_file.write(eligible)


above_thirty("transactions.txt")
