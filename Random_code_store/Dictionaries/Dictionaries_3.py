

##############:::::::::::::::::::::::##############**********################
###::::                                                               ###::::
###::::     Dictionaries Revisited:                                   ###::::
###::::                                                               ###::::
##############:::::::::::::::::::::::##############**********################
# A Simple Dictionary

#The dictionary alien_o stores the alien's color and point value. The two print statements access and display that information

alien_o={'color': 'green', 'points': 5}
print(alien_o['color'])
print(alien_o['points'])

#:::::::::::::::::::::::::::::::::
#Working with dictionaries
#Dictionary Defination
#:::::::::::::::::::::::::::::::::
'''
A dictionary in python is a collection of key-value pairs. Each key is connected to a value and you can use the key to access the value associated to that key
A key value can be a number, a string, a list, or even another dictionary
'''

#Accessing Values in a Dictionary

alien_o = {'color':'green'}
print(alien_o['color'])

#You can have an unlimited number of key value pairs in a dictionary

#Concartination With Dictionaries
alien_o={'color':'green', 'points':5}

new_points = alien_o['points']
print("you just earned " + str(new_points) + " points!") #when concartinating in python, you cannnot add a string to an int, you need to convert the int to a str first.


#Adding new key-value pairs

alien_o = {'color':'green', 'points':5}
print(alien_o)

alien_o['x_position'] = 0
alien_o['y_position'] = 25
print(alien_o)


#Starting with an empty Dictionary 

alien_o = {}
alien_o['color']='green'
alien_o['points']=5
print(alien_o)


#Modifying values in a Dictionary 

alien_o = {'color':'blue'}
print('The alien is ' + alien_o['color'] + '.')

alien_o['color'] = 'yellow'
print("The alien is now " + alien_o['color'] + ".")


