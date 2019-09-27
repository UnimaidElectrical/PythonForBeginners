#List Functions
#A very good way to alter a list is to use the append method. This basically adds an iten ti the end of an existing list.

nums=[1,2,3]
nums.append(4)
print(nums)

#The dot before append is there because it is a method of the list's class

#Using Len 
# To get the number of items in a list, you can use the len function
nums=[1,3,5,2,4]
print(len(nums))


#Unlike append, len is a normal function, rather than a method. This means that it is written before the list is being called upon without the use of a dot.

letters=["a","b","c"]
letters.append("d")
print(len(letters))

#The insert method is similar to append, except that it allows you to insert a new item at any position in the listas opposed to just at the end
words=["python","fun"]
index=1
words.insert(index,"is")
print(words)

#here it is a must to declear the index and then assign it to the proper location.
#Example
nums=[9,8,7,6,5]  # list with 5 elements
nums.append(4)  #appends the number 4 to the end of the list (count currently 6 characers)
nums.insert(2,11) #puts number 11 on the second position (count currently 7 characers)
print(len(nums))  #used to print the count of characters in the nums variable
# here we have used the insert in a differnt way, instead of seperately declearing it we have consolidated it into one line.


#The index method finds the first occurence of a list item and returns it's index. It also raises a Value Error if the item is not on the list.

letters=['p','q','r','s','p','u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('z'))


#Other very useful functions to consider:
#max(list):Returns the list with the maximum value
#min(list):Returns the list with the minimum value
#list.count(obj):Returns a count of how many times an item occures in a list
#list.remove(obj): Removes an object from a list 
#list.reverse(): Reverses objects in a list 
