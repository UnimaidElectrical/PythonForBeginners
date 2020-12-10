Common Python Built-in Functions
******************************************************************
Index
******

Python abs()
Python any()
Python all()
Python ascii()
Python bin()
Python bool()
Python bytearray()
Python callable()
Python bytes()
Python chr()
Python compile()
Python classmethod()
Python complex()
Python delattr()
Python dict()
Python dir()
Python divmod()
Python enumerate()
Python staticmethod()
Python filter()
Python eval()
Python float()
Python format()
Python frozenset()
Python getattr()
Python globals()
Python exec()
Python hasattr()
Python help()
Python hex()
Python hash()
Python input()
Python id()
Python isinstance()
Python int()
Python issubclass()
Python iter()
Python list() Function
Python locals()
Python len()
Python max()
Python min()
Python map()
Python next()
Python memoryview()
Python object()
Python oct()
Python ord()
Python open()
Python pow()
Python print()
Python property()
Python range()
Python repr()
Python reversed()
Python round()
Python set()
Python setattr()
Python slice()
Python sorted()
Python str()
Python sum()
Python tuple() Function
Python type()
Python vars()
Python zip()
Python __import__()
Python super()

******************************************************************
%%%###:::
----->         abs()     <--------
######
The abs() method returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.

The syntax of abs() method is:

abs(num)

abs() Parameters
################
abs() method takes a single argument:

num - a number whose absolute value is to be returned. The number can be:
integer
floating number
complex number


Return value from abs()
#########################

abs() method returns the absolute value of the given number.

For integers - integer absolute value is returned
For floating numbers - floating absolute value is returned
For complex numbers - magnitude of the number is returned




Example 1: Get absolute value of a number
# random integer
integer = -20
print('Absolute value of -20 is:', abs(integer))

#random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))
Output

Absolute value of -20 is: 20
Absolute value of -30.33 is: 30.33
Example 2: Get magnitude of a complex number
# random complex number
complex = (3 - 4j)
print('Magnitude of 3 - 4j is:', abs(complex))
Output

Magnitude of 3 - 4j is: 5.0



%%%###:::
----->         any()     <--------

The any() function returns True if any element of an iterable is True. If not, any() returns False.

The syntax of any() is:

any(iterable)

Parameters for the any() function
#########################
-> The any() function takes an iterable (list, string, dictionary etc.) in Python.

Value Returned by the any() function
##################################################
The any() function returns a boolean value:



True if at least one element of an iterable is true : THis can signify an OR logical operation
False if all elements are false or if an iterable is empty
Condition	Return Value
All values are true	True
All values are false	False
One value is true (others are false)	True
One value is false (others are true)	True
Empty Iterable	False




Example 1: Using any() on Python Lists
# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))
Output

True
False
True
False



The any() method works in a similar way for tuples and sets like lists.
##################################################

Example 2: Using any() on Python Strings
# Atleast one (in fact all) elements are True
s = "This is good"
print(any(s))

# 0 is False
# '0' is True since its a string character
s = '000'
print(any(s))

# False since empty iterable
s = ''
print(any(s))
Output

True
True
False



Example 3: Using any() with Python Dictionaries
In the case of dictionaries, if all keys (not values) are false or the dictionary is empty, any() returns False. If at least one key is true, any() returns True.

# 0 is False
d = {0: 'False'}
print(any(d))

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))

# iterable is empty
d = {}
print(any(d))

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))
Output

False
True
False
False
True



%%%###:::
----->         all()     <--------

The all() method returns True when all elements in the given iterable are true. If not, it returns False.


The syntax of all() method is:
all(iterable)


all() Parameters
##################################################
all() method takes a single parameter:

-> iterable - any iterable (list, tuple, dictionary, etc.) which contains the elements



Return Value from all()
all() method returns:

True - If all elements in an iterable are true
False - If any element in an iterable is false
Truth table for all()
When	Return Value
All values are true	True
All values are false	False
One value is true (others are false)	False
One value is false (others are true)	False
Empty Iterable	True



