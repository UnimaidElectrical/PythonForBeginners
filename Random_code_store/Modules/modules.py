#Modules 

#Modules are pieces of code that other perople have written to fulfill common tasks, such as generating random numbers. Performing mathermatical operations.
#The basic way to use a module is to add import module_name at the top of your code, and then using module_name.var to access functions and values with 
# the name var in the module.

#Using the random module to generate random numbers

import random

for i in range(5):
    value = random.randint(1,6)
    print(value)

#The code uses the randint function defined in the random module to print 5 random numbers in the range 1 to 6


#There is another kind of import that can be used if you need only certain function from a module.
These take the form from module_name import var and then var can be used as if it were defined normally in your code.

Importing only the pi constant from the math module:


from math import pi 
print(pi)

#We can use a comma seperated list to import multiple objects
from math import pi,sqrt

#To import all the objects from a module. From math import *
#But this norm is normally frowned upon as it confuses all the variables in your code 
# with the variables of the external code module.

# You will get an import error if you try to import a mmodule that doesn't exist

import some_module

# you can also import a module under a different name by using the as keyword.
#this is mainly used when the a module or object has a long and very confusing name.

from math import sqrt as square_root
print(square_root(100))





