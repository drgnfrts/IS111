def create_num_file(filename, n):
    nums = ""
    for i in range(n + 1):
        if i % 2 == 0:
            nums += str(i) + "\n"
    with open(filename, "w") as new_file:
        new_file.write(nums)


create_num_file("q1b-output.txt", 10)
