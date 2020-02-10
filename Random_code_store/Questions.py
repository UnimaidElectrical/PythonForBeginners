#What is the output of this code?
print(6+5-4*3/2%1)

#what is the output of this code?
def at(func,arg):   
    return func(func(arg))
def af(x):
    return x + 5
print(at(af,10))

# What is the most probable output of this code?
import random
a =[1,2,3,4,5]
sum = 0
for i in range(1000):
    b = random.choice(a)
    sum+=b
print(round(sum/1000))


#What is the output of this code?
x=list(range(0,6,2))
print(len(x))

#what is the output of this code?
y=1
z=3
x=5
loc={x:y,y:z,z:x}
print(loc[y])

#what is the output of this code?
double =lambda x: x * 6
print(double(5))

#What is the output of this code?
a=[1,5,6]
b=a[::1]
b[2]=2
b[1]=8
print(b[2])


#This shows the difference betwwn a list and a dictionary
list=[1,1,2,3,5,8,13]
print(list[list[4]])


#what does this code do?
#This code will print all the even number between 2 and 10
for i in range(10):
    if not i%2==0:   # not will be for even number and without the not will be for odd numbers
        print(i+1)



#what is the output of this code?
i='3471'
z=i[::-1]
if i==z:
    print(z)
else:
    print(z[2]*2 + z[3]*2)


#what is the output of this code?
a=[1,2,3,4]
b=a[:]
print(a==b,id(a)==id(b))



#Find the blanks to complete the implementation of custom map function.

# def myMap(lst,f):
#     nlst=[]
#     for val_lst:
#        nlst.append(__(val))
#     return(nlst)
# x=[1,2,3,4,5]
# print(myMap(x,lambda x:x**2))



#what is the output of this code?
b=0
for i in range (100):
b +=b
print(b)

#How many numbers will this code output?
i=0
while i <=5:
    print(i)
    i+=1

#What is the output of this code.
a=(lambda x:x**2 + 5 * x + 4)(-4)
print(a)


#What is the output of this code
a = [1,2,3,4]
def func(a):
    a = a + [5]
    return a
print(a == func(a))


#What is the output of this code
print((2**2) ** (12%10))

#What is the output of this code
a=[10,3,7]
y,x,z=a
print(y%z)



#What is the output of this code
def my_func(x,y):
    if(x > y and y > 0):
        print("True")
    else:
        print("False")
my_func(9,8)

#What is the output of this code
list1 = [1,2,3,4]
list2 = [5,6,7,7]
print(len(list1 + list2))

#What is the output of this code

def f(n):
    if n==1:
        return "0"
    else:
        return n*f(n-1)
print(int(f(5) == 120))


#What is the output of this code
x='123'
def fun(x):
    y=x.split(x[0])
    print(y[1])
fun(x)


#What is the output of this code
import math
print(math.pow(27,1/3))

#What is the output of this code
list1=[1,2,3,4];
list2=list1;
list1.append(5);
print(list2);


#What is the output of this code
seq=2
list_1 = [1,1,4]
for i in range(1, len(list_1)):
    h=list_1[i]-list_1[i-1]
    if h!=seq:
        list_1[i] = list_1[i-1] +seq
print(list_1)


#What is the output of this code
a= [1,[2,3]]
b = [1,2,3]
c=a[:]
d=b[:]
print(c is a,d is b)

