'''In object oriented programming, you write classes that represent real-world things and situations
and you create objects based on these classes.
when you write a class, you define the general behavior that a whole category can have'''
'''
#Creating the dog class
class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Stimulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years Old.")
my_dog.sit()
my_dog.roll_over()

print(":::::::::::::::::::::::::::::::::::::")
your_dog = Dog('lucy',3)
print("My dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years Old.")
your_dog.sit()





#Restaurant Class

class Restaurant():
    """An attempt to make everything withing a restaurant within reach"""

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a very posh restaurant")
        print("They even serve the " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " Is now open")

rest_call = Restaurant('Nobu', 'Afrogatto')
rest_call.describe_restaurant()
rest_call.open_restaurant()


second_rest = Restaurant('P F Chang', 'Rib Eye Steak')
second_rest.describe_restaurant()
ß
print('::::::::::::::::::::::::::::::::::::::::::::')

third_rest = Restaurant('Fourpoints', 'Egusi Soup')
third_rest.describe_restaurant()



#The car class
class Car():
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neately formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' +  self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

'''
'''
#modifying an attribute's value directly

class Car():
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neately formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' +  self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


my_new_car.odometer_reading=23
my_new_car.read_odometer()

'''


'''
#modifying an attribute's file through a method

class Car():
    """A simple attempt to represent a car."""

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading=0

    def get_descriptive_name(self):
        """Return a neately formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' +  self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """Set the odometer reading to this value
        Reject the change if it attempts to roll the odometer back"""
        self.odometer_reading = mileage
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

'''


#Incrementing an attribute's value through a method

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neately formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to this value
        Reject the change if it attempts to roll the odometer back"""
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


my_used_car = Car('Subaru', 'Outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()



def infinite_sequence(self):
    num = 0
    while True:
        yield num
        num += 1
infinite_sequence(1)


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
#<generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(i)


'''
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name) # this in Java





# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
        

r1.introduce_self()
r2.introduce_self()




class Robot:
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot()
r1.name = "Tom"
r2.color = "Red"
r3.weight = "60"

r1.introduce_self()



        self.actors = actors




class Website:
    def __init__(self,title,actors):
        self.title = title
        

    def showTitle(self):
        print(self.title)

    def showActors(self):
        print(self.actors)


obj = Website("pythonbasics.org")
obj.showTitle()
obj.showActors()





Exercise

Can you have more than one class in a file?
no, you cannot have more than one class in a file.


Can multiple objects be created from the same class?
- yes, you can create more than one object in a class


Can objects create classes?
- objects are created from classes 


Using the code above, create another object


Add a method to the class: location()
'''


