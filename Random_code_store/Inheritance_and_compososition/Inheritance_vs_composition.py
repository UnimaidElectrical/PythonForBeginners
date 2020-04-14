# What is Inheritance:
# Inheritance is used to indicate that one class will get the most of all its 
# features from a parent class.
# this happens implicitly whenever you write 
class Foo(Bar):
# which says "Make a class Foo that inherits from Bar."
# when this is done any actio that you do on instances of FOO will also work as if they were done
# to a instance of bar. Doing this lets you put common functionality in the Bar class,
# then specialize that functionality in the Foo class as needed.

# When doing this kind of specialization, there are three ways in which the parent and 
# child classes can interact:

# 1, Actions on the clild can IMPLY an action on the parent.

# 2, Actions on the child OVERRIDE the action on the parent.

# 3, Actions on the child can ALTER the action on the parent.


#IMPLICIT INHERITANCE:
# Here we define a function in the parent but not in the child.
# hence the child inherits everything from the parent.

class Parent(object):

    def implicit(sel:
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Clild()

dad.implicit()
son.implicit()



# OVERRIDE EXPLICITLY:
# to override the function in the child class effectively, we do this 
# by replacing the function in the child domain bu the same name.


class Parent(object):

    def override (self):
        print("PARENT override()")
    
class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()




#ALTER BEFORE OR AFTER
# To alter the behavior before and the Parent class. The first thing to do is to override the function.
# the python in-built function called SUPER is used to get the parentt version to call 



class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD,AFTER PARENT altered()")

dad = Parent(
son = Child()


dad.altered()
son.altered()


# 1, Overwriting the Parent.altered with the Child.altered 

# 2, calling super(Child,self).altered() which is aware of the Inheritance and will get the parent class for you.
# this should be interprieted as "call super with arguments Child and self, then call the function altered on whatever it returns."




# Inheritance, Overide and Altered 

class Parent(object):

    def override(self):
        print("PARENT override()")
    
    def implicit(self):
        print("PARENT implicit()")
    
    def altered(self):
        print("PARENT altered()")

class Child (Parent):

    def override(self):
        print("CHILD override()")

    def altered (self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child,self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.override()
son.override()

dad.altered()
son.altered()

dad.implicit()
son.implicit()