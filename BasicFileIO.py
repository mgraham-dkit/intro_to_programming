file_handle = open("students.txt")
student_info = file_handle.readline()
while student_info:
    print(student_info.strip())
    student_info = file_handle.readline()
file_handle.close()