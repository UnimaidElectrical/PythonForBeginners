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





#Function and Files
# This is to show how function and files work together 







#This is to display how to use the equate symbol "="

from sys import argv
script, input_file = argv

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")



# contains(arr, value): return True if value is in arr

# def arrayCheck(arr, value):
    

"""
More Functions Pratice
"""

print("Let's pratice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\nnewlines and \t tabs')

poem = """
\t The lovely world
with logic so firmly planted
cannot desern \nthe needs of love
nor comprehend position from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("----------")
print(poem)
print("----------")



five = 10-2+3-6
print(f"This should be five: {five} ")

def secret_formular(started):
    jelly_beans = started * 500
    jars = jelly_beans /1000
    crates = jars /100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formular(start_point)

#remember that this is another way to format a string
print("with a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point /10


print("We can also do that this way:")

formular = secret_formular(start_point)
#This is an easy way to apply a list to a format string

print("We'd have {}beans, {} Jars, and {} crates.".format(*formular))















# faster than a plane of alabama bbq




# def knockout(matedor):
#     calling_another_function(mistah, misiz, omomor)
#     firstName = scales + 300
#     secondName = firstName + 400
#     thirdName = secondName + 500
#     return firstName, secondName, thirdName


# def calling_another_function(mistah, misiz, omomor):
#     mistah = 'a'
#     misiz = 'b'
#     omomor = 'c'
#     return calling_another_function(mistah,misiz,omomor)


# knockout(20)



#Python Reserved words
and       |  del       |  for       |  is       |  raise   
assert    |  elif      |  from      |  Lamda    |  return
break     |  else      |  global    |  not      |  try
class     |  except    |  if        |  or       |  while
continue  |  exec      |  import    |  pass     |  yield
def       |  finally   |  in        |  print






#Augumented Assignment Statements

X += Y
X *= Y
X %= Y 
X &= Y
X ^= Y
X <<= Y
X >>= Y
X -= Y
X /= Y
X **= Y
X |= Y
X //= Y

S = "spam"
S += "SPAM"
S


X=0
Y=0
X=5
Y=4
X >>= Y
X
Y


#UNPACKING ASSIGNMENT
nudge = 1
wink = 2
A, B = nudge, wink
A, B

[C, D] = [nudge, wink]
C, D

#SWAP
nudge = 1
wink = 2
nudge, wink = wink, nudge
nudge, wink

#Range Assignment

red, green, blue = range(3)
red, blue




L = [1, 2]
L = L + [3]     #Concartinate: slower
L


L.append[4]    #Faster, but in-place
L


L = L + [5, 6]      #Concartinate: Slower
L

L.extend([7, 8])      #Faster, but in-place
L

#The inplace equavalent obviously runs faster than the concartinate option 

L += [9, 10]  #Mapped to L.extend([9, 10])
L

L[len(L):]  = [11,12,13]   #this is the same thing as extend 





 







