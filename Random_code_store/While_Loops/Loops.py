#Loops
#There always comes the need to perform code on each item in a list. We usually refer to this kind of action as an iteration. 
#This can be accomplished with a while loop and a counter variable.

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