#What is the output of this code
f = ((0,)
f = f +(2,)
print(f)


#what is the output of this code
print(float(5*5//9+int(12)))

#What is the output of this code
a=2
b=3
a,b=b,a
print(a**b)


#What is the output of this code
def func(a,b):
    c=(a+b)+(a+b)
    d=c%2
    e=d+c
    print(c)
func(3,3)


#What is the output of this code
a= [x for x in range(4)]
print(sum(a[1::-2]+ a[::-3]))


#What is the output of this code
if (2==2) and (2+5 >=7):
    print("true")
else:
    print("false")

#What is the output of this code
print({True: 'yes',1: 'no', 1.0: 'maybe'})


#What is the output of this code
y=4
x=2
z=3
def a(x,y,z):
    if x!=8 or y==5 and z==3:
        print(str(x*z)+str(y))
    else:
        print("66")
a(x,y,z)



#What is the output of this code
def shout(word):
    return word + "!"
speak = shout
output = speak("shout")
print(output)


#What is the output of this code

def sum(x):
    res=0
    for i in range(x):
        res +=i
    return res
print(sum(5))


#What is the output of this code
def print_nums(x):
    for i in range(x):
        print(i)
        return
print_nums(10)


#What is the output of this code
def func(x):
    res=0
    for i in range(x):
        res += i 
    return res
print(func(4))



#What is the output of this code
try:
    variable=10
    print(10/2)
except ZeroDivisionError:
    print("Error")
print("Finished")


#What is the output of this code
try:
    print(1)
except:
    print(2)
finally:
    print(3)


#What is the output of this code
a =[3,5,7,9]
b = a 
a[1]=8
print(b[1])


#What is the output of this code
count = 0
for i in range(5):
    for j in range(i):
        count+=1
print (count)


#What is the output of this code
import re
x='from:physicsisfunny@python.com'
y=re.findall('\S+?@\S+',x)
print(y)

#What is the output of this code
list1=[]
list2=[]

for i in range(5)[::-1]:
    list1.append(i)
for j in list1[::-2]:
    list2.append(j+1)
print(list1[2])

#What is the output of this code
s='potato'
print(s[-5::-1])

#What is the output of this code
x=y=[10,5,7]
x[0] =5
print(y)


#What is the output of this code
num_list = [-4,-3,-2]
print(abs(-4)*abs(max(num_list)))


#What is the output of this code
a=[7,3,9,5]
b=[8,0,4]

if a >b:
    print(len(a))
else:
    print(len(b))


#What is the output of this code
num = 12
answer = 2 if num % 7 >= 5 else 0
print(answer)


#What is the output of this code
arr=[str(i**3) for i in range (3,5)]
print(sum(arr))


#What is the output of this code
a=1
b=3
if (a<=5 and b<9):
    if (a==4):
        b=20
    a += 1
    b -=1
if (b<20):
    a=-5
print(a)


#What is the output of this code
a=6
a,b= 0, a+1
print(a*"str")


#What is the output of this code
X = "2" + "4"
print(X)


#What is the output of this code
s="string"
x = s
s = s + "s"
print(x[-1])


#What is the output of this code
x = 5
def changevar(x):
    x+=1
    return x
print(changevar(x))


#Is the code below valid ?
x = {(1,2):"buckle", 34:"knock","56":"forget"}


#What is the output of this code
try:
    s = ['a','c']
    n = [0,2]
    s[1:1] = 'b'
    n[1:1] = 1
except:
    pass
print(s[1],n[1])


#What is the output of this code
def f(n,v):
    n= len(v)
    v.append(n)
n=0
v=[8,0,4,6]
f(n,v)
print(n,sum(v))


#What is the output of this code
def print_with_exclamation(word):
    print(word + "!")
print_with_exclamation("spam")


#What is the output of this code
a = [1,2,[3,4],6,5]
print(a[a[2][1]])


#What is the output of this code
x=int('22143'[3])
print(x)

#What is the output of this code
dict_a = {'A':1,'B':2,'C':3}
print(len(dict_a))


#What is the output of this code
num1 =[1,3,4,5]
num2=num1
num2[0] = 5
print(num1[0])


#What is the output of this code
num1=5
num2="5"
print(num1*int(num2))


#What is the output of this code
i=0
def func(x,y):
    i=x+y
    func(4,5)
print(i)

#What is the output of this code: Jesse Schaar
class Myclass():
    n=0
    def__init__(self):
        MyClass.n +=1
    def__del__(self):
        Myclass.n -= 1
a = MyClsss()
print (a.n)
b = MyClass()
print(b.n)
a = MyClass()
print(a.n)


#What is the output of this code?
x=1
while x<5:
    x *= 2
print(x)

#What is the correct output ?
words = ["$10,","$20,","$30"]
for i in range(3):
    print(words[i], end='')
    if i ==2:
        print()
for i in words:
        print(i,end = '')


#What coes the list comprehension create?
a=[2*i +1 for i in range(7)]
print (a)


#What is the output of this code?
a=[1,2,3,4,12,13]
for i in a:
    if i % 2 ==1:
        a.append(0)
print(len(a))


#What is the output of this code?
double = lambda x : X * 6
print(double(5))

#What is the output of this code?
A = [4,3,1,6,8,5,2,7]
n = len(A)
for pos in range(n):
    m = min(A[:n-pos])
    A.remove(m)
    A.append(m)
print(A)

#What is the output of this code?
name ="Mark Foxx";
names = name.split(" ");
if names[1].endswith("foxx"):
    print(1)
else:
    print(0)

#What is the output of this code?
a, b, *c = [9,8,7,6]
print(b)

#What is the output of this code?
class A:
    def __init__(self):
        print(1)
class B(A):
    def __init__(self):
        super(A,self).__init__()
        print(2)
obj = B()

#What is the output of this code?
def build_list(element,to=[]):
    to.append(element)
    return to
my_list = build_list(2)
print (my_list)
my_other_list = build_list(5)
print (my_other_list)

#What is the output of this code?
class Mul:
    def __init__(self,n):
        self.n = n
    def __pow__(self,fles):
        return [fles ** i for i in self.n]
print(sum(Mul((1,2,3))**2))


#What is the output of this code?
class A:
    def __init__(a,b,c):
        print(b)
    A(8,3)


#What is the output of this code?
i=0
def func(x,y):
    i =x + y
func(4,5)
print(i)


#What is the output of this code?
i=0
def func(x,y):
    i =x + y
func(4,5)
print(i)



# Will the close() function get called in this code?
try:
  f = open("filename.txt")
  print(f.read())
  print(1 / 0)
finally:
  f.close()


#What is the output of this code?

a,b =[0],[0]
a,b=b,a
if(a is b):
    print(True)
else:
    print(False)


#What is the output of this code?

def func(**querty):
    print(querty["one"])
func(a=0,one=173)


#What is the output of this code?
a = 1 % 213
b = 1 % 215
print(a == abs(b))


#What is the output of this code?
a=["c","b","a"]
a=a[::-1]
print(a[1])


#What is the output of this code?
def func(a,b):
    c=(a+b)+(a+b)
    d=c%3
    return(d)
print(func(2,2))


#What is the output of this code?
randinterger=range(4,7,2)
randinterger.append(9)
y=float(len(randinterger))
v=len(randinterger)
print("v" + y+randinteger[1])





*********************************************************************************************************************************************************
                                                    NEW QUESTIONS
*********************************************************************************************************************************************************

Question:
Insert the correct keyword to make the variable x belong to the global scope.


Solution:
def myfunc():
  
global x
  x = "fantastic"




Question:
Insert the correct syntax to convert x into a complex number.

Solution:
x = 5
x = complex (x)


Question:
Replace the character H with a J.


Solution:

txt = "Hello World"
txt = txt.replace ("H", "J")



Question:
Insert the correct syntax to add a placeholder for the age parameter.

Solution:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))




Question:
The statement below would print a Boolean value, which one?


Solution:
print(bool("abc"))

True



Question:
The statement below would print a Boolean value, which one?

Solution:
print(bool(0))

False



Question:

Use the insert method to add "lemon" as the second item in the fruits list.

Solution:
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")


Question:
Use the remove method to remove "banana" from the fruits list.


Solution:
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")


Question:
Use negative indexing to print the last item in the list.


Solution:

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])




