# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def shift_string(orig_str):
    # Replace the code below with your implementation.
    if orig_str == "":
        return []
    shifted_list = [orig_str]
    for i in range(len(orig_str) - 1):
        orig_str = orig_str[1:] + orig_str[0]
        shifted_list.append(orig_str)
    return shifted_list
