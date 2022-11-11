# Name:
# Email ID:
def get_tuples_of_size(tup_list, num):
    r_list = []
    for each_tuple in tup_list:
        if len(each_tuple) >= num:
            r_list.append(each_tuple)
    return r_list