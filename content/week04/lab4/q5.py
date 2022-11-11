def pad_message(msg, width):
    if len(msg) < width:
        return (width - len(msg)) * " " + msg
        # OR return msg.rjust(width)
    else:
        return msg[:width]


print(pad_message("IS111 Lab 5", 20))
print(pad_message("IS111 Lab 5", 8))
print(pad_message("hello", 20))
print(pad_message("python programming", 20))
print(pad_message("Hello World! I enjoy programming in Python.", 20))
