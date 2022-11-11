def reverse_dict(input_dict):
    r_dict = {}
    for each_item in input_dict.items():
        each_key, each_value = each_item
        r_dict[each_value] = each_key
    return r_dict


i_dict = {'Monday': 'swimming', 'Tuesday': 'basketball',
          'Wednesday': 'tennis', 'Thursday': 'yoga', 'Friday': 'gymnastics'}

print(reverse_dict(i_dict))
