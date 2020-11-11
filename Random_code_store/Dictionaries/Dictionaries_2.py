

# Create a mapping of state to abbreviation
from click import prompt

states ={
    'Oregon': 'OR',
    'Florida': 'FL',
    'California':'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


#Create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'TX': 'Houston',
    'IL': 'Illinois'
}


#Add some more cities 
cities['NY']='New York'
cities['OR']='Portland'
cities['CO']='New Haven'

#Add some more states
# I am still wondering why this doesn't work
# states['Kansas City']='KS'
#states['New Mexico']='NM'
# states['Oklahoma']='OK'



#Print out some cities
print('-'*10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
print("CO State has: ", cities['CO'])


#Print some states
print('-'*10)
print("Michigan's abbreviation is: ",states['Michigan'])
print("California's abbreviation is: ", states['California'])

#Do it by using the states then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


#Print every state abbreviation
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is an abbreviated {abbrev}")


#Print every city in the state.
print('-'* 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city{city}")

#Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has {cities[abbrev]}")


print('-' * 10)
#safely get an abbreviation by state that might not be there
state = states.get("Texas")


if not state:
    print("Sorry, no Texas.")

#get a city with no default value

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")



mystuff = {'apple': 'I AM THE HAPPIEST PERSON ALIVE!'}
print(mystuff['apple'])




**********************************

******Dissecting Dictionaries*********

d2={'spam':2, 'ham':1,'eggs':3}
d3= {'food': {'ham':1, 'egg':2}}
d3['food']['ham']
#d2['spam']
d2

len(d2)
d2.has_key('ham')
'ham' in d3

d2.keys()


d3['food']['ham']
'ham' in d3

d2={'spam':2, 'ham':1,'eggs':3}
d2['ham']=['grill','bake','fry']
#d2
del d2['eggs']
#d2

d2['brunch']='Bacon'
d2
d2.values(), d2.keys()
d2.values(), d2.items()

d2.get('spam'), d2.get('toast'), d2.get('toast', 88) 



#using update:
d2
d3 = {'toast':4,'muffin':5}
d2.update(d3)
d2


##############:::::::::::::::::::::::##############**********################
###::::                                                               ###::::
###::::     #A Language Table:                                        ###::::
###::::                                                               ###::::
##############:::::::::::::::::::::::##############**********################
table = {'Python': 'Guido Van Rossum',
        'Perl': 'Larry wall',
        'Tcl': 'John Ousterhout'}
table
language = 'Python'  # creates an objects that points to the value (table array)
table
creator = table[language]
creator

second_language = 'perl'
creator = table[language],second_language
creator

for lang in table.keys():
    print (lang, '\t', table[lang])



for lang in table.items():
    print (lang, '\t', table[lang])

##############:::::::::::::::::::::::##############**********################
##############:::::::::::::::::::::::##############**********################
##############:::::::::::::::::::::::##############**********################
###::::                                                               ###::::
###::::     #using Dictionaries for sparse data structures            ###::::
###::::                                                               ###::::
##############:::::::::::::::::::::::##############**********################
##############:::::::::::::::::::::::##############**********################
##############:::::::::::::::::::::::##############**********################


Matrix= {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99

X = 2; Y = 3; Z = 4;
Matrix[(X,Y,Z)]

Matrix

#This will throw up an error
Matrix[(2,3,6)]

'''
to aviod the error messages we can use 

If statements
try Statement
dictionary get method
'''
Matrix= {}
Matrix[(2,3,4)] = 88


#If statements
if Matrix in ((2,3,6)):   # The implementation in Python 2 will be if Matrix.has_key((2,3,6)):
    print (Matrix[(2,3,6)])
else:
    print (0)

#try Statement
Matrix= {}
Matrix[(2,3,4)] = 88
try:
    print (Matrix[(2,3,6)])
except KeyError:
    print (0)


#dictionary get method

Matrix= {}
Matrix[(2,3,4)] = 88
#Matrix.get((2,3,4),0)
Matrix.get((2,3,6),0) # The Zero being used here is to state either the main value or Zero


##############:::::::::::::::::::::::##############**********################
###::::                                                               ###::::
###::::     #Using Dictionaries as records:                          ###::::
###::::                                                               ###::::
##############:::::::::::::::::::::::##############**********################

rec = {}
rec['name'] = 'mel'
rec['age'] = 41
rec['Job'] = 'trainer/writer'

print (rec['name'])

print(rec['name'],'age')   # This will print out two objects or keys in the dictionary. don't know why the second object is not allowed to sit in it's own square bracket



#Nested Dictionary

mel = {'name': 'Mark',
        'jobs': ['trainer','writer','farmer'],
        'web': 'www.rmi.net/~lutz',
        'home': {'state': 'CO','zip':80501}}

mel['name']
mel['jobs']
mel['jobs'][1][2]
mel['home']['zip']


#Cyclic Data Structures
#These are datastructures that get caught in a loop, say for instance appending a string to al already existing list with the same string

L= ['grail']
L.append(L)
L


Immutable calls cannot be changed in place but there are ways to mitigate this, but it may be costly for scaling up

T = (1,2,3)
T[2] = 4         #We should expect an error here
T = T[:2] + (4,)  #We should expect to get (1,2,4) here
T






'''

def make_album(artist_name,album_title,track_number=''):
    album_name = {name:artist_name, title:album_title,track:track_number}
    #return full_name.title()

while True:
    if track_number:
        full_names = artist_name + '' + album_title + '' + track_number
        #return full_names.title()
    else:
        full_names = artist_name + '' + album_title
        #return full_names.title()

#artist_name = input("Artist Name: ")
#album_title = input("Album Title: ")

music=make_album(artist_name,album_title)
print(music)


#Album= input(f'Please enter the album name and album title to search for: ')
#f'Please enter the album name and album title to search for: ',

print(make_album(xzibit, man vs machine,10))
'''

def make_album(artist, title):
    '''This is to make a dictionary of album'''
    album_dict = {
        'artist':artist.title(),
        'title':title.title(),
    }
    return album_dict

album = make_album('greenday','shadow')
print(album)
album = make_album('metallica','unbellivable')
print(album)





def make_albumTracks(artist,title,tracks=0):
    '''This makes a dictionary of artist titles and tracks'''
    album_dict_tracks={
        'album':artist.title(),
        'title':title.title(),
    }
    if tracks:
        album_dict_tracks['tracks'] = tracks
    return album_dict_tracks
album = make_album('greenday','shadow',tracks=10)
print(album)
album = make_album('metallica','unbellivable')
print(album)




def make_album(artist, title,track=0):
    album_dict={
        'artist':artist.title(),
        'title':title.title(),
    }
    if track:
        album_dict['track'] = track
    return album_dict

title_prompt = "/nWhat album are you thinking of: "
artist_prompt = "Who is the artist? "

print("Enter quit at any time you want to stop")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist= input(artist_prompt)
    if artist == 'quit':
        break
    album=make_album(artist,title)
    print(album)






