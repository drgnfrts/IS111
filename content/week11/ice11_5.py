mydict = {}
with open("phone_numbers.txt", "r") as input_file:
    for line in input_file:
        name, number = line.strip("\n").split("|")
        if name not in mydict:
            mydict[name] = [number]
        else:
            mydict[name].append(number)

searchval = input("Enter a person's name: ")
if searchval in mydict:
    print(f"{searchval} has {len(mydict[searchval])} number(s):")
    for num in mydict[searchval]:
        print(f"\t{num}")
else:
    print(f"{searchval} cannot be found in our database")
