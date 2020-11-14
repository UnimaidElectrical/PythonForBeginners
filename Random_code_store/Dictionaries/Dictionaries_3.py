

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


user_1 = {
'First Name': 'Mercedes',
'Last Name':'Bench',
'age': 23,
'City Of Residence' :'San Francisco',
}
for man in user_1():
    print(man)


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



#Looping through a Dictionary's keys in order
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")



#Values
#Looping through all the values in a dictionary

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())


#Making this sorted
for language in sorted(favorite_languages.values()):
    print(language.title())




#Removing the duplicates from the values
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for language in set(favorite_languages.values()):
    print (language.title())




#Making this sorted
for language in sorted(set(favorite_languages.values())):
    print (language.title())





#Nesting
#    A list of Dictionaries:


#Creating the dictionary
alien_o = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}


#Packing the created dictionary into a list
aliens = [alien_o,alien_1,alien_2]

for alien in aliens:
    print(alien)



#Make an empty list for storing aliens
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)    # In this case you're applying new_alien to the aliens list

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("..............")

#Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))




#first we Make an empty list
aliens = []
for alien_number in range(0,30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    alien.append(new_alien)

#This will only modify the first 3 aliens in the list
for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


#A  List in a Dictionary

pizza = {
    'crust':'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + " with the following toppings: ")

for topping in pizza['toppings']:
    print("\t" + topping)




favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + " 's favorite languages are: ")
    for language in languages:
        print("\t" + language.title())



#A Dictionary in Dictionary

users = {'aeinstein':
    {'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
                            },'mcurie': {
                                        'first': 'marie',
                                        'last': 'curie',
                                        'location': 'paris',
                                        },
        }

for username,user_info in users.items():
    print("\nUsername: "+ username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull Name: "+ full_name.title())
    print("\tLocation: "+ location.title())

