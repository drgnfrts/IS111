user_mins = int(input("What's the minimum number calls (in mins) you need? "))
user_sms = int(input("What's the minimum number SMS you need? "))
user_data = float(input("What's the minimum amount of data you need? "))


def find_plan(mins, sms, data):
    plans = ((80, 300, 0.1), (200, 500, 2), (300, 1000, 3),
             (400, 1500, 4), (800, 2000, 10))
    if mins > 800 or sms > 2000 or data > 10:
        return 0
    for i in range(len(plans)):
        if mins < plans[i][0]:
            plan_num = i
            break
    for j in range(plan_num, len(plans)):
        if sms < plans[j][1]:
            plan_num = j
            break
    for k in range(plan_num, len(plans)):
        if data < plans[k][2]:
            plan_num = k
            break
    return plan_num + 1


reco_plan = find_plan(user_mins, user_sms, user_data)

if reco_plan != 0:
    print(f"We recommend Combo {reco_plan}")
else:
    print("Sorry! We don't have any plan that satisfies your requirements!")
