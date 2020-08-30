# Dictionaries are data structures used to map arbitrary keys to values.
# Lists can be thought of as dictionaries with integer keys within a certain range.
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# Each element in a dictionary is represented by a key:value pair.



# Dictionaries

# Trying to index a key that isn't part of the dictionary returns a KeyError.

primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}

print(primary["red"])
print(primary["yellow"])

# A dictionary can store any types of data as values.
# An empty dictionary is defined as {}.


# points to remember
# .....
# dictx = {}
# print(dictx[0])  #returns KeyError
# ....
# listx = []
# print(listx[])  # returns IndexError
# ....
# Good for debugging!!!



# Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be changed. So far, the only mutable objects you've come across are lists and dictionaries. Trying to use a mutable object as a dictionary key causes a TypeError.

bad_dict = {
  [1, 2, 3]: "one two three", 
}


# Just like lists, dictionary keys can be assigned to different values.
# 

squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[3] = 9
print(squares)


What is the result of this code?
primes = {1: 2, 2: 3, 4: 7, 7:17}
print(primes[primes[4]])

# primes[4] refers to the value (recall: each element of a Dictionary posses form Key:Value) 
# in the Dictionary primes that has its (unique identifier) Key as 4. Clearly, it follows that primes[4] refers to 7.
# Hence, primes[primes[4]] really refers to primes[7]. Following similar lines of thinking as above, it follows that primes[7] refers to 17. 
# Therefore, primes[primes[4]] really refers to primes[7] and hence refers to 17.
# So, print(primes[primes[4]]) is just print(17), giving output as just 17 clearly.



# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

nums = {
  1: "one",
  2: "two",
  3: "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)



