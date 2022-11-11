# Name:
# Email ID:
from q4b import get_relation_through_link


def get_relation(family_dict, p1, p2):
    # Modify the code below.
    link_dict = {}
    added = []
    added2 = []
    for ekey in family_dict.keys():
        k0, k1 = ekey
        if k0 not in link_dict and k1 not in added:
            link_dict[k0] = k1
            added += [k0, k1]
    for ekey2 in link_dict.keys():
        if ekey2 not in added2:
            added2 += [ekey2, link_dict[ekey2]]
        else:
            added2.append(link_dict[ekey2])
    start = added2.index(p1)
    end = added2.index(p2)
    if start < end:
        link = added2[start:end + 1]
    else:
        link = added2[start - len(added2):end-1 - len(added2):-1]
    return get_relation_through_link(family_dict, link)
