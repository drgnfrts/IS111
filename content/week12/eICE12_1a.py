valid_days = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11], 28: [2]}
task_list = {}
earliest_month = 0

start = input("Do you want to enter a task? [Y|N]: ")
while start == "Y":
    task = input("Enter task description: ")
    while True:
        month = input("Enter the month it is due: ")
        try:
            month = int(month)
            if 1 <= month <= 12:
                if earliest_month == 0:
                    earliest_month = month
                else:
                    earliest_month = min(earliest_month, month)
                break
        except:
            print("Sorry, invalid month!")
            print()
    while True:
        date = input("Enter the date it is due: ")
        for mykey, myvalue in valid_days.items():
            if month in myvalue:
                max_date = mykey
        try:
            date = int(date)
            if 1 <= date <= max_date:
                break
        except:
            print("Sorry, invalid date!")
            print()
    print()
    duedate = f"{date}/{month}"
    if duedate in task_list:
        task_list[duedate].append(task)
    else:
        task_list[duedate] = [task]
    print(f"{task} due on {duedate} has been recorded")
    print()
    start = input("Do you want to continue? [Y|N]: ")
    print()
print("Here are the tasks you've entered:")
print()
for i in range(earliest_month, 13):
    for j in range(1, 32):
        anything_due = f"{j}/{i}"
        if anything_due in task_list:
            print(f"Due on {anything_due}:")
            for eachtask in task_list[anything_due]:
                print("\t" + eachtask)
