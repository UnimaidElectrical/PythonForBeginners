# *args This is very similar to the argv when writing statements
#*args here works like a charm.
"""
This tells python to take all the arguments to the function and then put them in args as a list.
It's like argv but only that it's for function. It is not normally used unless it is specifically needed.
"""
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1},arg2: {arg2}")

print_two("Zed","Shaw")



# # in otherwords, that *args is not needed. 
def print_two_again(arg1,arg2):
    print(f"agr1: {arg1},arg2: {arg2}")

print_two_again("Tega","Max")

# #This takes in just one agument

def print_one(arg1):
    print(f"arg1: {arg1}")
print_one("First!")

# #This is a function that takes no argument

def print_none():
    print("I got nothing'.")
print_none()


#Functions and variables
#The variables in your function are not connected to the variables in your script
#A function can be called in any way possible there is no theoritically correct way to call a function

def cheese_and_crackers(cheese_count, boxes_of_cheese):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_cheese} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the functin numbers directly: ")
cheese_and_crackers(10,20)

print("OR, We can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do more math inside too: ")
cheese_and_crackers (10+20,5+6)


print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)









