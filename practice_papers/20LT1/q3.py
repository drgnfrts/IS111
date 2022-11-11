# Name:
# Email ID:

def check_math(list_of_equations):
    # Replace the code below with your implementation.
    operators = ["+", "-", "*", "//", "%"]
    if list_of_equations == []:
        return True
    for equation in list_of_equations:
        result = int()
        equation_temp_list = equation.split("=")
        right_hand_side = int(equation_temp_list[1])
        for operator in operators:
            if operator in equation_temp_list[0]:
                sign = operator
                left_hand_side = equation_temp_list[0].split(operator)
        int1 = int(left_hand_side[0])
        int2 = int(left_hand_side[1])
        if sign == "+":
            result = int1 + int2
        elif sign == "-":
            result = int1 - int2
        elif sign == "*":
            result = int1 * int2
        elif sign == "//":
            result = int1 // int2
        elif sign == "%":
            result = int1 % int2

        if result != right_hand_side:
            return False
    return True
