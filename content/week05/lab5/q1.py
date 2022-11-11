# Q1 Initials
# Write your code below:
##############################
num_people = int(input("How many people will attend the meeting? "))
participant_list = []
participant_initials = []

for i in range(num_people):
    participant_list.append(input(f"Participant {i + 1}: "))

for names in participant_list:
    initial_list = ""
    indiv_name = names.split()
    for subname in indiv_name:
        initial_list += subname[0]
    participant_initials.append(initial_list)

print("The initials of the participants are as follows:")
for initials in participant_initials:
    print(initials)
