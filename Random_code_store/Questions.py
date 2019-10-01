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




