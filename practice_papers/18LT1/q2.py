def represent_numbers(start, end):
    dash_str = ""
    if start < end:
        for i in range(start, end + 1):
            dash_str += abs(i) * "-"
            if i != end:
                dash_str += "#"
    if start > end:
        return ""
    return dash_str


print(represent_numbers(3, 1))
