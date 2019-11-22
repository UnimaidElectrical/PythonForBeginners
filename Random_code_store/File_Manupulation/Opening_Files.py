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



# Reading Files

# To read only a certain amount of a file, you can provide a number as an argument to the read function. This determines the number of bytes that should be read. 
# You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, read returns the rest of the file.

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# Just like passing no arguments, negative values will return the entire contents.



# Reading Files

# To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file.
# For example:

file = open("filename.txt", "r")
print(file.readlines())
file.close()


# You can also use a for loop to iterate through the lines in the file:

file = open("filename.txt", "r")

for line in file:
    print(line)

file.close()



# Working with Files

# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. 
# One way of doing this is to use try and finally.

try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

# This ensures that the file is always closed, even if an error occurs.




# Working with Files

# An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.
with open("filename.txt") as f:
   print(f.read())

# The file is automatically closed at the end of the with statement, even if exceptions occur within it.


# Which number is not printed by this code?
try:
  print(1)
  print(20 / 0)
  print(2)
except ZeroDivisionError:
  print(3)
finally:
  print(4)

#   What is the highest number that would be printed by this code?
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)