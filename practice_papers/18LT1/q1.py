def get_color(color):
    if color == "R" or color == "r":
        return "Red"
    elif color == "G" or color == "g":
        return "Green"
    elif color == "B" or color == "b":
        return "Blue"
    else:
        return "Invalid"


print(get_color("g"), get_color("b sky"), get_color("R"))
