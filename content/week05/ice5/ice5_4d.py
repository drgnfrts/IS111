'''
Q4d)
Implement a function called check_hashtags(). The function takes in a list of strings. The function returns True if all the strings are hashtags, i.e., all the strings start with a '#' symbol and do not contain any space. The function returns False if at least one of the strings is not a hashtag.
'''

def check_hashtags(list_of_hashtags):
    if len(list_of_hashtags) == 0:
        return False
    for hashtag in list_of_hashtags:
        if hashtag[0] == "#" and " " not in hashtag:
            continue
        else:
            return False
    return True

# note do not put return too early in the function, else it may risk returning True on the first variable without checking

print(check_hashtags(["#singapore", "#music", "#travel"]))
print(check_hashtags([]))
print(check_hashtags(["#singapore", "#music album", "#travel"]))
print(check_hashtags(["singapore", "#music", "#travel"]))