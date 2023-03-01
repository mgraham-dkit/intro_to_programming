# File reading
file_handle = open("tester.txt")
data = []
line = file_handle.readline()
while line:
    # strip() removes the padding and formatting characters at the start
    # and end of a line of text
    # All data coming in from a file is read in as text, so you have to cast
    # to a number if you are reading numeric data
    num = int(line.strip())
    print(num)
    data.append(num)
    line = file_handle.readline()
    
file_handle.close()

# File writing
# This will open the file in "write" (i.e. overwrite) mode
# If you want to open the file and have your program add its data in at the end
# (i.e. inserted after the data already in the file), you need to set it to
# "append" mode. You do this by using "a" instead of "w" in your open call
file_handle = open("multiple.txt", "w")
for num in data:
    # Remember 2 things here:
    # 1) All data going to a file must be TEXT, so you need to
    # cast the numbers to text before writing out
    # 2) You are writing out data but there's no mention of a line wrap,
    # so you have to include the newline character manually
    file_handle.write(str(num*5)+"\n")
file_handle.close()
