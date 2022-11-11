'''
Q4b)
Implement a function called get_longest_str() that takes in a list of strings. The function returns the string that is the longest among all the strings in the given list. If there are multiple strings having the longest length, the function returns the first such string in the list.

For example, get_longest_str(["C", "Java", "Python", "PHP"]) returns "Python", and get_longest_str(["C", "Java", "HTML", "PHP"]) returns "Java".

If the list is empty, the function returns an empty string.
'''


def get_longest_str(list_of_strings):
    if len(list_of_strings) == 0:
        return ""
    longest_string = ""
    for lang_string in list_of_strings:
        if len(lang_string) > len(longest_string):
            longest_string = lang_string
    return longest_string


'''
def get_longest_str(list_of_strings):
    return max(list2, key=len)
'''


print(get_longest_str(["C", "Java", "Python", "PHP"]))
print(get_longest_str([]))
print(get_longest_str(["C", "Java", "HTML", "PHP"]))
