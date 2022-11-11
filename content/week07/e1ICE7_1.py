def encode_message(text):
    encoded_string = ""
    if text == "":
        return encoded_string
    holding_list = []
    for ch in text:
        if ch not in holding_list:
            try:
                encoded_string += holding_list[0] + \
                    str(len(holding_list)) + " "
                holding_list = []
            except:
                pass
        holding_list.append(ch)
    encoded_string += holding_list[0] + str(len(holding_list))
    return encoded_string


x = [4, 39, [35, 12, [45], 32], 4, [35, [4, [6]]]]
print(str(x))
