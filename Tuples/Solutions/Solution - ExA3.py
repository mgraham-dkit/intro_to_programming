def count_vowels(text):
    count = 0
    count = count + text.count("a")
    count = count + text.count("e")
    count = count + text.count("i")
    count = count + text.count("o")
    count = count + text.count("u")
    return count

def count_vowels_improved(text):
    vowels = ["a","e","i","o","u"]
    count = 0
    for letter in vowels:
        count += text.count(letter)
    return count


filename = input("Please enter the student file name: ")

student_names = []
with open(filename) as file_handle:
    for line in file_handle:
        student_names.append(line.strip())
        
student_tuple = tuple(student_names)
for student in student_tuple:
    print("Student", student, "has", count_vowels_improved(student.lower()), "vowels in their name.")
