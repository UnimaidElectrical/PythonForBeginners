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

