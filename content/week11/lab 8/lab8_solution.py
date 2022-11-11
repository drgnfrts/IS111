## Q1a Substitution Cipher
# SOLUTION

def encrypt(cipher_dict, message):
    encrypted_message = ''
    for ch in message:
        if ch != ' ':
            encrypted_ch = cipher_dict[ch]
        else:
            encrypted_ch = ch
        encrypted_message += encrypted_ch
        
    return encrypted_message

## Q1b Substitution Cipher
# SOLUTION 1
def encrypt(cipher_dict, message):
    encrypted_message = ''
    for ch in message:
        if ch != ' ':
            encrypted_ch = cipher_dict[ch]
        else:
            encrypted_ch = ch
        encrypted_message += encrypted_ch
        
    return encrypted_message

# SOLUTION 2
import q1a
def decrypt(my_dict,encrypted_msg):
    decrypt_dict={}

    for k,v in my_dict.items():
        decrypt_dict[v]=k
    
    return q1a.encrypt(decrypt_dict,encrypted_msg)

## Q2 Prime Numbers
# SOLUTION

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def create_prime_dict(num_list):
    my_dict = {}
    for num in num_list:
        if is_prime(num):
            my_dict[num] = True
        else:
            my_dict[num] = False
    return my_dict

## Q3a Facilities
# SOLUTION
facility_dict = {}
with open('facilities.txt', 'r') as my_file:
    for line in my_file:
        line = line.rstrip('\n')
        row_details = line.split('\t')
        school = row_details[0]
        room_no = row_details[1]
        capacity = int(row_details[2])
        has_projector = row_details[3]
        key = (school, room_no)
        value = (capacity, has_projector)
        facility_dict[key] = value       

ans = input('\nDo you want to search for a facility? [Y|N] :')
while ans == 'Y':
    school = input('Enter the school [LKCSB|SOE|SOL|SOA|SIS] :')
    room_no = input('Enter the room number :')
    key = (school, room_no)
    value = facility_dict[key]
    capacity = value[0]
    has_projector = value[1]
    if has_projector == 'yes':
        projector_info = 'has a projector'
    else:
        projector_info = 'does not have a projector'
    print(school, room_no, 'has a capacity of', capacity,'and', projector_info + '.')
    
    ans = input('\nDo you want to search for a facility? [Y|N] :')
    
print('Thanks for using our system!')

## Q3b 
# SOLUTION

def display_school_facilities(facility_dict, given_school):
    print('\tRoom #\tCap\tProjector?')
    print('\t------\t---\t----------')

    facilities = facility_dict[given_school]
    for facility_info in facilities:
        room_no = facility_info[0]
        capacity = facility_info[1]
        has_projector = facility_info[2]

        print('\t' + room_no + '\t' + str(capacity) + '\t' + has_projector)

# read file into a dictionary
facility_dict = {}
with open('facilities.txt', 'r') as my_file:
    for line in my_file:
        line = line.rstrip('\n')
        row_details = line.split('\t')
        school = row_details[0]
        room_no = row_details[1]
        capacity = int(row_details[2])
        has_projector = row_details[3]
        
        facility_info = (room_no, capacity, has_projector)
        
        if school in facility_dict:
            facility_list = facility_dict[school]
            facility_list.append(facility_info)
        else:
            facility_dict[school] = [facility_info]    

ans = input('\nDo you want to search for the facilities within a school? ? [Y|N] :')
while ans == 'Y':
    school = input('Enter the school [LKCSB|SOE|SOL|SOA|SIS] :')
    print('The following facilities are in ' + school + ' :')
    display_school_facilities(facility_dict, school)
    
    ans = input('\nDo you want to search for the facilities within a school? ? [Y|N] :')
    
print('Good-bye!')

## Q3c 
# SOLUTION

def display_school_facilities_by_capacity(facility_dict, given_school, min_capacity):
    print('\tRoom #\tCap\tProjector?')
    print('\t------\t---\t----------')

    facilities = facility_dict[given_school]
    for facility_info in facilities:
        room_no = facility_info[0]
        capacity = facility_info[1]
        has_projector = facility_info[2]
        if capacity >= min_capacity:
            print('\t' + room_no + '\t' + str(capacity) + '\t' + has_projector)

