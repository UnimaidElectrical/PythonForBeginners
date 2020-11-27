

#Enumerating a List
#With the help of Python enumerate function, we can iterate over the index and value in a Python list by using a basic for loop. Let us see how:

List = [“Red”, “Green”, “Black”, “Blue”]
for i, j in enumerate(List):
print(i, j)

'''
Output:
0 Red
1 Green
2 Black
3 Blue
'''

#Using Enumerate with Dictionary
#with enumerate, we can create a Python Dictionary out of a list very easily

all_lists = ['About','Automatically','switching','between','devices','Quick','access','Seamless','connected','comfortable']
Dict = dict(enumerate(all_lists))
print(Dict)
'''
Output:
{0: 'About', 1: 'Automatically', 2: 'switching', 3: 'between', 4: 'devices', 5: 'Quick', 6: 'access', 7: 'Seamless', 8: 'connected', 9: 'comfortable'}
'''


List = ["Red", "Green", "Black", "Blue"]
Dict= dict(enumerate(List))
print(Dict)
'''
Output:
{0: ‘Red’, 1: ‘Green’, 2: ‘Black’, 3: ‘Blue’}
'''


#Enumerating a Tuple
#Just the way we performed enumerate Python in a list, we can enumerate a Python tuple. Let us try this out with a simple example.

List = ["Red", "Green", "Black", "Blue"]
for i, j in enumerate(List):
print(i, j)

'''
Output:
0 Red
1 Green
2 Black
3 Blue
'''


#Enumerating a List of Tuples

List1 = [(10,"Red"), (5,"Green"), (8,"Black"),(2,"Blue")]
for idx, (count, color) in enumerate(List1):
print(idx, count, color)

'''
Output:
0 10 Red
1 5 Green
2 8 Black
3 2 Blue
'''

List1 = [(10,"Red"), (5,"Green"), (8,"Black"),(2,"Blue")]
for i, (j,k) in enumerate(List1):
    print(i,j,k)
    print(i, [j, k])
    print(i, (j, k))
#The print statement here shows that the output can be represented in whatever format that pleases the author




#Enumerating a String

String = "Python"
for i, j in enumerate(String):
print(i, j)

'''
Output:
0 P
1 y
2 t
3 h
4 o
5 n
'''




#Enumerating from a Specific Index
#Let us view how to enumerate from a specific index and not from index 0 with the help of an example.

String = "Python"
for i, j in enumerate(String, 1):
print(i, j)

'''
Output:
1 P
2 y
3 t
4 h
5 o
6 n
'''



