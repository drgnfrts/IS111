def modify_list(my_list):
    for index in range(len(my_list)):
        x = my_list[index]
        if len(x) > 5:
            my_list[index] = x[0:5]


str_list = ["IS111", "Python", "Programming", "List"]

modify_list(str_list)
print(str_list)
# ["IS111", "Pytho", "Progr", "List"]


def modify_list_2(my_list):
    for element in my_list:
        if len(element) > 5:
            element = element[0:5]
            # here, the first element is a new variable but is not called at any point


str_list_2 = ["IS111", "Python", "Programming", "List"]

modify_list_2(str_list_2)
print(str_list_2)
# ["IS111", "Python", "Programming", "List"]
