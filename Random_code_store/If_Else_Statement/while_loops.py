#thie code takes you through the process it takes to run a while loop


i = 0

numbers = []

while i < 6:
    print(f"A the top i is {i}")
    numbers.append(i)


    i = i + 1

    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)

print(numbers)


#code to print all even numbers
x=10
while x:
    x-=1
    if x % 2 != 0: continue
    print(x)


while True:
    name = input('Enter name: ')
    if name == 'stop': break
    age = int(input('Enter Age: '))  # You can have the int on theis line  
    print('Hello' , name, '=>',  int(age)**2) # or on this line. # you can also choose to use commas 
    #print('Hello' + name + 'of names' '=>'+  int(age)**2) # you may run into issues using concartinate here. As python only concartinates strings not int

************************************************

y = int(input('Enter your Number here: '))
#m = y / 2
m=10
while m>1:
    if y % m == 0:
        print(y, 'has factor', m)
        break
    x -= 1
else:
    print(y, 'is prime')


#or this as well

y = int(input('Enter your Number here: ')); x = y / 2
while x>1:
    if y % x ==0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')



found = 0
while x and not found:
    if match(x[0]):
        print 'Ni'
        found = 1
    else:
        x = x[1:]
    if not found:
        print 'not found'



#sum
sum = 0
for x in [1,2,3,4]:
  sum +=x
print(sum)

#multiplication
prod = 1
for x in [1,2,3,4]:
  prod *=x
print(prod)

#declearing two variables in a one line 
#and the methods to call them

S, T = "lumberjack", ("and", "I'm", "okay")

for x in S:
    print(x) 

for x in T:
    print(x)        



#This loops through an ordered list and prints out 
#the list in the same format it was represented in.
T = [(1,2),(3,4),(5,6)]
for (i,j) in T:
    print (i,j)




'''
This block of test case will be alot different from the next one.
in this one, it completely loops through the first list before matching with the second list
it is always advisable to use the list of more priority
'''
items = ['aaa', 111, (4,5), 2.01]
tests = [(4,5), 3.14]
for key in items:
    for test in tests:
        if test==key:
            print(key,'key found')
            break
    else:
        print(key,'Key was not found!')



'''
In this block we have a shorter set, it almost feels like a left join
'''
tests = [(4,5), 3.14]
items = ['aaa', 111, (4,5), 2.01]
for test in tests:
    for key in items:
        if key==test: # the order doesn't matter here
            print(key,'key found')
            break
    else:
        print(key,'Key was not found!')



'''
Here we have a direct comparison where the elements of the smaller list 
is compared with the elements of the other list one at a time.
'''
tests = [(4,5), 3.14]
items = ['aaa', 111, (4,5), 2.01]
for key in tests:
    if key in items:
        print(key, "Was Found")
    else:
        print(key,'Not Found!')


'''
This code checks for for simarities between the two strings and appended to a list
'''
seq1 = 'sp1akh6m'
seq2 = 's6ch1a7m'

res = [] # Starting with an empty string
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)  #The result of the comes as a list because of the append construct ['s','a','m']



item = 'spam'
for x in item:
    print(x,)

'''
the output of this will be 
s
p
a
m
'''


#While Loop Iteration
'''
Using the while loop to transverse through the string while expecting another input 
'''
x='spam'
i = 0
while i < len(x):
    print(x[i]),;
    i+=1


'''
using the for loop to go through the string, quite similat to the while loop
'''
x='spam'
for i in range(len(x),):
    print(x[i])


x='spam'
len(x)
list(range(len(x)))

for i in range(len(x)):
    print(x[i])


S = 'abcdefghijk'
list(range(0,len(S),2))

for i in range(0, len(S), 2):
    #print(S[i])
    print(i)


for i in range(0, len(S), 2): #This has stipulated the values that needs to be selected and how far it should go 
    print(S[i])

for x in S[::2]: print(x) #This means the same with the upper code as it is taking in the defaults for inbetween the columns



#This line prints all the indexes and the object contents
for i in range(0, len(S), 2):
    print(S[i],i)
    #print(i)


'''
print(*a, sep = ", ")  # print() argument after * must be an iterable, not int

a = [1, 2, 3, 4, 5] 
print(' '.join(map(str, a))) 
'''


#Changing Lists: range


pi=['a','b','c','d','e','f']
abi=[]
for i in pi:#list(range(len(pi))):
    abi.append(i)
print(abi)


********************
L = [1,2,3,4,5]
#L=['a','b','c','d','e','f']
for i in range(len(L)):
    L[i]+=1
L
    #print(L[i])


i = 0
while i < len(L):
    L[i] +=1
    i+=1
L

#Parallel Transverse: zip and map
L1 = [1,2,3,4]
L2 = [5,6,7,8]
concatn=zip(L1,L2)
list(concatn)   # this can be switched between Dictionary or List

for (x,y) in zip(L1,L2): # this iterates through the list already made in the zip operation
    print(x,'+',y, '-->',x+y)



T1,T2,T3= (1,2,3,10),(4,5,6,11),(7,8,9)
T3
concatnn=zip(T1,T2,T3)
list(concatnn)
'''
The results here will yield:
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
remember it is taking the very first element from all of the decleared lists
what this also does is that it truncates the missing objects in a list that doesn't match with the others
'''


s1='abc'
s2='xyz123'
list(zip(s1,s2))
m=map(None,s1,s2)  #I'm not too sure why this doesn't work pls debug
m



#Dictionary construction with zip

D1 = {'spam':1,'eggs':2,'toast':5}
D1

D1 = {}
D1['spam'] = 2
D1['eggs'] = 4
D1['toast'] = 6

D1

keys = ['spam','eggs','toast']
vals = [7,8,9]

list(zip(keys,vals))

D2 = {}
for k,v in zip(keys,vals): # same as (k,v) 
    D2[k] = v  # what this is doing here is to associate the keys to the value pairs
D2


keys = ['spam', 'eggs','toast']
vals = [11,12,13]
D3 = dict(zip(keys,vals))
D3

