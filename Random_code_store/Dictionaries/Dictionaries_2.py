

# Create a mapping of state to abbreviation 
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




