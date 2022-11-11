# Name:
# Email ID:
import string


def extract_names_2(name_list):
    r_list = []
    for name in name_list:
        valid = False
        holding = ""
        for ch in name:
            if ch.isalpha() or ch == " ":
                holding += ch
        for ch in holding:
            if ch in string.ascii_letters:
                valid = True
                break
        if valid:
            r_list.append(holding)
    return r_list