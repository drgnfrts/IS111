# Name:
# Email ID:
import datetime


def get_days_between(start_tup, end_tup):
    start_date = datetime.date(*start_tup)
    end_date = datetime.date(*end_tup)
    return (end_date - start_date).days


def date_format_conversion(input_date):
    splitted = input_date.split("/")
    date, month, year = splitted
    return (int(year), int(month), int(date))


def get_vaccination_status(filename, today):
    r_list = {}
    with open(filename, "r") as inputfile:
        for eachline in inputfile:
            stripped = eachline.strip("\n").split("|")
            name, age, start, end = stripped
            age = int(age)
            if age < 12:
                r_list[name] = (age, False)
                continue
            if start == "NA" or end == "NA":
                r_list[name] = (age, False)
                continue
            if not 27 < get_days_between(date_format_conversion(start), date_format_conversion(end)) < 57:
                r_list[name] = (age, False)
                continue
            if get_days_between(date_format_conversion(end), date_format_conversion(today)) < 14:
                r_list[name] = (age, False)
                continue
            r_list[name] = (age, True)
    return r_list