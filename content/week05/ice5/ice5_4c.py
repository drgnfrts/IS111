'''
Q4c) Implement a function called concatenate_emails(). This function takes in a list of strings, where some of these strings are email address. The function returns a string that contains the email addresses separated by semi-colons. 

Here a string is considered an email address if it contains exactly one '@' symbol and it does not contain any space.

For example, concatenate_emails(["IS111", "a @ b", "jerry.lee@sis.smu.edu.sg", "@@@", "alan_wong@gmail.com", "Python", "george_tan@yahoo.com"]) returns "jerry.lee@sis.smu.edu.sg;alan_wong@gmail.com;george_tan@yahoo.com".

If the list is empty, the function returns an empty string.

'''


def concatenate_emails(list_of_strings):
    if len(list_of_strings) == 0:
        return ""
    correct_emails = []
    for indiv_string in list_of_strings:
        if "@" not in indiv_string:
            continue
        for i in range(len(indiv_string)):
            if indiv_string[i] == "@" and indiv_string[i - 1].isalpha() and indiv_string[i + 1].isalpha():
                correct_emails.append(indiv_string)
    # alternate to for the outer loop, easier method below
    '''
    for i in range(len(list_of_strings)):
        if list_of_strings[i].count(@) == 1 and " " not in list_of_strings[i]:
            correct_emails.append(indiv_string)
    '''
    combined_string = ";".join(correct_emails)
    return combined_string


my_list1 = ["tommy.goh@sis.smu.edu.sg", "alan_wong@gmail.com"]
print(concatenate_emails(my_list1))
my_list2 = []
print(concatenate_emails(my_list2))
my_list3 = ["IS111", "a @ b", "jerry.lee@sis.smu.edu.sg", "@@@",
            "alan_wong@gmail.com", "Python", "george_tan@yahoo.com"]
print(concatenate_emails(my_list3))
