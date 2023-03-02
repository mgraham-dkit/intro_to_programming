# Create a list of students and fill it with information
# A student is made up of a name (string) and a grade (int)
students = []

for i in range(5):
    name = input("Please enter the student name: ")
    grade = int(input("Please enter the student's grade: "))
    # Bind the two student components into a single entity - the student tuple
    student = (name, grade)
    # Save the student:
    # Add that student entity (the tuple) into the list of students
    students.append(student)
 
# Display the student information
'''
Reminder: enumerate returns each element from a collection
AND its position.
This is why we need to specify two variable names (i and student),
the first variable (i) will hold the current position in the list
the second variable (student) will hold the current element from the list
'''
for i,student in enumerate(students):
    print(str(i+1) + ") " + student[0] + ": " + str(student[1]))