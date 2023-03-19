def create_record():
    stud_id = input("Please enter your student ID ")
    stud_name = input("Please enter your first and last name ")
    stud_age = input("Please enter your age ")
    stud_add = input("Please enter your address ")
    stud_phone = input("Please enter your phone number ")
    student_info = [stud_id, stud_name, stud_age, stud_add, stud_phone]
    return student_info


x = int(input("Please choose an option 1-5 "))
if x == 1:
    create_record()
else:
    print("That's not a valid option")

record_list = create_record()
print(record_list)
