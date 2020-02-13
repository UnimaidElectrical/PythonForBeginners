


mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apples'])


#This goes in mystuff.py
def apple():
    print("I AM APPLES!")


import mystuff
mystuff.apple()


#This is an variable
tangerine = "Living reflection of a dream"


import mystuff 
mystuff.apple()
print(mystuff.tangerine)


mystuff['apple']    #Get apple form dict
mystuff.apple()     #Get apple fromt the module 
mystuff.tangerine   #Same thing, it's just a variable.




#Dict Style 
mystuff['apples']

#Module Style 
mystuff.apples()
print(mystuff.tangerine)

#Class Style
thing = MyStyle()
thing.apples()
print(thing.tangerine)





