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






