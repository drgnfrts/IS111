while True:
    student = input("Are you a student? ")
    yn = ["Yes", "No", "YES", "NO", "yes", 'no']
    if student in yn:
        print("Got it!")
        break
    print("Please enter a valid answer (YES, Yes, yes, NO, No, no)")
