# Create a function that takes in a filename as a parameter,
# reads in the content of the file and generates a list of numbers from the data
# This function requires the filename supplied to be a text file of numbers
def read_int_file(filename):
    file_handle = open(filename)

    file_data = []
    line = file_handle.readline()
    while line:
        file_data.append(int(line.strip()))
        line = file_handle.readline()
    file_handle.close()
    return file_data


# Use the function from above to read in the numbers file
# and save the returned list generated from the file in a variable
file_data = read_int_file("numbers.txt")
for num in file_data:
    print("Number:", num, " squared is", (num*num))
    
