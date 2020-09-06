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
m = y / 2
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
