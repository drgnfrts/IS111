# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def construct_string(orig_str, len_list, cnct_list):
    # Replace the code below with your implementation.
    if orig_str == "":
        return ""
    combined_string = ""
    for i in range(len(len_list)):
        combined_string += orig_str[:len_list[i]]
        orig_str = orig_str[len_list[i]:]
        if i != len(len_list) - 1:
            combined_string += cnct_list[i]
    return combined_string
