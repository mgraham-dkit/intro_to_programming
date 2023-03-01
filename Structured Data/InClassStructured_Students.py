# Open file (with read access)
file_handle = open("structured_students.txt")

# Read in first line
line = file_handle.readline()
# While there is still real data in file
while line:
    # Break up current line into student components
    # Structure employed in file is: id,name,degree,year
    student_data = line.split(",")
    # Display the 4 components with their corresponding labels
    print("ID:", student_data[0])
    print("Name:",student_data[1])
    print("Degree:",student_data[2])
    print("Year:", student_data[3])
    # Print break between students
    print("------------------------")
    # Read in next line from file
    line = file_handle.readline()

# Finished with file reading, close the connection to the file
file_handle.close()