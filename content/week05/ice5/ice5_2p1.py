def extract_email_id(email):
    if "@" in email:
        broken_string = email.split("@")
        return broken_string[0]
    else:
        return ""


print(extract_email_id("jerry.lee@sis.smu.edu.sg"))
print(extract_email_id("alan_wong.com"))
print(extract_email_id(""))
print(extract_email_id("alan_wong@gmail.com"))
