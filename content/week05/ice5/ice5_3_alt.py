import string


def is_valid_username(username):
    pool = "_.!#$%?" + string.ascii_lowercase + string.digits
    if len(username) > 8 or username == "":
        return False
    for character in username:
        if character not in pool:
            return False
    return True


username_list = ['abcdefgh', 'abcdefghi', 'ab$cd', 'ab_cd',
                 'ab-cd', 'ab:cd', '', 'ab cd', 'abcDef', 'abc8ef']
for username in username_list:
    print(
        f"The username {username} is valid : {str(is_valid_username(username))}")
