while True:
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")
    if len(first) >= len(second) or " " in first or " " in second:
        print("Conditions not satisfied!")
        continue
    list_first = list(set(first))
    list_second = list(set(second))
    for i in range(len(list_first)):
        if list_first[i] not in list_second:
            ready = False
            break
        if i == len(list_first) - 1:
            ready = True
    if ready:
        print()
        break
    print("Conditions not satisfied!")
    print()

print("Bingo")
