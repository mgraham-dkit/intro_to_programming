# Open file (with read access)
file_handle = open("numbers.txt")

# Create list to store the information
file_data = []
# Read in first line
line = file_handle.readline()
# While there's still real data from file to process
while line:
    # Strip off padding from current line, cast to a number and store in a list
    file_data.append(int(line.strip()))
    # Read in the next line from the file
    line = file_handle.readline()
# File reading is finished, so close the connection to the file
file_handle.close()

# Loop through the list of numbers pulled from the file, displaying the current number and its square
for num in file_data:
    print("Number:", num, " squared is", (num*num))
    