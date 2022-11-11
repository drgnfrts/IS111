def print_diamond_using_str(text):
    s = int(len(text) / 4 + len(text) / 4 + 1)
    n = int(len(text) / 4 + 1)
    #n = int(((len(text) - 4) / 4) + 2)
    for i in range(s):
        if i == 0 or i == s - 1:
            print((n - 1) * " " + text[i] + (n - 1) * " ")
        else:
            middle = s - 2 - 2 * abs(n - 1 - i)
            print(abs(n - 1 - i) * " " +
                  text[i] + middle * " " + text[-i] + abs(n - 1 - i) * " ")


print_diamond_using_str("123456789012")
