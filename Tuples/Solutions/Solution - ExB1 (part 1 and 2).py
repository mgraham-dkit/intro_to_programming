def validate_grade(num):
    if num >=0 and num <= 100:
        return True
    else:
        return False
    

grade_count = 0
grade_list = []
while grade_count < 5:
    grade = int(input("Please enter a grade: "))
    if validate_grade(grade):
        grade_list.append(grade)
        grade_count += 1
    else:
        print("Grades must be between 0 and 100")
        
grades = tuple(grade_list)
# Handling highest grade
max_grade = max(grades)
max_pos = grades.index(max_grade)
print("The highest grade achieved was", max_grade, "in position", max_pos)

# Handling lowest grade
min_grade = min(grades)
min_pos = grades.index(min_grade)
print("The lowest grade achieved was", min_grade, "in position", min_pos)

# Handling average
grades = tuple(grade_list)
total = sum(grades)
average = total/len(grades)
print("The average grade achieved was", average)