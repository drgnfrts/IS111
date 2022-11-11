mydict = {}
with open("seating_plan.txt", "r") as input_file:
    for line in input_file:
        stripped = line.strip("\n").split(",")
        newkey = stripped[0] + stripped[1]
        stripped[1] = int(stripped[1])
        mydict[newkey] = stripped

letter = input("Enter a letter (from A to E) :")
seatnum = input("Enter a seat number (from 1 to 25) :")
int_seatnum = int(seatnum)
searchval = letter + seatnum
left = letter + str(int_seatnum - 1)
right = letter + str(int_seatnum + 1)
print()
if searchval in mydict:
    print(f"The person seated at seat {searchval} is {mydict[searchval][2]}")
else:
    print("Seat not taken")
if left in mydict:
    print(
        f"The person seated on the left side of that person is {mydict[left][2]}")
else:
    print("Seat not taken on the left side")
if right in mydict:
    print(
        f"The person seated on the left side of that person is {mydict[right][2]}")
else:
    print("Seat not taken on the right side")
