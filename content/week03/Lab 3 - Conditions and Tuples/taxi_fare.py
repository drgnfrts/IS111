def base_fare_calculation():
    flagdown_charge = float(input("What's the flag-down fare: $"))
    mid_dist_charge = float(
        input("What's the rate per 400 metres within 9.8km? $"))
    long_dist_charge = float(
        input("What's the rate per 350 metres beyond 9.8km? $"))
    distance = float(input("What's the distance traveled (in meters)? "))
    if distance <= 1000:
        total_base_fare = flagdown_charge
    elif 1000 < distance <= 9800:
        if (distance - 1000) % 400 != 0:
            mid_dist_fare = ((distance - 1000) // 400 + 1) * mid_dist_charge
        else:
            mid_dist_fare = (distance - 1000) // 400 * mid_dist_charge
        total_base_fare = mid_dist_fare + flagdown_charge
    elif distance > 9800:
        mid_dist_fare = (9800 - 1000) // 400 * mid_dist_charge
        if (distance - 9800) % 350 != 0:
            long_dist_fare = ((distance - 9800) // 350 + 1) * long_dist_charge
        else:
            long_dist_fare = (distance - 9800) // 350 * long_dist_charge
        total_base_fare = long_dist_fare + mid_dist_fare + flagdown_charge
    return total_base_fare


def surcharge_calculation(base_fare):
    if input("Is the ride during a peak period? [yes/no] ") == "yes":
        total_fare = base_fare * 1.25
    elif input("Is the ride between midnight and 6am? [yes/no] ") == "yes":
        total_fare = base_fare * 1.50
    else:
        total_fare = base_fare
    if input("Is there any location surcharge? [yes/no] ") == "yes":
        total_fare += float(input("What's the amount of location surcharge? "))
    return total_fare

print(round(surcharge_calculation(base_fare_calculation()), 2))