Example 1: How all() works for lists?
# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))
Output

True
False
False
False
True


any() method works in a similar way for tuples and sets like lists.

Example 2: How all() works for strings?
s = "This is good"
print(all(s))

# 0 is False
# '0' is True
s = '000'
print(all(s))

s = ''
print(all(s))
Output

True
True
True





%%%###:::
----->         ascii()     <--------

The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using \x, \u or \U escapes.


The syntax of ascii() is:

ascii(object)


ascii() Parameters
##################################################
ascii() method takes an object (like: strings, list etc).


Return Value from ascii()
##################################################
It returns a string containing a printable representation of an object.

For example, ö is changed to \xf6n, √ is changed to \u221a

The non-ASCII characters in the string are escaped using \x, \u or \U.




Example 1: How ascii() method works?
normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

Output
'Python is interesting'
'Pyth\xf6n is interesting'
Pythön is interesting


More Examples
randomList = ['Python', 'Pythön', 5]
print(ascii(randomList))
randomTuple = ('python', 'Pythön', 5)
print(ascii(randomTuple))

Output
['Python', 'Pyth\xf6n', 5]
('python', 'Pyth\xf6n', 5)


0000 1
0001 2
0010 3
0011 4
0101 5




%%%###:::
----->         bin()     <--------

The bin() method converts and returns the binary equivalent string of a given integer.
If the parameter isn't an integer, it has to implement __index__() method to return an integer.



The syntax of bin() method is:

bin(num)


bin() Parameters
##################################################

bin() method takes a single parameter:

num - an integer number whose binary equivalent is to be calculated.
If not an integer, should implement __index__() method to return an integer.




Return value from bin()
##################################################
bin() method returns the binary string equivalent to the given integer.

If not specified an integer, it raises a TypeError exception highlighting the type cannot be interpreted as an integer.




Example 1: Convert integer to binary using bin()
number = 5
print('The binary equivalent of 5 is:', bin(number))

Output
The binary equivalent of 5 is: 0b101

The prefix 0b represents that the result is a binary string.





Example 2: Convert an object to binary implementing __index__() method


class Quantity:
    apple = 1
    orange = 2
    grapes = 2

    def __index__(self):
        return self.apple + self.orange + self.grapes


print('The binary equivalent of quantity is:', bin(Quantity()))


Output
The binary equivalent of quantity is: 0b101


Here, we've sent an object of class Quantity to the bin() method.

bin() method doesn't raise an error even if the object Quantity is not an integer.

This is because we have implemented the __index__() method which returns an integer (sum of fruit quantities).
This integer is then supplied to the bin() method.







%%%###:::
----->         bool()     <--------

The bool() method converts a value to Boolean (True or False) using the standard truth testing procedure.


The syntax of bool() is:
##################################################
bool([value])


bool() parameters
##################################################
It's not mandatory to pass a value to bool(). If you do not pass a value, bool() returns False.

In general use, bool() takes a single parameter value. 
bool can take a string, int, float, list, tuple or dict



Return Value from bool()
bool() returns:

False if the value is omitted or false
True if the value is true


-> The following values are considered false in Python:

None
False
Zero of any numeric type. For example, 0, 0.0, 0j
Empty sequence. For example, (), [], ''.
Empty mapping. For example, {}
objects of Classes which has __bool__() or __len()__ method which returns 0 or False
All other values except these values are considered true.


Example: How bool() works?
test = []
print(test,'is',bool(test))

test = ()
print(test,'is',bool(test))

test = {}
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))

Output
[] is False
() is False
{} is False
[0] is True
0.0 is False
None is False
True is True
Easy string is True


%%%###:::
----->         bytearray()     <--------

The bytearray() method returns a bytearray object which is an array of the given bytes.



The syntax of bytearray() method is:
##################################################
bytearray([source[, encoding[, errors]]])

bytearray() method returns a bytearray object which is mutable (can be modified) 
sequence of integers in the range 0 <= x < 256.

If you want the immutable version, use bytes() method.


