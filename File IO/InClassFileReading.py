def display_students(students):
    for name in students:
        print(name.strip())


file_handle = open("students.txt")
student_info = file_handle.readlines()
file_handle.close()
display_students(student_info)