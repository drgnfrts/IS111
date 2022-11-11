def is_valid_username(username):
    special_ch_allowed = ("_", ".", "!", "#", "$", "%", "?")
    if len(username) > 8 or username == "":
        return False
    for character in username:
        if not (character.isdigit() or character.islower() or character in special_ch_allowed):
            return False
    return True


username_list = ['abcdefgh', 'abcdefghi', 'ab$cd', 'ab_cd',
                 'ab-cd', 'ab:cd', '', 'ab cd', 'abcDef', 'abc8ef']
for username in username_list:
    print("The username '" + username + "' is valid : " +
          str(is_valid_username(username)))
