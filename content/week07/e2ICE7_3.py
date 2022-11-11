def flatten(my_list):
    z = str(my_list).replace("[", "").replace(
        "]", "").replace(" ", "").split(",")
    for i in range(len(z)):
        z[i] = int(z[i])
    return z


x = [4, 39, [35, 12, [45], 32], 4, [35, [4, [6]]]]
print(flatten(x), isinstance(flatten(x), list))
