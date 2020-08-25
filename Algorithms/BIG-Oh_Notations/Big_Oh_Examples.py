Below are some examples of functions in Python. Look at each and take note of the time efficiency. Then, in the quiz, enter those values using the correct notation. Use approximations wherever possible!

"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee



Example 1
We iterate over every manatee in the manatees list with the for loop. Since we are given that manatees has n elements, our code will take approximately O(n) time to run.

Example 2
We look at two specific properties of a specific manatee. We are not iterating over anything - just doing constant-time lookups on lists and dictionaries. Thus the code will complete in constant, or O(1), time.

Example 3
There are two for loops, and nested for loops are a good sign that you need to multiply two runtimes. Here, for every manatee, we check every property. If we had 4 manatees, each with 5 properties, then we would need 5+5+5+5 steps. This logic simplifies to the number of manatees times the number of properties, or O(nm).

Example 4
Again we have nested for loops. This time we are iterating over the manatees list twice - every time we see a manatee, we compare it to every other manatee age. We end up with O(nn), or O(n^2) (which is read as "n squared").

Throughout the course, you can reference the Big-O Cheat Sheet to keep track of time complexities for many of the algorithms and data structures we study.