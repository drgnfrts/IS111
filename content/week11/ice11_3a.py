def convert_to_dict(list_of_tuples):
    # newdict = {}
    # for indiv_tuple in list_of_tuples:
    #     newdict[indiv_tuple[0]] = indiv_tuple[1]
    # return newdict
    return dict(list_of_tuples)


tuple_list = [(1, 'apple'), (2, 'banana'), (4, 'durian'),
              (8, 'orange'), (3, 'peach')]

print(convert_to_dict(tuple_list))
