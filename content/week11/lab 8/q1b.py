# Q1b Substitution Cipher
# write your code below
def decrypt(my_dict, encrypted_msg):
    r_msg = ""
    for ch in encrypted_msg:
        if ch == " ":
            r_msg += " "
        else:
            for mykey, myvalue in my_dict.items():
                if ch == myvalue:
                    r_msg += mykey
    return r_msg
