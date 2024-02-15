# File Handling (File Handling)

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)



# # Syntax

# f = open("demofile.txt")
# f = open("demofile.txt", "rt")



# # Read file 
# # Open a File on the Server
# f = open("demofile.txt", "r")
# print(f.read()

# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())

# # Read Only Parts of the File
# f = open("demofile.txt", "r")
# print(f.read(5))

# # Read Lines from the File
# f = open("demofile.txt", "r")
# print(f.readline())

# # Close Files
# f = open("demofile.txt", "r")
# print(f.readline())
# f.close()

# Python File Write