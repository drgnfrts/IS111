def print_diamond(n):
    s = 2 * n - 1
    for i in range(2 * (n - 1) + 1):
        if i == 0 or i == 2 * (n - 1):
            print((n - 1) * " " + "*" + (n - 1) * " ")
        else:
            middle = s - 2 - 2 * abs(n - 1 - i)
            print(abs(n - 1 - i) * " " + "*" +
                  (" " * middle) + "*" + abs(n - 1 - i) * " ")


print_diamond(4)
