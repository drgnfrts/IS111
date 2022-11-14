# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

def time_to_minutes(time):
    if "AM" in time:
        h, m = time.strip("AM").strip().split(":")
        return int(h) * 60 + int(m)
    if "PM" in time:
        h, m = time.strip("PM").strip().split(":")
        if int(h) == 12:
            return int(h) * 60 + int(m)
        return (int(h) + 12) * 60 + int(m)


def get_flight_durations(filename):
    # Replace the code below with your implementation.
    hold_dict = {}
    r_dict = {}
    with open(filename, "r") as input_file:
        for line in input_file:
            stripped = line.strip("\n").split(")")
            scheduledtime_code_place, airline_aircraft, status_actualtime = stripped
            stcp = scheduledtime_code_place.split()
            st = time_to_minutes(stcp[0] + stcp[1])
            code = stcp[2]
            for i in range(3):
                stcp.pop(0)
            stcp.pop(-1)
            location = " ".join(stcp)
            aa = airline_aircraft.split()
            for j in range(2):
                aa.pop(-1)
            airline = " ".join(aa)
            sat = status_actualtime.split()
            at = time_to_minutes(sat[-2] + sat[-1])
            status = sat[-3]
            if code not in hold_dict:
                hold_dict[code] = {}
            if status not in hold_dict[code]:
                hold_dict[code][status] = airline, location, st, at
    print(hold_dict)
    for code, info in hold_dict.items():
        if len(info) == 2:
            airline, origin, origin_st, origin_at = hold_dict[code]["Departed"]
            airline, destination, dest_st, dest_at = hold_dict[code]["Landed"]
            sft = dest_st - origin_st
            aft = dest_at - origin_at
            if airline not in r_dict:
                r_dict[airline] = [(code, destination, origin, sft, aft)]
            else:
                r_dict[airline].append((code, destination, origin, sft, aft))
    return r_dict
