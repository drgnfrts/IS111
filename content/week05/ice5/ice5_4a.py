'''
Q4a)

Implement a function called get_avg_len() that takes in a list of strings. The function returns the average length of all the strings in the given list. 

For example, get_avg_len(["C", "Java", "Python", "PHP"]) returns 3.5.
If the list is empty or if the strings are all empty strings, the function returns 0.
'''


def get_avg_len(list_of_strings):
    if len(list_of_strings) == 0:
        return 0
    total_length = 0
    for lang_string in list_of_strings:
        total_length += len(lang_string)
    return total_length / len(list_of_strings)


print(get_avg_len(["C", "Java", "Python", "PHP"]))
print(get_avg_len([]))