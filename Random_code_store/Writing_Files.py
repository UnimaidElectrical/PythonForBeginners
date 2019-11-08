# Writing Files

# To write to files you use the write method, which writes a string to the file.
# For example:

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()