""" What this section is all about

How modern computers store human languages for display and processing and how Python 3 calls this strings
How you must “encode” and “decode” Python’s strings into a type called bytes
How to handle errors in your string and byte handling
How to read code and find out what it means even if you’ve never seen it before
"""


import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

print(raw_bytes, "<===>", cooked_string)
languages = open("languages.txt", encoding="utf-8")
main(languages, encoding, error)




cross(a, b, c, d): a and b are strings, c and d are integers. given cross("foo", "bar", 2, 3), return "foofoobarbarbar"

dLink=[3,5,'t','s',2]

def dLink_func(value):
    dLinkNum=[]
    dlinkstring=[]
    for item in dLink:
        if item = int(value):
            


    for this many times:
    if conditional: 
        do this thing
    else:
        do something else  



for item in list:
    if conditional:
        expression 


def is_dig(s):
    numbers = "0123456789"  # single iterable of the numbers
    for i in s:
        if i not in numbers:
            return False
    return bool(s) 


return a.append


def is_dig(s):
    numbers = "0123456789"  # single iterable of the numbers
    alphabeths="abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i not in numbers:
            a.append(i)
        else i not in alphabeths:
            b.append(i)


for n in alist:
    if n == 5:
        new.append(n)
    else:
        new.append(n+1)



