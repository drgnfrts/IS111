# Name:
# Email ID:

def opposing_gender(user_gender, test_input):
    if user_gender == "M" and test_input == "F":
        return True
    elif user_gender == "F" and test_input == "M":
        return True
    return False


def get_persons(person_list, n):
    r_list = []
    for i in range(len(person_list)):
        name, gender = person_list[i]
        left = i
        right = i
        gender_count = 0
        check = 0
        checked = []
        while True:
            leftadd = False
            rightadd = False
            left = left - 1
            right = right + 1
            if right > len(person_list) - 1:
                right -= 5
            if opposing_gender(gender, person_list[left][1]) and person_list[left] not in checked:
                gender_count += 1
                checked.append(person_list[left])
                leftadd = True
            if opposing_gender(gender, person_list[right][1]) and person_list[right] not in checked:
                gender_count += 1
                checked.append(person_list[right])
                rightadd = True
            check += 2
            if check == 2 and (not leftadd or not rightadd):
                break
            if (not leftadd and not rightadd) or check >= len(person_list):
                break
        if gender_count >= n:
            r_list.append(person_list[i])
    return r_list