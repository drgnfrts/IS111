'''
E2)

Write a function called compute_avg_height. The function takes in a single parameter, which a string that consists of some people's heights. An example of such a string is "Jonathan Li:1.75m, Lim, Josephine : 1.59m , George Khoo:   1.7 m". We can see that for each person, the person's name is given, followed by a colon. After that there may be zero, one or more spaces, followed by the person height. The person's height is followed by the letter 'm', but there might be zero, one or more spaces before 'm' and after 'm'. The function compute_avg_height should return the average height of all the people listed in the string.
You can assume that the input string is always well formatted as described above. To be more specific, you can assume the following:
•	Digits and the symbol '.' appear only as part of a person's height.
•	A person's name doesn't contain the symbol ':'.
•	However, a person's name may be expressed as '<surname>, <given name>', such as 'Lim, Josephine'.
•	The string parameter contains at least one person's height.
'''


def compute_avg_height(string_of_heights):
    total_height = 0
    colon_count = 0
    for ch in string_of_heights:
        if ":" in ch:
            colon_count += 1
    list_of_details = string_of_heights.split(":")
    for item in list_of_details:
        item_height = []
        for ch in item:
            if ch.isdigit() or ch == ".":
                item_height.append(ch)
        if item_height == []:
            pass
        else:
            total_height += float("".join(item_height))
    return total_height / colon_count


print(compute_avg_height(
    "Jonathan Li:1.75m, Lim, Josephine : 1.59m , George Khoo:   1.7 m"))