Question:
Use a range of indexes to print the third, fourth, and fifth item in the list.

Solution:
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])


Question:

Use the correct syntax to print the number of items in the list.

Solution:

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#printing from a tuple, dictionary and a list are quite different 


Question:
Use the correct syntax to print the first item in the fruits tuple.

Solution:
fruits = ("apple", "banana", "cherry")
print(fruits[0])




Question:
Use the correct syntax to print the number of items in the fruits tuple.

Solution:
fruits = ("apple", "banana", "cherry")
print(len(fruits))

Question:
Use the add method to add "orange" to the fruits set.

Solution:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")





Question:
Use the correct method to add multiple items (more_fruits) to the fruits set.

Solution:
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)


Question:
Use the remove method to remove "banana" from the fruits set.

Solution:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")



Question:

Use the get method to print the value of the "model" key of the car dictionary.

Solution:
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get["model"])


Question:
Change the "year" value from 1964 to 2020.

Solution:
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["year"] = 2020


Question:
Add the key/value pair "color" : "red" to the car dictionary.

Solution:
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["color"] = "red"



Question:
Use the pop method to remove "model" from the car dictionary.

Solution:
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")



Question:
Use the clear method to empty the car dictionary.


Solution:
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()



Question:
Print "Hello World" if a is greater than b.

Solution:

a = 50
b = 10
if a > b:
  print("Hello World")


Question:
Print "Hello" if a is equal to b, or if c is equal to d.

Solution:

if a == b 
or
 c == d:
  print("Hello")



Question:
Print i as long as i is less than 6.




Solution:
i = 1
while i < 6:

  print(i)
  i += 1


Question:
Stop the loop if i is 3.


Solution:
i = 1
while i < 6:
  if i == 3:
    break
  i += 1


Question:

In the loop, when i is 3, jump directly to the next iteration.

Solution:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue

  print(i)


Question:
Print a message once the condition is false.


Solution:
i = 1
while i < 6:
  print(i)
  i += 1
else:

  print("i is no longer less than 6")



Question:
In the loop, when the item value is "banana", jump directly to the next item.


Solution:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    
continue

  print(x)



Question:
Exit the loop when x is "banana".


Solution:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    
break

  print(x)



Question:
If you do not know the number of arguments that will be passed into your function, 
there is a prefix you can add in the function definition, which prefix?


Solution:

def my_function(*kids):
  print("The youngest child is " + kids[2])


Question:

If you do not know the number of keyword arguments that will be passed into your function,
 there is a prefix you can add in the function definition, which prefix?



Solution:
def my_function(**kid):
  print("His last name is " + kid["lname"])

Question:

Create a lambda function that takes one parameter (a) and returns it.

Solution:

x = lambda a : a


Question:
Create a class named MyClass:


Solution:
class
 MyClass:
  x = 5


Question:
Create an object of MyClass called p1:

Solution:

class MyClass:
  x = 5

p1 = MyClass()


Question:
Use the p1 object to print the value of x:

Solution:

class MyClass:
  x = 5

p1 = MyClass()

print(p1.x)


Question:

What is the correct syntax to assign a "init" function to a class?


Solution:
class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age



Question:

What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?

Solution:

class Student(Person):


Question:

We have used the Student class to created an object named x.
What is the correct syntax to execute the printname method of the object x?

Solution:

class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


Question:
What is the correct syntax of printing all variables and function names of the "mymodule" module?


Solution:

import mymodule

print(dir(mymodule))