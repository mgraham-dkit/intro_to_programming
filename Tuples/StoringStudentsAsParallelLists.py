names = []
grades = []

for i in range(2):
    names.append(input("Please enter the student name: "))
    grades.append(int(input("Please enter the student's grade: ")))
                  
for i,name in enumerate(names):
    print(str(i+1) + ") " + name + ": " + str(grades[i]))