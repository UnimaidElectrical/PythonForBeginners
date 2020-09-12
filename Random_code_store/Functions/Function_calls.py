


def f(a, b, c): 
    print(a, b, c)      #printing the results to screen

f(1, 2, 3)              #Calling the function

f(c=3, b=2, a=1)        #Using Keywords for function calls

f(1, c=3, b=2)          #a gets 1 by position, b and c passed by name

#New function with constants

def f(a, b=2, c=3):        # a required, b and c optional for a function call
    print(a, b, c)

f(1)                       # Use defaults will give you predefined answers 

f(a=1)                     # making a the default

f(1, 4)                    # Override defaults. This will change the first two arguements

f(1, c=6)                  # Choose defaults. This will choose the defaults for the specified object



#Arbitrary Arguments Examples

#Headers: Collecting arguments

def f(*args):                  #this collects all the arguments in the function call
    print(args)

f()
f('aa',3.984, [4,6,2],{e=9,f=0})                            #all arguments here will be accepted in the fnction 


def f(**args):     # ** feature is similar, but it only works for keyword arguments (key value pairs)
    print(args)

#f()
f(e=9,f=0)         # 