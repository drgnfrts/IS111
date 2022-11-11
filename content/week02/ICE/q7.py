# This line of code prompts the user for a system time.
input_str = input('Please enter the system time (in seconds): ')

################################################################################
# Complete the code below to get the correct numbers of days, hours, minutes and seconds.

# num_days = 0
# num_hours = 0
# num_minutes = 0
# num_seconds = 0

# Put your code below

ONE_DAY = 60 * 60 * 24
ONE_HOUR = 60 * 60
ONE_MINUTE = 60

system_time_secs = int(input_str)

num_days = system_time_secs // ONE_DAY
num_hours = system_time_secs % ONE_DAY // ONE_HOUR
num_minutes = system_time_secs % ONE_DAY % ONE_HOUR // ONE_MINUTE
num_seconds = system_time_secs % ONE_DAY % ONE_HOUR % ONE_MINUTE


################################################################################
# DO NOT MODIFY THE CODE BELOW!!!

# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' +
      str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.')
