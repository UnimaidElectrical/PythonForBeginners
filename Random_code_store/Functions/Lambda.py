'''
Lambda's general form is the jeyword, followed by one or more arguments
(this will be exactly like the arguments list you enclose in parenthesis in a def header)
followed by an expression after a colon:

lambda argument1, argument2,.... argumentN : expession using arguments

'''

def func(x,y,z):
    return x + y + z
    
func(2,3,4)

f = lambda x, y, z: x + y + z
f(2,3,4)


x = (lambda a="fee", b="fie", c="foe": a + b + c)
x('wee')


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

#knights()    #This will not work here as the function is not expecting any arguments to be passed this way

act=knights()   # we have to first assign the call to an object before calling it with an argument
act('robin')    #Calling the assigned object with the argument.



'''
Lambdas are commonly used to code jump tables - lists or dictionaries of actions to be performed on demand
Using Lists
'''

L = [(lambda x: x**2),(lambda x: x**3), (lambda x: x**4)]   # This takes in a list in here

for funcs in L:
    print(funcs(2))        #Prints 4, 8, 16

print(L[0](3))    #This targets the first item in the list and then parses the argument #Answer should be 9




'''
Using Dictionaries and lambda
'''

key = 'got'
{'already': (lambda: 2 + 2),
 'got': (lambda: 2 * 4),
 'one': (lambda: 2 ** 6)
 }[key]()



def ifelse(a,b,c):
    return ((a and [b]) or [c])[0]

ifelse(1, 'spam', 'ni')

ifelse(0,'spam','ni')