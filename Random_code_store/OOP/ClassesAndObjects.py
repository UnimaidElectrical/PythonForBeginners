


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

