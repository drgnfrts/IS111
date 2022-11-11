# Q1a Substitution Cipher
# write your code below
def encrypt(my_dict, msg):
    r_msg = ""
    for ch in msg:
        if ch in my_dict:
            r_msg += my_dict[ch]
        elif ch == " ":
            r_msg += " "
    return r_msg
