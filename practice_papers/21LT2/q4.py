# Name:
# Email ID:

def ampm_converter(ampm_time):
    if ampm_time == "12AM":
        return 0
    elif ampm_time == "12PM":
        return 12
    elif "AM" in ampm_time:
        return int(ampm_time.strip("AM"))
    elif "PM" in ampm_time:
        return int(ampm_time.strip("PM")) + 12


def read_schedule(filename):
    hold_dict = {}
    r_dict = {}
    with open(filename, "r") as inputfile:
        for line in inputfile:
            stripped = line.strip("\n").split("|")
            day, start12, end12, usernames = stripped
            start24 = ampm_converter(start12)
            end24 = ampm_converter(end12)
            list_of_usernames = list(set(usernames.split()))
            if day not in hold_dict:
                hold_dict[day] = {}
            for each_name in list_of_usernames:
                if each_name not in hold_dict[day]:
                    hold_dict[day][each_name] = (start24, end24)
                else:
                    existing_start, existing_end = hold_dict[day][each_name]
                    if end24 - start24 < existing_end - existing_start:
                        hold_dict[day][each_name] = (start24, end24)
                    elif end24 - start24 == existing_end - existing_start and end24 > existing_end:
                        hold_dict[day][each_name] = (start24, end24)
        for each_day in hold_dict.keys():
            r_dict[each_day] = []
            for final_names, timings_tuple in hold_dict[each_day].items():
                final_start, final_end = timings_tuple
                r_dict[each_day].append((final_start, final_end, final_names))
    return r_dict