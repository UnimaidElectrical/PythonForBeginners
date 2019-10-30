#Opening Files

# You can use python to read and write the contents of Files.
# text files are the easiest to manupulate. 
# Before a file can be edited, It must be opened, using the open function.

myfile=open("filename.txt")


The argument of the open function is the path to the file. 
If the file is in the current working directory of the program, you can specify only its name.





Opening Files
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.
Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).For example:

# write modeopen("filename.txt", "w")
# read modeopen("filename.txt", "r")open("filename.txt")
# binary write modeopen("filename.txt", "wb")


# You can use the + sign with each of the modes above to give them extra access to files. For example, r+ opens the file for both reading and writing.


# Reading Files
# The contents of a file that has been opened in text mode can be read using the read nethod

file = open("filename.txt", "r")
cout = file.read()
print(cout)
file.close()

# This will print all of the contents of the file "filename.txt"



# Reading Files Continued

# To read only a certain amount of a file, you can provide a number as an argument to the read function. 
# This determines the number of bytes that should be read. You can make more calls to read on the same file object 
# to read more of the file byte by byte. With no argument, read returns the rest of the file.

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# Just like passing no arguments, negative values will return the entire contents.