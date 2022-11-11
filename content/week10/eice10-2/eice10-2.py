def frequent_three(filename):
    with open(filename, "r") as input_file:
        new_dict = {}
        for line in input_file:
            stripped = line.strip("\n").strip('"').split()
            for word in stripped:
                cleanword = word.lower().strip('"')
                if cleanword in new_dict:
                    new_dict[cleanword] += 1
                else:
                    new_dict[cleanword] = 1
    sort = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
    return sort[0], sort[1], sort[2]


frequent_three("article-1.txt")
