# Name: Tang Wen Chung, Nicolas
# Email ID: nicolastang.2022

from q3a import read_courses


def countable_to_gpa(subject, start_term, end_term):
    name, year, term, credit, gpa = subject
    if start_term <= (year, term) <= end_term:
        return True
    return False


def calculate_student_gpa(filename, start_term, end_term):
    student_results = read_courses(filename)
    r_dict = {}
    for student, subjects in student_results.items():
        credit_total = 0
        score_total = 0
        subject_total = 0
        for each_subject in subjects:
            if not countable_to_gpa(each_subject, start_term, end_term):
                continue
            sn, year, term, credit, gpa = each_subject
            score_total += (gpa * credit)
            credit_total += credit
            subject_total += 1
        final_gpa = float(round((score_total / credit_total), 1))
        r_dict[student] = (subject_total, final_gpa)
    return r_dict
