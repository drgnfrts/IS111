def extract_multiple_email_ids(emails):
    list_of_emails = emails.split(";")
    for email in list_of_emails:
        if "@" in email:
            broken_string = email.split("@")
            print(broken_string[0])
        else:
            print()


extract_multiple_email_ids(
    "jerry.lee@sis.smu.edu.sg;alan_wong@gmail.com;george_tan@yahoo.com")
extract_multiple_email_ids("")
extract_multiple_email_ids("jerry.lee@sis.smu.edu.sg")
