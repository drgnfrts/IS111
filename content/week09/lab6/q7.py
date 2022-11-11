def line_up(list_of_tuples):
    lined_up = []
    while len(lined_up) != len(list_of_tuples):
        for each_tuple in list_of_tuples:
            if "" in each_tuple and each_tuple[0] not in lined_up:
                lined_up.append(each_tuple[0])
            elif len(lined_up) != 0 and each_tuple[1] == lined_up[0] and each_tuple[0] not in lined_up:
                lined_up.insert(0, each_tuple[0])
    return lined_up


print(line_up([("Mary", "Jason"), ("John", "Alan"), ("Jason", "George"),
      ("Alan", "Christie"), ("Christie", "Mary"), ("George", "")]))
