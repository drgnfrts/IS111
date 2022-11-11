def all_to_secs(time_tuple):
    h, m = time_tuple
    return m * 60 + h * 3600


def count_emails(file_name, start_time, end_time, sender):
    # Modify the code below.
    r_count = 0
    with open(file_name, "r") as input_file:
        for eachline in input_file:
            stripped = eachline.strip("\n").split("\t")
            hours, mins, secs = stripped[0].split(":")
            hours = int(hours)
            mins = int(mins)
            if secs[-1].isalpha():
                if secs[-2] == "A" and hours == 12:
                    hours = 00
                elif secs[-2] == "P" and hours != 12:
                    hours += 12
                secs = secs[:len(secs) - 2]
            secs = int(secs)
            newstart = all_to_secs(start_time)
            newend = all_to_secs(end_time)
            timestamp = all_to_secs((hours, mins)) + secs
            if sender != stripped[1]:
                continue
            if newstart <= timestamp <= newend:
                r_count += 1
    return r_count

# convert time ALL to seconds.


# Do not modify the code below!!!
if __name__ == '__main__':
    # #####################################
    # Test Cases of Q2
    print('\nTestcase 1')
    print('-' * 10)
    count = count_emails('emails-1.txt', (12, 30), (14, 0), 'joe@abc.com')
    print("Expected: 3")
    print('Actual:   ' + str(count))

    print('\nTestcase 2')
    print('-' * 10)
    count = count_emails('emails-2.txt', (11, 0), (14, 0), 'joe@abc.com')
    print("Expected: 2")
    print('Actual:   ' + str(count))
