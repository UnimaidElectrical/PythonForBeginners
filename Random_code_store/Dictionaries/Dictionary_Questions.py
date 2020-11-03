#Below are random questions to solidify the knowledge on how python dictionaries work.
#This will be very useful in future when we start talking about hash tables and JSON formatting or data parsing in JSON
'''
exercise 1: Below are the two lists convert it into the dictionary
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
#Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

sampleDict = dict(zip(keys,values))
print(sampleDict)

'''
exercise 2: Merge following two Python dictionaries into one
'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#Expected output: {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3={**dict1,**dict2}
print(dict3)


#Another way

Dict3 = dict1.copy(),dict2.copy()  #This will give two seperate dictionaries in one. ({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50})
print(Dict3)

#Another way
Dict3 = dict1.copy()
Dict3.update(dict2)     #This will give you a continious dictionary record {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(Dict3)





'''
exercise 3: Access the value of key ‘history’
'''
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

#{"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}} #Re-arranging

print(sampleDict['class']['student']['marks']['history'])

'''
exercise 4: Initialize dictionary with default values
Given:
'''
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

initialized=dict.fromkeys(employees,defaults)
#print([employees],[defaults])

#print(initialized)
print(initialized['Kelly'])   #{'designation': 'Application Developer', 'salary': 8000}



'''
exercise 5: Create a new dictionary by extracting the following keys from a given dictionary
Given dictionary:
'''

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

#Keys to extract
keys = ["name", "salary"]

#Expected output: {'name': 'Kelly', 'salary': 8000}


newkeys= {k:sampleDict[k] for k in keys}
print(newkeys)


*********************************
**********Pratice****************
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

#Keys to extract
keys = ["name", "salary"]

newhome={i:sampleDict[i] for i in keys}
print(newhome)
*******************************





sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

keys=["name","salary"]
for k in keys:
    print(k,':',sampleDict[k])






'''
exercise 6: Delete set of keys from Python Dictionary
Given:
'''

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]
valuesToRemove = ["Kelly","New york"]

#Expected output: {'city': 'New york', 'age': 25}

#Using List comprehension
newdict={i:sampleDict[i] for i in sampleDict.keys()-keysToRemove}
print(newdict)



#create a new dictionary with the items from the previous dictionary
 sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keys=["name","salary"]
for k in keys:
    newdict={k,sampleDict[k]}
    print(newdict)



#without list comprehension and without the need to create a new dictionary.
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
keysToRemove = ["name", "salary"]
for i in keysToRemove:
    del sampleDict[i]
print(sampleDict)





'''
exercise 7: Check if a value 200 exists in a dictionary
'''

sampleDict = {'a': 100, 'b': 200, 'c': 300}

print(200 in sampleDict.values())



'''exercise 8: Rename the key city to location in the following dictionary

Expected output:
{
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "location": "New york"
}
'''
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sampleDict['location']= sampleDict.pop('city')
print(sampleDict)





'''
exercise 9: Get the key corresponding to the minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}'''

sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(max(sampleDict,key=sampleDict.get))
print(min(sampleDict,key=sampleDict.get))




'''
exercise 10: Given a Python dictionary, Change Brad’s salary to 8500
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
'''

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict['emp3']['salary']=8500









'''
d=[2,3,4]
e=[5,6,7]
for i in d:
    i.append(d)
    return i
print(d)
'''