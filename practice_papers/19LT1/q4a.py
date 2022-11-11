# Name:
# Email ID:

def check_seating_arrangement(arrangement, must_list, cannot_list):
    # Modify the code below.
    for i in range(len(arrangement)):
        if i == 0:
            for j in range(len(must_list)):
                pax_a, pax_b = must_list[j]
                if arrangement[i] == pax_a:
                    if arrangement[len(arrangement) - 1] == pax_b or arrangement[1] == pax_b:
                        pass
                    else:
                        return False
                elif arrangement[i] == pax_b:
                    if arrangement[len(arrangement) - 1] == pax_a or arrangement[1] == pax_a:
                        pass
                    else:
                        return False
            for k in range(len(cannot_list)):
                pax_a, pax_b = cannot_list[k]
                if arrangement[i] == pax_a:
                    if arrangement[len(arrangement) - 1] == pax_b or arrangement[1] == pax_b:
                        return False
                    else:
                        pass
                elif arrangement[i] == pax_b:
                    if arrangement[len(arrangement) - 1] == pax_a or arrangement[1] == pax_a:
                        return False
                    else:
                        pass
        elif i == len(arrangement) - 1:
            for j in range(len(must_list)):
                pax_a, pax_b = must_list[j]
                if arrangement[i] == pax_a:
                    if arrangement[i - 1] == pax_b or arrangement[0] == pax_b:
                        pass
                    else:
                        return False
                elif arrangement[i] == pax_b:
                    if arrangement[i - 1] == pax_a or arrangement[0] == pax_a:
                        pass
                    else:
                        return False
            for k in range(len(cannot_list)):
                pax_a, pax_b = cannot_list[k]
                if arrangement[i] == pax_a:
                    if arrangement[i - 1] == pax_b or arrangement[0] == pax_b:
                        return False
                    else:
                        pass
                elif arrangement[i] == pax_b:
                    if arrangement[i - 1] == pax_a or arrangement[0] == pax_a:
                        return False
                    else:
                        pass
        else:
            for j in range(len(must_list)):
                pax_a, pax_b = must_list[j]
                if arrangement[i] == pax_a:
                    if arrangement[i - 1] == pax_b or arrangement[i + 1] == pax_b:
                        pass
                    else:
                        return False
                elif arrangement[i] == pax_b:
                    if arrangement[i - 1] == pax_a or arrangement[i + 1] == pax_a:
                        pass
                    else:
                        return False
            for k in range(len(cannot_list)):
                pax_a, pax_b = cannot_list[k]
                if arrangement[i] == pax_a:
                    if arrangement[i - 1] == pax_b or arrangement[i + 1] == pax_b:
                        return False
                    else:
                        pass
                elif arrangement[i] == pax_b:
                    if arrangement[i - 1] == pax_a or arrangement[i + 1] == pax_a:
                        return False
                    else:
                        pass
    return True