# read file into a dictionary
facility_dict = {}
with open('facilities.txt', 'r') as my_file:
    for line in my_file:
        line = line.rstrip('\n')
        row_details = line.split('\t')
        school = row_details[0]
        room_no = row_details[1]
        capacity = int(row_details[2])
        has_projector = row_details[3]
        
        facility_info = (room_no, capacity, has_projector)
        
        if school in facility_dict:
            facility_list = facility_dict[school]
            facility_list.append(facility_info)
        else:
            facility_dict[school] = [facility_info]       

ans = input('\nDo you want to search for the facilities within a school? [Y|N]:')
while ans == 'Y':
    school = input('Enter the school [LKCSB|SOE|SOL|SOA|SIS] :')
    min_capacity = int(input('Enter the minimum capacity you need :'))
    print('The following facilities with a capacity of ' + str(min_capacity) + ' or above are found in ' + school + ' :')
    display_school_facilities_by_capacity(facility_dict, school, min_capacity)
    
    
    ans = input('\nDo you want to search for the facilities within a school? [Y|N]:')
    
print('Good-bye!')

## Q4 Students and Schools
# SOLUTION

def get_students_by_school(student_school_dict):
    dict_to_return = {}
    
    for student in student_school_dict:
        school = student_school_dict[student]

        if school not in dict_to_return:
            dict_to_return[school] = [student]
        else:
            student_list = dict_to_return[school]
            student_list.append(student)
    return dict_to_return

## Q5a Word Counts
# SOLUTION

def count_words_in_file(filename):
    dict_to_return = {}
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            line = line.lower()
            line_words = line.split()
            for word in line_words:
                if word in dict_to_return:
                    dict_to_return[word] = dict_to_return[word] + 1
                else:
                    dict_to_return[word] = 1
    return dict_to_return

## Q5b Word Counts
# SOLUTION

for key in my_dict:
    frequency = my_dict[key]
    if len(key) >= 4 and frequency > 50:
        print(key + " : " + str(frequency))
        
## Q5c Word Counts
# SOLUTION

top_words = []
for i in range(10):
    
    top_word = ''
    max_freq = 0
    for word in my_dict:
        frequency = my_dict[word]
        my_tuple = (word, frequency)
        if my_tuple not in top_words and frequency > max_freq:
            max_freq = frequency
            top_word = word
    top_words.append( (top_word, max_freq) )

print(top_words)

## Q6 Employees
# SOLUTION

def create_employee_dictionary(filename):
    
    employees_dict = {}
    with open(filename, 'r') as my_file:
        for line in my_file:
            line = line.rstrip('\n')
            line_details = line.split('\t')
            # extract the id only
            emp_id = int(line_details[0][3:])
            emp_dict = {}
            # extract othe employee details in the rest of the line
            for item in line_details[1:]:
                item_list = item.split(':')
                key = item_list[0]
                value = item_list[1]
                emp_dict[key] = value
            # the value of each employee will be a dictionary containing all his/her details
            employees_dict[emp_id] = emp_dict
    return employees_dict


my_dict = create_employee_dictionary('employees.txt')

# keep prompting until employee exists
continue_search = 'Y'
while continue_search == 'Y':
    
    emp_id = int(input('Enter an employee ID :'))
    
    if emp_id not in my_dict:
        print('Not found!')
    else:
        emp_dict = my_dict[emp_id]
        print('This employee is ' + emp_dict['name'])
        field_name = input("Enter a field name or 'S' to stop :")
        while field_name != 'S':
            if field_name in emp_dict:
                print('The', field_name, 'is', emp_dict[field_name] + '.')
            else:
                print('Not found!')
            field_name = input("Enter a field name or 'S' to stop :")
    
    continue_search = input('\nDo you want to search for another employee? [Y|N] :')

print('Good-bye!')   
        
