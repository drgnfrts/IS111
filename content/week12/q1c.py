from q1a import retrieve_email


def add_new_email(email_dict, pair):
    searchkey, searchval = pair
    result = retrieve_email(email_dict, searchval)
    email_dict[searchkey] = searchval
    if result == None:
        return result
    else:
        return result


# Test cases used to test your function
print('\nTestcase 1')
print('-' * 10)
my_dict = {'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg'}
new_name = 'Peter'
new_email = 'peter@sis.smu.edu.sg'
pair = (new_name, new_email)

print("Expected returned value: peter@smu.edu.sg")
print('Actual returned value :  ' + str(add_new_email(my_dict, pair)))

print(
    "\nExpected dictionary: {'Jack': 'jack@gmail.com', 'Peter': 'peter@sis.smu.edu.sg'}")
print('Actual dictionary :  ' + str(my_dict))

print('\nTestcase 2')
print('-' * 10)
my_dict = {'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg'}
new_name = 'Mary'
new_email = 'mary@sis.smu.edu.sg'
pair = (new_name, new_email)

print("Expected returned value: None")
print('Actual returned value :  ' + str(add_new_email(my_dict, pair)))

print(
    "\nExpected dictionary: {'Jack': 'jack@gmail.com', 'Peter': 'peter@smu.edu.sg', 'Mary': 'mary@sis.smu.edu.sg'}")
print('Actual dictionary :  ' + str(my_dict))
