# Name:
# Email ID:
def string_to_polylist(indiv_x, poly_dict, highest):
    if "x" not in indiv_x:
        power = 0
        num = int(indiv_x)
    elif "x^" in indiv_x:
        power = int(indiv_x[-1])
        num = int(indiv_x[0:indiv_x.rfind("x^")])
    else:
        power = 1
        num = int(indiv_x[0:indiv_x.rfind("x")])
    if power in poly_dict:
        poly_dict[power] += num
    else:
        poly_dict[power] = num
    if power > highest:
        return power
    return highest


def get_polynomial(poly_str):
    r_list = []
    holding_dict = {}
    hold = ""
    highest = 0
    i = 0
    while i < len(poly_str):
        if (poly_str[i] == " " or poly_str[i] == "+") and (hold == "" or hold == "-"):
            i += 1
            continue
        elif (poly_str[i] == " " or poly_str[i] == "+") and hold != "":
            highest = string_to_polylist(hold, holding_dict, highest)
            hold = ""
        else:
            hold += poly_str[i]
            if i == len(poly_str) - 1:
                highest = string_to_polylist(hold, holding_dict, highest)
        i += 1
    for j in range(highest, -1, -1):
        try:
            r_list.append(holding_dict[j])
        except:
            r_list.append(0)
    while r_list[0] == 0:
        r_list.pop(0)
    return r_list


# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)

    poly_str = '2x - 2x^2 + 3x - 1 + 6x^3'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print("Expected : [6, -2, 5, -1]")
    result = get_polynomial(poly_str)
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

    tc_num += 1
    print('-' * 40)

    poly_str = '  4x -2x^2 +   3x^5 -   6x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [3, 0, 0, -8, 4, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)

    poly_str = '3x^2 - 2x - 3x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [-2, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()
