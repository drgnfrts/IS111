# Name:
# Email ID:

import q3a


def clear_and_replace(team1, team2):
    local_team_a = []
    local_team_b = []
    for participant in team1:
        local_team_a.append(participant)
    for participant in team2:
        local_team_b.append(participant)
    return local_team_a, local_team_b


def swap_members(team1, team2):
    # Replace the code below with your implementation.
    team_a, team_b = clear_and_replace(team1, team2)
    for i in range(len(team_a)):
        for j in range(len(team_b)):
            takeout_a = team_a[i]
            takeout_b = team_b[j]
            team_a.pop(i)
            team_b.pop(j)
            team_a.insert(i, takeout_b)
            team_b.insert(j, takeout_a)
            if q3a.check_diversity(team_a) == True and q3a.check_diversity(team_b) == True:
                return (takeout_a[0], takeout_b[0])
            team_a, team_b = clear_and_replace(team1, team2)
    return None
