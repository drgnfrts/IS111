# Name:
# Email ID:
def get_daily_spending(filename, start_day, end_day, month, year):
    r_dict = {}
    with open(filename, "r") as inputfile:
        for line in inputfile:
            stripped = line.strip("\n").split("|")
            lineday, linemonth, lineyear = stripped[0].split("/")
            k = str(f"{int(lineday)}/{int(linemonth)}/{lineyear}")
            print(k, type(k))
            if k in r_dict:
                r_dict[k] += int(stripped[1])
            else:
                r_dict[k] = int(stripped[1])
    date_list = []
    for i in range(start_day, end_day + 1):
        date_list.append(str(f"{i}/{month}/{year}"))
    r_list = []
    for each_date in date_list:
        if each_date in r_dict:
            r_list.append(r_dict[each_date])
        else:
            r_list.append(0)
    return r_list


# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    n = 0

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 3, 5, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 3, 5, 10, 2020)
    print("Expected : [13500, 31520, 100]")
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 6, 7, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 6, 7, 10, 2020)
    print("Expected : [0, 0]")
    print(f"Actual   : {result}")
    print()

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 2, 6, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 2, 6, 10, 2020)
    print("Expected : [0, 13500, 31520, 100, 0]")
    print(f"Actual   : {result}")
    print()

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('spending_file.txt', 1, 2, 1, 2020)")
    result = get_daily_spending('spending_file.txt', 1, 2, 1, 2020)
    print("Expected : [1200, 0]")
    print(f"Actual   : {result}")
    print()
    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('spending_file.txt', 1, 10, 2, 2020)")
    result = get_daily_spending('spending_file.txt', 1, 10, 2, 2020)
    print("Expected : [50, 0, 0, 0, 0, 0, 0, 0, 0, 80]")
    print(f"Actual   : {result}")
    print()
    
    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('empty.txt', 2, 6, 10, 2020)")
    result = get_daily_spending('empty.txt', 2, 6, 10, 2020)
    print("Expected : [0, 0, 0, 0, 0]")
    print(f"Actual   : {result}")
    print()

    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('empty.txt', 2, 2, 11, 2020)")
    result = get_daily_spending('empty.txt', 2, 2, 11, 2020)
    print("Expected : [0]")
    print(f"Actual   : {result}")
    print()