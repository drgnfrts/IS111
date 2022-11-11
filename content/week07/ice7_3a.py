def print_triangle(ch, num_rows):
    for i in range(num_rows):
        whitespace_row = (num_rows - i) * " "
        characters = (i * 2 + 1) * ch
        print(whitespace_row + characters + whitespace_row)


print_triangle("*", 3)
print_triangle("#", 5)
