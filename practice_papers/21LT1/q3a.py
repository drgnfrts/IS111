# Name:
# Email ID:

# CARELESS MISTAKE: MAKE SURE U ARE REFERENCING CORRECTLY
# EARLIER, LINE17 "religious_groups" was mistyped as "racial_groups"

def check_diversity(team):
    # Replace the code below with your implementation.
    male = 0
    racial_groups = []
    religious_groups = []
    for i in range(len(team)):
        if team[i][1] == "M":
            male += 1
        if team[i][2] not in racial_groups:
            racial_groups.append(team[i][2])
        if team[i][3] not in religious_groups and team[i][3] != "Freethinker":
            religious_groups.append(team[i][3])
    if male < 2 or male > 3:
        return False
    if len(racial_groups) < 3:
        return False
    if len(religious_groups) < 2:
        return False
    return True

# def check_diversity(team):
#     # Replace the code below with your implementation.
#     male = 0
#     racial_groups = []
#     religious_groups = []
#     for people in team:
#         if people[1] == "M":
#             male += 1
#         if people[2] not in racial_groups:
#             racial_groups.append(people[2])
#         if people[3] not in religious_groups and people[3] != "Freethinker":
#             religious_groups.append(people[3])
#     if male < 2 or male > 3:
#         return False
#     if len(racial_groups) < 3:
#         return False
#     if len(religious_groups) < 2:
#         return False
#     return True


# PSEUDOCODE FOR 2021-Q3B:
'''
step 1: create 2 new lists in memory, team a & team b. so team1 & team2 should not be touched.
step 2a: u want to iterate thru team a & team b. a[0] b[0], a[0] b[1], and swap the indexes. 
step 2b: but if you swap the indexes you will mess up team a & team b and cannot iterate properly
step 2c: so u want to reset back team a & team b every time u finish checking
'''
