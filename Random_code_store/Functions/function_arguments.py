#Function Arguments

#we have functions with zero arguments. In orther words these are functions with empty parentheses.

#Function that takes in one arguement

def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

#The arguements are defined inside the parenthesis

#what is the result of the code?

def print_double(x):
    print(2*x)
print_double(3)


#Arguments 

def print_sum_twice(x,y):
    print(x+y)
    print(x+y)
print_sum_twice(5,8)




#Referencing Function Arguments
#Function arguments can be used as variables inside the function defination. However, they cannot be referenced outside the function's defination
#This also applies to other variables inside a function.

def function (variable):
    variable +=1 
    print(variable)

function(7)
print(variable)

#in order words 
#parameters are the variables in a function defination, and 
# arguments are the values put into parameters when the functions are called.


#Using an if/else statement in a function call
def even(x):
    if x%2==0:
        print("Yes")
    else:
        print("No")

#using an if/elif/else statement in a function call 
