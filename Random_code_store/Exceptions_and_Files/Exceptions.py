


#Python has several other built-in functions, such as ZeroDivisionError and OSError. Third-party libraries also often define their own exceptions



#
# Exception Handling


# To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
# The try block contains code that might throw an exception. If that exception occurs, the code in the try block stops being executed,
# and the code in the except block is run. If no error occurs, the code in the except block doesn't run.

try:
    num1=7
    num2=0
    print(num1/num2)
    print("Done Calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to ZeroDivisionError")



# Exception Handling #2

# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can also be put into a single except block using parenthesis, to have the except block handle all of them.

try:
    variable =0
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by Zero")
except (ValueError, TypeError):
    print("Error Occured")



#An except statement without any exception specified will catch all errors. These should be used sparinghly, as they can catch 
# unexpected errors and hide programming mistakes.

try:
    word="spam"
    print(word/0)
except:
    print("An error occured")


#raising exceptions
print(1)
raise ValueError
print(2)

# you need to specify the type of exception raised at all times

# Which error occur during the handling of this code 
try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError   



# exceptions can be raise without giving details about them

name = '123'
raise NameError("Invalid name")

# fill in the blanks to raise a ValueError exception, if the input is negative.

num = input(":")
if float(num) > 0
    raise ValueError("Negative!")



In the except block the raise statement can be used without arguments to re-raise whatever exception occured.

try:
    num = 5/0
except:
    print("An error occured")
    raise