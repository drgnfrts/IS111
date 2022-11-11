def get_strings(str_list, t):
    r_list = []
    count = 0
    i = 0
    while count <= t:
        r_list.append(str_list[i])
        count += len(str_list[i])
        i += 1
    return r_list


print(get_strings(['a', 'bc', 'defgh', 'ij', 'k', 'lmn'], 9))
