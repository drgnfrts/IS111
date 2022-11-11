stu_dict = {}
ok = "Y"
with open("students.txt", "r") as input_file:
    for line in input_file:
        stripped = line.strip("\n").split("\t")
        if stripped[3] == "M":
            stripped[3] = "male"
        else:
            stripped[3] = "female"
        stu_dict[stripped[1]
                 ] = f"{stripped[0]}, {stripped[3]}, born on {stripped[2]}."
while ok == "Y":
    searchval = input("Please enter an email ID: ")
    if searchval in stu_dict:
        print(f"This student is {stu_dict[searchval]}")
    else:
        print("This is not a valid student ID")
    print()
    ok = input("Do you want to continue [Y|N] :")
    print()
print("Good-bye!")
