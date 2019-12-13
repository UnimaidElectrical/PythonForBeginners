#Constructor 

class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

bob = Human()
print(bob.legs)






class Plane:
    def __init__(self):
        self.wings = 2

        # fly
        self.drive()
        self.flaps()
        self.wheels()

    def drive(self):
            print('Accelerating')

    def flaps(self):
            print('Changing flaps')

    def wheels(self):
            print('Closing wheels')

ba = Plane()





class Bug:
   def __init__(self):
       self.wings = 4

class Human:
   def __init__(self):
       self.legs = 2
       self.arms = 2

class sam:
    def __init__(self):
        self.head = 5
        self.body = 4

bob = Human()
tom = Bug()
cia = sam()

print(tom.wings)
print(bob.arms)
print(cia.head)

