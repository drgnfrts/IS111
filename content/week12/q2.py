storedict = {}
start = input("Enter a string > ")
while start != " ":
    if start[0].isalpha():
        startkey = start[0].lower()
    else:
        startkey = start[0]
    if startkey in storedict:
        storedict[startkey] += 1
    else:
        storedict[startkey] = 1
    start = input("Enter a string > ")
print()
print("You've entered:")
for eachkey in storedict.keys():
    if storedict[eachkey] > 1:
        s = "s"
    else:
        s = ""
    if eachkey.isalpha():
        print(
            f"{storedict[eachkey]} string{s} starting with '{eachkey}' or '{eachkey.upper()}'")
    else:
        print(
            f"{storedict[eachkey]} string{s} starting with '{eachkey}'")
