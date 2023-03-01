ids = []
names = []
degrees = []
years = []
# Open file (with read access)
file_handle = open("structured_students.txt")

i = 0
# Read in first line
line = file_handle.readline()
# While there is still real data in file
while line:
    # Break up current line into student components
    # Structure employed in file is: id,name,degree,year
    student_data = line.split(",")
    ids.append(student_data[0].strip())
    names.append(student_data[1].strip())
    degrees.append(student_data[2].strip())
    years.append(student_data[3].strip())
    # Read in next line from file
    line = file_handle.readline()

# Finished with file reading, close the connection to the file
file_handle.close()

for i in range(len(ids)):
    # Display the 4 components with their corresponding labels
    print("ID:", ids[i])
    print("Name:",names[i])
    print("Degree:",degrees[i])
    print("Year:", years[i])
    
'''
 Define a format for our structured student output
 {} indicates where a "real" value will be inserted in place of the placeholder text
 All other text in the string is literal,
 i.e. it will appear within the string exactly as shown
'''
student_structure = "{id},{name},{degree},{year}\n"
# Open connection to the file - We can use this to write to the file
# and it will append, not overwrite because we are using "a" instead of "w"
file_handle = open("structured_students.txt", "a")
# Loop through the contents of the lists and output their information
# We use the format defined above to structure how the data will appear when written out
# The placeholders are filled in using the key=value pair syntax,
# the key is the name of the placeholder and the value is the
# relevant information for that position in the lists
for i in range(len(ids)):
    file_handle.write(student_structure.format(id=ids[i],name=names[i],degree=degrees[i],year=years[i]))
    
# Once all data has been written out to the file
# (i.e. the lists have been looped through fully),
# close the file
file_handle.close()    