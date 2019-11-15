# Writing Files

# To write to files you use the write method, which writes a string to the file.
# For example:

file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()


# Writing Files

# When a file is opened in write mode, the file's existing content is deleted.
# the content of the file will be overritten

file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()


# The write method returns the number of bytes written to a file, if successful.

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

# To write something other than a string, it needs to be converted to a string first.