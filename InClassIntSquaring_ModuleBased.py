# Import read_int_file function from the useful_functions module
# This gives the current program access to that function
from useful_functions import read_int_file

# Use the read_int_file function to read in the file's contents
# and store the result in a list
file_data = read_int_file("numbers.txt")
for num in file_data:
    print("Number:", num, " squared is", (num*num))