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


#What is the output of this code?
list1= {"blue","green"}
list2= {"green","blue"}
list1.add("black")
print(list((lambda x,y: x-y) (list1,list2))[0][2:])




#What is the output of this code?
def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)


# What is sum of the numbers printed by this code?
for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)


Fill in the blanks to swap the variable values with one single statement.

a = 7
b = 42
a,b = b,a


MAX_NUM=4

def main():
    for i in range (MAX_NUM):
        print(i, factorial(i))


def factorial(n):
    n = 1
    for i in range(n,n+1):
        return *=i
    return result

main()

****************************************8

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    return n

def main():
    n=42
    n=divide_and_round(n)
    print(int(n))

main()


''''''''''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            return
        '''''''''''      

            
            
class Solution(object):
    def moveZeroes(self, nums):
        i = count = 0
        while count < len(nums):
            if nums[i] == 0: nums.append(nums.pop(i))
            else: i += 1
            count += 1
    

'''''''''''       
#while 0 in nums:
            for i, num in enumerate(nums):
                if nums[i] == 0:
                    del nums[i]
                    t += 1         #keep track of the "0's" we delete
        for j in range(t):
            nums.append(0)      #add them back to the end of the array
'''''''''''''''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            
            else:
                i += 1






******************************************

Leetcode questions

******************************************

1, 
def rob(self, nums):
        n = len(nums)
        i=j=k=0
        for x in range(n):
            k=max(i + nums[x], j)
            i,j=j,k
        return j
rob(0,[2,7,9,3,1])


2, 
def moveZeroes(self, nums):
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] == 0: nums.append(nums.pop(i))
            else: i += 1
            count += 1
        #print(nums)
moveZeroes(0,[0,1,0,3,12])







L = [1,2,4,8,16,32,64]
x = 5
found = i = 0
while not found and i < len(L):
    if 2**x == L[i]:
        found = 1
    else:
        i +=1
    
    if found:
        print('at index', i)
    else:
        print(x, 'not found')

'''
Chapter Questions
Program logic alternatives. Consider the following code, which uses a while loop and found flag to search a list of powers of 2 for the value of 2 
raised to the fifth power (32). It’s stored in a module file called power.py.
'''
#Starter Code
L = [1, 2, 4, 8, 16, 32, 64] 
X= 5
found = False
i= 0
while not found and i < len(L):
    if 2 ** X == L[i]:
        found = True
    else:
        i = i+1
    if found:
        print('at index', i)
    else:
        print(X, 'not found')

'''
a. First, rewrite this code with a while loop else clause to eliminate the found flag and final if statement.
'''

L = [1, 2, 4, 8, 16, 32, 64] 
X= 5
i= 0
while i < len(L):
    if 2**X ==L[i]:
        print('Found at index',i,'the list number is: ', L[i])
    else:
        print('Not found!','at index',i,'the list number is: ',L[i])
    i+=1
    
'''
b. Next, rewrite the example to use a for loop with an else clause, to eliminate the explicit list-indexing logic. 
(Hint: to get the index of an item, use the list index method—L.index(X) returns the offset of the first X in list L.)
'''
L = [1, 2, 4, 8, 16, 32, 64] 

X= 5
j= 0
for i in range(j,7):
    powr= 2**j
    if powr == 2**X:
        print('Found at index',j,'the list number is: ', powr)
    else:
        print('Not found!','at index',j,'the list number is: ',powr)
    j+=1


c. Next, remove the loop completely by rewriting the example with a simple in operator membership expression. 
(See Chapter 8 for more details, or type this to test: 2 in [1,2,3].)

(x,y)
for 5 in [1,2,3,4,5,6]:
    for 

d. Finally, use a for loop and the list append method to generate the powers-of-2 list (L) instead of hardcoding a list literal.
Deeper thoughts:

e. Do you think it would improve performance to move the 2 ** X expression outside the loops? How would you code that?

f. As we saw in exercise 1, Python includes a map(function, list) tool that can generateapowers-of-2list,
too:map(lambda x: 2 ** x, range(7)).Trytyping this code interactively; we’ll meet lambda more formally in the next part of this book, 
especially in Chapter 19. Would a list comprehension help here (see Chapter 14)?




* allNumeric(arr): returns true if all items in arr are ints or floats, otherwise false

* removeNones(arr): returns arr without the None values in it
* reverse a list, given [5,4,3,2,1] return [1,2,3,4,5]

* turn ["a", "b", "c"] into "a,b,c" (turn a list of strings into one string separated by commas)

def ListToString(L):
    strings=","
    print(strings.join(L))
L=["a", "b", "c"]
ListToString(L)

    
* given a sorted list like [1,2,3,4,5] turn it in [5,1,4,2,3] (so interleave the list such that max value is first, then min, then second max, then second min, etc)
* multiplyItem(arr, i, x): given arr=["a","b","c"], i=0 and x=2, turn it into ["a", "a", "b", "c"] (multiply item at index i by x and insert in the same spot)
* divMod(a, b) return as a pair the division and modulo of a and b. for example: divMod(7, 3) should return (2, 1) because 2*3 + 1 = 7
* cross(a, b, c, d): a and b are strings, c and d are integers. given cross("foo", "bar", 2, 3), return "foofoobarbarbar"
* contains(arr, value): return True if value is in arr


* containsTwice(arr, value) return True of value is in arr at least two times

* containsN(arr, value, n): return True if value is in arr exactly N times


GivenVal = ["a","b","c","d","e","f","g","h","a","c","a","g","j","u","a","g","t","a"]
x=5
counting=''
for i in GivenVal:
    for j in GivenVal:
        if i == j:
            counting+=1
            print(counting)

