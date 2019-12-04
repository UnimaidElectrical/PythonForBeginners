# define strings                                                         
firstname = "Bugs"
lastname = "Bunny"

# define our sequence                                                    
sequence = (firstname,lastname)

# join into new string                                                   
name = " ".join(sequence)
print(name)



#Joining a list of words
words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)

# Splitting

s = "Its too easy"
words = s.split()
print(words)
print(len(words))
print(len(s))

# splits the words into letters
word = "Easy"
g = list(word)
print(g)



#splits the group of words by a comma
s="World,Earth,America,Canada"
word=s.split(", ")
print(word)


#Random Numbers

# Generate random numbers

import random
# Create a random floating point number and print it.
print(random.random())

# pick a random whole number between 0 and 10.
print(random.randrange(0,10))

# pick a random floating point number between 0 and 10.
print(random.uniform(0,10))


# If Statements

gender = input("Gender? ")
if gender == "male" or gender == "Male":
    print("Your cat is male")
else:
    print("Your cat is female")

age = int(input("Age of your cat? "))
if age < 5:
    print("Your cat is young.")
else:
    print("Your cat is adult.")




# For Loops

city = ['Tokyo','New York','Toronto','Hong Kong']
print('Cities loop:')
for x in city:
    print('City: ' + x)


print('\n')  

num = [1,2,3,4,5,6,7,8,9]
print('x^2 loop:')
for x in num:
    y = x * x
    print(str(x) + '*' + str(x) + '=' + str(y))


#Printing out the city names in a line
city= ["Lagos","Abuja","Kano","Kaduna"]
for n in city:
    print('City:' + n)

print('\n') # newline


# squaring two numbers and showing your work
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    y=i*i
    print(str(i) + '*' + str(i) + '=' + str(y))

#Questions 

2. Create a loop that counts from 0 to 100
for ide in range(0,100):
    print(ide)


3. Make a multiplication table using a loop
for i in range(10):
    j=i*
4. Output the numbers 1 to 10 backwards using a loop
5. Create a loop that counts all even numbers to 10
for i in range(0,10,2):
    print(i)

6. Create a loop that sums the numbers from 100 to 200

sum=0
for i in range(100,200):
    sum = sum + i
    print(sum)


# While Loop

x = 3                              
while x < 10:
    print(x)
    x = x + 1




while True:
    print('Forever')


2. What’s the difference between a while loop and a for loop?
3. Can you sum numbers in a while loop?
4. Can a for loop be used inside a while loop?



# Functions
def currentYear():
    print('2018')
currentYear()


# Functions with parameters
#!/usr/bin/env python3

def f(x,y):
    return x*y

print(f(3,4))



# Return variables
result = f(3,4)
print(result)



1. Make a function that sums the list mylist = [1,2,3,4,5]
2. Can functions be called inside a function?
3. Can a function call itself? (hint: recursion)
4. Can variables defined in a function be used in another function? (hint: scope)






list = [ "New York", "Los Angles", "Boston", "Denver" ]

print(list)     # prints all elements
print(list[0])  # print first element

list2 = [1,3,4,6,4,7,8,2,3]

print(sum(list2))
print(min(list2))
print(max(list2))
print(list2[0])
print(list2[-1])








states = [ 'Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming' ] 

# Display all states starting with the letter M
# all_states=states.split()

for i in states:
    if states.startswith('m'):
        print(i)
    


    #String to be splitted
St = 'where is my mobile'

#Split the string on blank characters
List = St.split()

#for each element in the list, if it starts with 'm' then print it
for s in List:
    if s.startswith('m'):
        print(s)


# Append and Pop
x = [3,4,5]
x.append(6)
print(x)
x.append(7)
print(x)
x.pop()
print(x)


# Accessing Items
x = [3,4,5]

print(x[0])
print(x[1])

print(x[-1])



questions:

1, Given the list y = [6,4,2] add the items 12, 8 and 4.
2, Change the 2nd item of the list to 3.



#Sorting





x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
y=(x[0][0],x[1][0])
print(y)


x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(x[0])

y=



x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print(x)

