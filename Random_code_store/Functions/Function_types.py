Nested Functions

def f1():
  x = 88
  def f2():
    print(x)
  f2()
f1()       # prints 88



# called a closure as it remembers the values of the enclosing scopes even though the scopes are not around anymore
def f1():
    x = 88
    def f2():
        print(x)
    return f2
action = f1()   #Make, return function
action()        # Call it now: prints 88


#Using Default Arguement Values
def f1():
    x=88
    def f2(x=x):  # Here the arguement will default to the value of x in the enclosing scope
        print(x)
    f2()
f1()   prints 88

'''
Notice that it is okay to call a function defined after the one that contains the call like this
as long as the second def runs before the call of the first function- the code inside the dev is 
never evaluated until the function is actually called.
'''

def f1():
    x = 88
    f2(x)

def f2(x):
    print (x)
f1()



#The Global Statement

y,z = 1,2
def all_global():   #the arguments here should be left as blank. if you have arguemrnts here it will be that they 
                    #were already assigned before being used in the function itself
    global xp
    xp = y + z
all_global()
print(xp)



#Global Assignments and function calls
xm,ym = 'pack','man'
#xrm=yrm=200
def al_global(xm,ym):
    global
    doo = xm + ym
xrm=6
yrm=1
xrm,yrm = al_global(5,3)
print(xrm,yrm)
print(doo)


#xp,y = all_global(1,2)





def func():
    global mani
    mani = 99
func()
print(mani)


def func():
    x = 4
    action = (lambda n: x ** n)   # x in enclosing def
    return action
x = func()
print(x(4))


# Here python will search all the enclosing defs after the referencing function's local scope and before the module global scope.
def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()
f1()


#Arguments and Shared References

def changer(x,y):       #Function
    x = 2               #Changes local name value only
    y[0] = 'spam'       #Changes shared object in place 

x = 1                   
L = [1,2]               #caller
changer(x,L)            #Pass immutable and mutable
x,L                     # x is unchanged, L is different #vs print(x,L) #This prints the output without the parenthesis



def changer(x,y):
    y = y[:]
    x = 2
    y[0] = 'spam'
    return x,y  # for this instance we see that the return statement and print statement are the same.
    print(x,y)
changer(1,[3,5,7])


L = [1,2]
changer(x, tuple(L))   #This will throw up an error because Tuples are immutable 




#Stimulating output parameters

def multiple(x,y):
    x = 2
    global 
    y = [3,4]
    return(x,y)
x = 1
L = [1,2]               # Assignment 
x, y = multiple(x,y)
#x, L = multiple(x,L)    # Assign results to caller's names
x, L 
x,y

