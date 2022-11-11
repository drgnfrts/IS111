transactions = []
with open("transactions.txt", "r") as input_file, open("transactions-output-2.txt", "w") as output_file:
    for line in input_file:
        date, location, price = line[3::].strip("\n").split("\t")
        unique = True
        for i in range(len(transactions)):
            if transactions[i][0] == date:
                unique = False
                transactions[i][1] += float(price.strip("$"))
                transactions[i][2].append(location + "\t" + price)
        if unique:
            transactions.append(
                [date, float(price.strip("$")), [location + "\t" + price]])
    for monthly_receipts in transactions:
        month_year, total, locations = monthly_receipts
        output_file.write(
            f"{month_year}: total transaction amount is ${total}\n")
        for location in locations:
            output_file.write(f"\t{location}\n")
        output_file.write("\n")
