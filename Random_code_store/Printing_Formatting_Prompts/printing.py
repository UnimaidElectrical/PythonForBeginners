

#Printing and Formatting

"""
We use %r for debugging, since it displays the "raw" data of the variable, but we use %s and others for displaying to users.
"""

x = "There are %d types of people." % 10
binary="binary"
do_not="don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print (x)
print (y)

print  ("I said: %r." % x )
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isin't that a joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)  # adding the strings together makes the string alot longer because here we are using the concartinate feature imbeded in the python interpreater




# More Printing 

print ("Mary had a little lamb.")
print ("it's fleece was white as %s" %'snow')
print ("And everywhere that Mary went.")
print ("." * 10) 

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

print(end1 + end2 + end3 + end4 + end5 + end6,) # What does the comma do here ?
print(end7 + end8 + end9 + end10 + end11 + end12)


# Printing Printing

formatter = "%r %r %r %r" # this will get printed with a single quote
print(formatter % (1,2,3,4))

print(formatter % ("One", "Two", "Three", "Four"))
print (formatter % (True, False, True, False))
print (formatter % (formatter, formatter, formatter, formatter))

print (formatter % 
    ("I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So i said goodnight!."))