# list Strings can also be sorted.

words = ["Be","Car","Always","Door","Eat" ]
words.sort()
print(words)


# Reverse order
# To sort in reverse order, combine it with the method reverse()


x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
x = list(reversed(x))
print(x)


words = ["Be","Car","Always","Door","Eat" ]
words.sort()
words = words[::-1]
print(words)


# Range function

x = list(range(100))
print(x)


# Python starts counting from zero. Now what if you want to count from 1 to 100?

x = list(range(1,101))
print(x)


# A third parameter defines the step size, by default its one. Range can be used in a for loop:

for i in range(1,11,2):
   print(i)

# Try the exercises below

# Create a list of one thousand numbers
# Get the largest and smallest number from that list
# Create two lists, an even and odd one.


# we define some key,value pairs and then print them using their unique keys.

words = {}
words["BMP"] = "Bitmap"
words["BTW"] = "By The Way"
words["BRB"] = "Be Right Back"

print words["BMP"]
print words["BRB"]










#Nested Loops
# A loop can contain one or more other loops: you can create a loop inside a loop.
# This principle is known as nested loops. Nested loops go over two or more loops.
# Programmers typically nest 2 or 3 levels deep. Anything higher than that is just confusing


persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]

for person in persons:
    for restaurant in restaurants:
        print(person + " eats " + restaurant)


Try the exercises below

Given a tic-tac-toe board of 3x3, print every position
horizontal_view=["1","2","3"]
vertical_view=["a","b","c"]

for horizontal in horizontal_view:
    for vertical in vertical_view:
        print(horizontal + vertical)

Create a program where every person meets the other
persons=["John", "Marissa", "Pete", "Dayton"]
persns=["Marissa", "Pete", "Dayton"]    (since one persion cannot meet themselves how can i take that out)

for person in persons:
    for persn in persns:
        print (person + " meets " + persn)


If a normal for loop finishes in n steps O(n), how many steps has a nested loop?
a nested loop will still have O(n) steps



# Slices
# A slice can be taken from a string or list, just as you can take a slice from a pizza.
# If you have a variable, be it a list or a string, that you want a part of, you don’t have to define it all over again.
# You can get a copy of the variable, which is the whole or a subset of the original variable. This concept is known as slicing.


# List Slice

persons = [ "John", "Marissa", "Pete", "Dayton" ]

slice = persons[0:2]
print(slice)


# String Slice

destination = "hello world"
mySlice = destination[6:11]
print(mySlice)

destination = "summer holiday at beach"
mySlice = destination[0:6]
print(mySlice)


# Try the exercises below
 
# Take a slice of the list below:
pizzas = ["Hawai","Pepperoni","Fromaggi","Napolitana","Diavoli"]
MySlice=pizzas[1:2]
print(MySlice)

# Given the text “Hello World”, take the slice “World”

world_slices="Hello World"
MySlice=world_slices[6:11]
print(MySlice)


# Multiple return
# Python functions can return multiple variables. These variables can be stored in variables directly. 
# A function is not required to return a variable, it can return zero, one, two or more variables.
# This is a unique property of Python, other programming languages such as C++ or Java do not support this by default.

def complexfunction(a,b):
    sum = a +b
    return sum
complexfunction(2,3)


# Multiple Return 

def getPerson():
    name = "Leona"
    age = 35
    country = "UK"
    return name,age,country

# name,age,country = getPerson()
print(name)
print(age)
print(country)

Try the exercises below:

Create a function that returns a,b and a+b

def sum_and_list():
    listed = "ab"
    sum = a+b
    return sum,listed
sum,listed=sum_and_list()
print(sum)
print(listed)


Create a function that returns 5 variables

def car_choices():
    jeep = "Wrangler_2019"
    audi = "Q7_2019"
    mazda = "a6_2019"
    lexus = "Rx350_2019"
    BMW = "series_2019"
    return jeep,audi,mazda,lexus,BMW
jeep,audi,mazda,lexus,BMW=car_choices()
print(jeep)
print(audi)
print(mazda)
print(lexus)
print(BMW)

