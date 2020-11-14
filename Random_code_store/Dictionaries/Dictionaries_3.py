

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



alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_o['x_position']))
#Move the alien to the right, determine how far you'll move the alien based on it's current speed


if alien_o['speed'] == 'slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2 
else:
    #This must be a fast alien
    x_increment = 3
#The new position is the old position plus the increment
alien_o['x_position']= alien_o['x_position'] + x_increment
print("New x-position: " + str(alien_o['x_position']))





#Removing Key-Value Pairs
alien_o = {'color': 'green', 'points':3}
print(alien_o)

del alien_o['points']
print(alien_o)


#A Dictionary of similar objects

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print(favorite_languages['sarah'])
print("Sarah's favorite language is: " + favorite_languages['sarah'].title() + ".")

#or this can also be implemented in this way
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Looping through a dictionary

#Looping through all key-value pairs

user_o = {
'username':'efermi',
'first':'enrico',
'second':'fermi',
}

for key,value in user_o.items():
    print("\nkey: " + key)
    print("Value " + value)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() +" 's favorite language is: "+ language.title()+".")
    #print(language)



#Looping through all the keys in a dictionary
'''
The Keys() method is useful when you don't have to work with all the values in a dictionary.
Let's loop through the favorite_languages dictionary and print the names of everyone who took the poll
'''
1)
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

2)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + " I can see that your favorite language is  "+ favorite_languages[name].title() + "!")



