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
