# Name:
# Email ID:

import q5a
import itertools


def get_seating(person_list, n, m):
    all_permutations = list(itertools.permutations(person_list))
    for permutations in all_permutations:
        if len(q5a.get_persons(permutations, n)) >= m:
            return permutations
    return []
