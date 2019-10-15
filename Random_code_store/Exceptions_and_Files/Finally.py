# Finally

# To ensure some code runs no matter what errors occur, you can use a finally statement. 
# The finally statement is placed at the bottom of a try/except statement. 
# Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.


try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by Zero")
finally:
    print("This code will run, no matter what!")


#Uncaught Exception
#The code in the finally statement even runs if an uncaught exceotion occures in one of the preceding blocks 

try:
    print(1)
    print(10/0)
except ZeroDivisionError:
    print(Unknown_Var)
finally:
    print("This is executed last")

    