def process_numbers(input_filename, output_filename):
    groupcount = 0
    max_avg = -float("inf")
    # use minus infinity here instead of 0 because some groups have negative numbers
    with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
        for line in input_file:
            stripped = line.strip("\n").split("#")
            send = []
            groupcount += len(stripped)
            for group in stripped:
                newgroup = group.split()
                grp_total = 0
                for num in newgroup:
                    grp_total += float(num)
                grp_avg = grp_total / len(newgroup)
                max_avg = max(grp_avg, max_avg)
                send.append(str(grp_avg))
            line = str(len(stripped)) + ": " + "#".join(send) + "\n"
            output_file.write(line)
        output_file.write(
            f"Total number of groups: {groupcount}\nMaximum average: {max_avg}")


# do not modify this test code
if __name__ == "__main__":
    print("Test Case for Q3")
    print()

    process_numbers("numbers.txt", "output.txt")
    print("Please check whether the file 'output.txt' generated is the same as the file 'expected-output.txt' that we've provided.")
