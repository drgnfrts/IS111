# Name:
# Email ID:

import itertools
import q4a


def get_seating_arrangement(female_list, male_list, must_list, cannot_list):
    male_permutations = list(itertools.permutations(male_list))
    female_permutations = list(itertools.permutations(female_list))
    for m_perm in male_permutations:
        for f_perm in female_permutations:
            proposed_seating = []
            for i in range(len(m_perm)):
                proposed_seating.append(m_perm[i])
                proposed_seating.append(f_perm[i])
            if q4a.check_seating_arrangement(proposed_seating, must_list, cannot_list):
                return proposed_seating
    return None
