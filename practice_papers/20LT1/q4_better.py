# Name:
# Email ID:

def trace_contacts_2(patient, history, m, n):
    infected = [(patient, -m)]
    days_to_infective = n - m
    checked = []
    for person in infected:
        name, infectious_date = person
        if name in checked:
            continue
        for interaction in history:
            pax1, pax2, date = interaction
            if date < infectious_date:
                continue
            if pax1 == name:
                infected.append((pax2, date + days_to_infective))
            if pax2 == name:
                infected.append((pax1, date + days_to_infective))
        checked.append(name)
    checked.remove(patient)
    return list(set(checked))
