# Name:
# Email ID:


def trace_sick_people(name, infectious_start_date, history, checked, no_days_to_infective):
    sick_people_details = []
    sick_people = []
    for i in range(len(history)):
        pax1, pax2, date = history[i]
        if name == pax1 and date >= infectious_start_date and pax1 not in sick_people and pax2 not in sick_people and pax2 not in checked:
            sick_people_details.append((pax2, date + no_days_to_infective))
            sick_people.append(pax2)
        elif name == pax2 and date >= infectious_start_date and pax1 not in sick_people and pax2 not in sick_people and pax1 not in checked:
            sick_people_details.append((pax1, date + no_days_to_infective))
            sick_people.append(pax1)
        # if name == history[i][0] and history[i][2] >= infectious_start_date and name not in sick_people and history[i][1] not in checked and history[i][1] not in sick_people:
        #     sick_people_details.append(
        #         (history[i][1], history[i][2] + no_days_to_infective))
        #     sick_people.append(history[i][1])
        # elif name == history[i][1] and history[i][2] >= infectious_start_date and name not in sick_people and history[i][0] not in checked and history[i][0] not in sick_people:
        #     sick_people_details.append(
        #         (history[i][0], history[i][2] + no_days_to_infective))
        #     sick_people.append(history[i][0])
    return sick_people_details


def all_checked(unchecked):
    if unchecked == []:
        return True
    return False


def trace_contacts_2(patient, history, m, n):
    unchecked_list = [(patient, -m)]
    days_to_infective = n - m
    checked = []
    while not all_checked(unchecked_list):
        for contact in unchecked_list:
            trace_name, trace_start = contact
            if trace_sick_people(trace_name, trace_start, history, checked, days_to_infective) == []:
                checked.append(trace_name)
                unchecked_list.remove(contact)
            else:
                unchecked_list += trace_sick_people(
                    trace_name, trace_start, history, checked, days_to_infective)
                checked.append(trace_name)
                unchecked_list.remove(contact)
    checked.remove(patient)
    return checked
