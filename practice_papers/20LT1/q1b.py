# Name:
# Email ID:

def is_compatible(patient_group, donor_group):
    # Replace the code below with your implementation.
    compatiable_types = (("A", ("A", "AB")), ("B", ("B", "AB")), ("AB", ("AB")), ("O", ("O", "AB", "A", "AB")))
    for i in range(len(compatiable_types)):
        if patient_group == compatiable_types[i][0]:
            for j in range(len(compatiable_types[i][1])):
                if donor_group in compatiable_types[i][1][j]:
                    return True
    return False