bytearray() Parameters
bytearray() takes three optional parameters:

source (Optional) - source to initialize the array of bytes.
encoding (Optional) - if the source is a string, the encoding of the string.
errors (Optional) - if the source is a string, the action to take when the encoding conversion fails.



The source parameter can be used to initialize the byte array in the following ways:

Different source parameters
Type	Description
String	Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
Integer	Creates an array of provided size, all initialized to null
Object	A read-only buffer of the object will be used to initialize the byte array
Iterable	Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
No source (arguments)	Creates an array of size 0.


Return value from bytearray()
##################################################
bytearray() method returns an array of bytes of the given size and initialization values.

Example 1: Array of bytes from a string

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)

Output
bytearray(b'Python is interesting.')



Example 2: Array of bytes of given integer size
size = 5

arr = bytearray(size)
print(arr)

Output
bytearray(b'\x00\x00\x00\x00\x00')



Example 3: Array of bytes from an iterable list
rList = [1, 2, 3, 4, 5]

arr = bytearray(rList)
print(arr)
Output

bytearray(b'\x01\x02\x03\x04\x05')




%%%###:::
----->         callable()     <--------

The callable() method returns True if the object passed appears callable. If not, it returns False.


The syntax of callable() is:

callable(object)


callable() Parameters
callable() method takes a single argument object.



Return value from callable()
##################################################
callable() method returns:

True - if the object appears callable
False - if the object is not callable.
It important to remember that, even if callable() is True, call to the object may still fail.

However, if callable() returns False, call to the object will certainly fail.


Example 1: How callable() works?
x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))
Output

False
True


Here, the object x is not callable. And, the object y appears to be callable (but may not be callable).



Example 2: Callable Object 
class Foo:
  def __call__(self):
    print('Print Something')

print(callable(Foo))
Output

True
The instance of Foo class appears to be callable (and is callable in this case).

class Foo:
  def __call__(self):
    print('Print Something')

InstanceOfFoo = Foo()

# Prints 'Print Something'
InstanceOfFoo()





Example 3: Object Appears to be Callable but isn't callable.
class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))


Output
True




The instance of Foo class appears to be callable but it's not callable. The following code will raise an error.

class Foo:
  def printLine(self):
    print('Print Something')

print(callable(Foo))

InstanceOfFoo = Foo()
# Raises an Error
# 'Foo' object is not callable
InstanceOfFoo()


Output
True

Traceback (most recent call last):
File "", line 10, in 
TypeError: 'Foo' object is not callable







%%%###:::
----->         bytes()     <--------
The bytes() method returns a immutable bytes object initialized with the given size and data.

The syntax of bytes() method is:
##################################################

bytes([source[, encoding[, errors]]])
bytes() method returns a bytes object which is an immutable (cannot be modified) sequence of integers in the range 0 <=x < 256.

If you want to use the mutable version, use bytearray() method.



bytes() Parameters
##################################################
bytes() takes three optional parameters:

source (Optional) - source to initialize the array of bytes.
encoding (Optional) - if the source is a string, the encoding of the string.
errors (Optional) - if the source is a string, the action to take when the encoding conversion fails.
The source parameter can be used to initialize the byte array in the following ways:

Different source parameters
Type	Description
String	Converts the string to bytes using str.encode() Must also provide encoding and optionally errors
Integer	Creates an array of provided size, all initialized to null
Object	A read-only buffer of the object will be used to initialize the byte array
Iterable	Creates an array of size equal to the iterable count and initialized to the iterable elements Must be iterable of integers between 0 <= x < 256
No source (arguments)	Creates an array of size 0
Return value from bytes()
The bytes() method returns a bytes object of the given size and initialization values.




Example 1: Convert string to bytes
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)
Output

b'Python is interesting.'



Example 2: Create a byte of given integer size
size = 5

arr = bytes(size)
print(arr)
Output

b'\x00\x00\x00\x00\x00'



Example 3: Convert iterable list to bytes
rList = [1, 2, 3, 4, 5]

arr = bytes(rList)
print(arr)
Output

