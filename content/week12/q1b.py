def create_email_dict(list_of_names):
    mydict = {}
    tempkey = ""
    for line in list_of_names:
        if "@" in line:
            mydict[tempkey] = line
        else:
            tempkey = line
    return mydict


print(create_email_dict(["Jack", "jack@gmail.com", "Mary",
      "mary.loh@smu.edu.sg", "John", "john.smith@microsoft.com"]))
