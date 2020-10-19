#Loops
#There always comes the need to perform code on each item in a list. We usually refer to this kind of action as an iteration. 
#This can be accomplished with a while loop and a counter variable.
from numpy import append

words=["hello","world","spam","eggs"]
counter=0
max_index=len(words) - 1

while counter <= max_index:
    word=words[counter]
    print(word+ "!")
    counter=counter+1

#The code above iterates through all items in the list, accesses them using their indices and prints them with exclamation marks.
#The loops construct can be used to iterate through a list

#For Loops and Range

#The for loop is commonly used to repeat some code a certain number of times. This is done by combining for loops with range objects.

for i in range(5):
    print("hello")

#You don't need to call list on the range object when it it used in a for loop, because it isin't indexed, so a list isin't required.


#This will print all the even numbers in the range
for i in range(0,20,2):
    print(i)






 “Truthy” AnD “Falsey” Values
'''
There are some values in other data types that conditions will consider equiva- lent to True and False . When used in conditions, 0, 0.0, and '' (the empty string) are considered False, while all other values are considered True . For example, look at the following program:
'''

name = ''
while not name:
    print('Enter your name:')
    name = input()
    print('How many guests will you have?') numOfGuests = int(input())
    if numOfGuests:
        print('Be sure to have enough room for all your guests.')
print('Done')

 '''
If the user enters a blank string for name, then the while statement’s condition will be True u, and the program continues to ask for a name . If the value for numOfGuests is not 0 v, then the condition is considered to be True, and the program will print a reminder for the userw .
You could have typed not name != '' instead of not name, and numOfGuests != 0 instead of numOfGuests, but using the truthy and falsey values can make your code easier to read:
'''



#Python if else, for loop, and range() Exercise with Solutions
'''
Question 1: Print First 10 natural numbers using while loop
'''
i=0
while True:
    for i in range(0,11):
        print(i)
        i+=1
    break

'''
Question 2: Print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
Solution:
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")


print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    print("row " + str(row))
    for column in range(1, row + 1):
        print("col " + str(column))
        #print(column, end=' ')
    print("")




'''
Question 3: Accept number from user and calculate the sum of all number between 1 and given number
For example user given 10 so the output should be 55
'''

solution:
sums=0
fac=int(input("Please enter a number "))
for i in range(1,fac+1,1):
    sums+=i
print(sums)


sum1 = 0
n = int(input("Please enter number "))
for i in range(1, n + 1, 1):
    sum1 += i
print("\n")
print("Sum is: ", sum1)


Question 4: Print multiplication table of given number
For example num = 2 so the output should be

for i in range(1,11):
    print(i*2)




n = 2
for i in range(1, 11, 1):
    product = n*i
    print(product)




'''
Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

Expected output:

15
55
75
150
'''
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for item in list1:
    if (item > 150):
        break
    if(item % 5 == 0):
        print(item)


list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i%5==0 and i<=150:
        print(i)


'''
Question 6: Given a number count the total number of digits in a number
For example, the number is 75869, so the output should be 5.
'''
num = 78345353543547510
count = 0
while num!=0:
    num//=10
    count+=1
print(count)

'''
Question 7: Print the following pattern using for loop
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''

#numbers=5
for j in range(5,0,-1):
    #print(j)
    for i in (1,j+1):
        #print(i)
        print(i, end=' ')
    print(" ")


n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
