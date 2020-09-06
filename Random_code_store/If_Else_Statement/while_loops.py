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




seq1 = 'sp1akh6m'
seq2 = 's6ch1a7m'

res = [] # Starting with an empty string
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)


