def print_dancing_string(sentence, start):
    top = ["|"]
    middle = ["|"]
    bottom = ["|"]
    if sentence == "":
        top.append("|")
        middle.append("|")
        bottom.append("|")
    elif start == "T":
        new_sent = " " + sentence
        for i in range(len(new_sent)):
            if i == 0:
                continue
            elif i % 4 == 1:
                top.append(new_sent[i])
                middle.append(" ")
                bottom.append(" ")
            elif i % 4 == 2 or i % 4 == 0:
                top.append(" ")
                middle.append(new_sent[i])
                bottom.append(" ")
            elif i % 4 == 3:
                top.append(" ")
                middle.append(" ")
                bottom.append(new_sent[i])
        top.append("|")
        middle.append("|")
        bottom.append("|")
    elif start == "M":
        new_sent = " " + sentence
        for i in range(len(new_sent)):
            if i == 0:
                continue
            elif i % 4 == 2:
                top.append(new_sent[i])
                middle.append(" ")
                bottom.append(" ")
            elif i % 4 == 1 or i % 4 == 3:
                top.append(" ")
                middle.append(new_sent[i])
                bottom.append(" ")
            elif i % 4 == 0:
                top.append(" ")
                middle.append(" ")
                bottom.append(new_sent[i])
        top.append("|")
        middle.append("|")
        bottom.append("|")
    elif start == "B":
        new_sent = " " + sentence
        for i in range(len(new_sent)):
            if i == 0:
                continue
            elif i % 4 == 3:
                top.append(new_sent[i])
                middle.append(" ")
                bottom.append(" ")
            elif i % 4 == 2 or i % 4 == 0:
                top.append(" ")
                middle.append(new_sent[i])
                bottom.append(" ")
            elif i % 4 == 1:
                top.append(" ")
                middle.append(" ")
                bottom.append(new_sent[i])
        top.append("|")
        middle.append("|")
        bottom.append("|")
    print("".join(top))
    print("".join(middle))
    print("".join(bottom))


print_dancing_string('abcdefghi', 'T')
print_dancing_string('abcdefghi', 'M')
print_dancing_string('abcdefghi', 'B')
print_dancing_string('', 'T')
