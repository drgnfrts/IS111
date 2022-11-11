friends = {}
with open("friends.txt", "r") as input_file:
    for line in input_file:
        stripped = line.strip("\n").split("\t")
        if stripped[0] not in friends:
            friends[stripped[0]] = [stripped[1]]
        else:
            friends[stripped[0]].append(stripped[1])

original = input("Name: ")
check = [original]
dos = int(input("Degrees of separation, n: "))
index = 1
final_list = []
friend_link = {}
while index <= dos:
    holding = []
    for name in check:
        if name in friends:
            holding += friends[name]
        for each_item in friends.items():
            each_key, each_val = each_item
            if name in each_val:
                holding.append(each_key)
    holding = list(set(holding))
    unique = []
    for i in range(len(holding)):
        if holding[i] not in final_list and holding[i] != original:
            unique.append(holding[i])
    check = unique
    final_list += unique
    friend_link[index] = unique
    index += 1

print(final_list)
print(friend_link)