b'\x01\x02\x03\x04\x05'



%%%###:::
----->         chr()     <--------
The chr() method returns a character (a string) from an integer (represents unicode code point of the character).


The syntax of chr() is:

chr(i)


chr() Parameters
##################################################
chr() method takes a single parameter, an integer i.

The valid range of the integer is from 0 through 1,114,111.


Return Value from chr()
##################################################
chr() returns:

a character (a string) whose Unicode code point is the integer i
If the integer i is outside the range, ValueError will be raised.

Example 1: How chr() works?
print(chr(97))
print(chr(65))
print(chr(1200))
Output

a
A
Ұ


Example 2: Integer passed to chr() is out of the range
print(chr(-1))
Output

Traceback (most recent call last):
File "", line 1, in 
ValueError: chr() arg not in range(0x110000)
When you run the program, ValueError is raised.

It's because the argument passed to chr() method is out of the range.

The reverse operation of chr() function can be performed by ord() function. To learn more, visit Python ord() function












******************************************************************
Short Description 
******************************************************************


Python abs()
returns absolute value of a number

Python all()
returns true when all elements in iterable is true

Python any()
Checks if any Element of an Iterable is True

Python ascii()
Returns String Containing Printable Representation

Python bin()
converts integer to binary string

Python bool()
Converts a Value to Boolean

Python bytearray()
returns array of given byte size

Python bytes()
returns immutable bytes object

Python callable()
Checks if the Object is Callable

Python chr()
Returns a Character (a string) from an Integer

Python classmethod()
returns class method for given function

Python compile()
Returns a Python code object

Python complex()
Creates a Complex Number

Python delattr()
Deletes Attribute From the Object

Python dict()
Creates a Dictionary

Python dir()
Tries to Return Attributes of Object

Python divmod()
Returns a Tuple of Quotient and Remainder

Python enumerate()
Returns an Enumerate Object

Python eval()
Runs Python Code Within Program

Python exec()
Executes Dynamically Created Program

Python filter()
constructs iterator from elements which are true

Python float()
returns floating point number from number, string

Python format()
returns formatted representation of a value

Python frozenset()
returns immutable frozenset object

Python getattr()
returns value of named attribute of an object

Python globals()
returns dictionary of current global symbol table

Python hasattr()
returns whether object has named attribute

Python hash()
returns hash value of an object

Python help()
Invokes the built-in Help System

Python hex()
Converts to Integer to Hexadecimal

Python id()
Returns Identify of an Object

Python input()
reads and returns a line of string

Python int()
returns integer from a number or string

Python isinstance()
Checks if a Object is an Instance of Class

Python issubclass()
Checks if a Class is Subclass of another Class

Python iter()
returns an iterator

Python len()
Returns Length of an Object

Python list()
creates a list in Python

Python locals()
Returns dictionary of a current local symbol table

Python map()
Applies Function and Returns a List

Python max()
returns the largest item

Python memoryview()
returns memory view of an argument

Python min()
returns the smallest value

Python next()
Retrieves next item from the iterator

Python object()
creates a featureless object

Python oct()
returns the octal representation of an integer

Python open()
Returns a file object

Python ord()
returns an integer of the Unicode character

Python pow()
returns the power of a number

Python print()
Prints the Given Object

Python property()
returns the property attribute

Python range()
return sequence of integers between start and stop

Python repr()
returns a printable representation of the object

Python reversed()
returns the reversed iterator of a sequence

Python round()
rounds a number to specified decimals

Python set()
constructs and returns a set

Python setattr()
sets the value of an attribute of an object

Python slice()
returns a slice object

Python sorted()
returns a sorted list from the given iterable

Python staticmethod()
transforms a method into a static method

Python str()
returns the string version of the object

Python sum()
Adds items of an Iterable

Python super()
Returns a proxy object of the base class

Python tuple()
Returns a tuple

Python type()
Returns the type of the object

Python vars()
Returns the __dict__ attribute

Python zip()
Returns an iterator of tuples

Python __import__()
Function called by the import statement




