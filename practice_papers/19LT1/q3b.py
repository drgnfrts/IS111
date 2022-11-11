# Name:
# Email ID:

import q3a


def calculate_entrance_fees_2(m, n):

    # These variables are defined for you to use.
    ADULT_TICKET = 75
    CHILD_TICKET = 50

    PACKAGE_A = 140
    PACKAGE_B = 110
    PACKAGE_C = 200

    subtotal_rest = 0
    subtotal_b_c = q3a.calculate_entrance_fees_1(min(m, n))
    if m > n:
        a = m - n
        subtotal_rest = (a // 2) * PACKAGE_A + (a % 2) * ADULT_TICKET
    if m < n:
        c = n - m
        subtotal_rest = c * CHILD_TICKET
    # Modify the code below.
    return subtotal_rest + subtotal_b_c
