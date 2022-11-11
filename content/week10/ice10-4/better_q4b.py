# read the file ONCE
headline_list = []
with open("ice10-4/news.txt", "r") as headlines:
    for headline in headlines:
        mod = headline.strip("\n")
        headline_list.append(mod)

search = input("Do you want to search our news database? [Y|N]: ")
print()
while search == "Y":
    relevant = []
    num = 1
    keyword = input("Please enter a keyword or keyphrase: ").lower()
    with open("ice10-4/news.txt", "r") as headlines:
        for headline in headline_list:
            if keyword in headline.lower():
                relevant.append(f"\t{num}. {mod}")
                num += 1
    print()
    if relevant == []:
        print("There is no matching headline")
    else:
        print(f"There are {num} matching headlines:")
        for headline in relevant:
            print(headline)
    search = input("Do you want to search again? [Y|N]: ")
    print()
print("Goodbye!")
