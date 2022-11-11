def print_frame(ch, num_rows, num_cols):
    print(ch * num_cols)
    for i in range(1, num_rows - 1):
        print(ch + ((num_cols - 2) * " ") + ch)
    print(ch * num_cols)


print_frame("#", 5, 6)
