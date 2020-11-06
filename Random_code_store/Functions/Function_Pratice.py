***************************************************
                    NEW QUESTIONS 
                codingbat.com/python
***************************************************

Question:
missing_char
Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

Solution:
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back


Question:
front_back
Given a string, return a new string where the first and last chars have been exchanged.

Solution:
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]



Question:
front3
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'



  Solution:
  def front3(str):
  # Figure the end of the front
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front



Question:
front_times
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
 or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'


Solution:
  def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result += front
  return result
  


Question:
string_bits
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

Solution:
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i%2 == 0:
      result = result + str[i]
  return result 
 


Question:
sleep_in
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True


Solution:
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)


Question:
monkey_trouble
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.


monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False

Solution:
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)



Question:
sum_double
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8


Solution:
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum


Question:
diff21
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

Solution:
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2


Question:
parrot_trouble
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

Solution:
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +



Question:
makes10
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True

Solution:
def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)





Question:
near_hundred
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

Solution:

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))



Question:
pos_neg
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True

Solution:

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))



Question:
not_string
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'

Solution:
def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3


Question:
missing_char
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

Solution:
def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back


Question:
front_times
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. Return n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'

Solution:
def front_times(str, n):
  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  
  result = ""
  for i in range(n):
    result = result + front
  return result




Question:
string_bits
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'


Solution:
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result



Question:
string_splosion
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

Solution:
def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result



Question:
last2
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

Solution:
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count




Question:
array_count9
Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

Solution:
def array_count9(nums):
  count = 0
  # Standard loop to look at each value
  for num in nums:
    if num == 9:
      count = count + 1

  return count




Question:
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

Solution:
def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False



Question:
array123
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True

Solution:
def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False



Question:
string_match
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0


Solution:
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count



*********************************************************
                ---Thugging it Out---


*********************************************************

Question:
first_last6
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False


Solution:
def first_last6(nums):
  for i in nums:
    if nums[-1]==6:
      return True
    elif nums[0]==6:
      return True
    else: 
      return False




Question:
same_first_last
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True

Solution:
def same_first_last(nums):
  for i in nums:
      if len(nums)>=1:
        if nums[0]==nums[-1]:
          return True
        else:
          return False
  return False






Question:
common_end
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True


Solution:
def common_end(a, b):
  for i in a:
    if a[0]==b[0]:
      return True
    elif a[-1]==b[-1]:
      return True
    else:
      return False



Question:
sum3
Given an array of ints length 3, return the sum of all the elements.


sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7

Solution:
def sum3(n):
  total= 0
  for i in range(0,len(n)):
    total = total + n[i]
  return total



Question:
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2

Solution:
def sum2(nums):
      if  len(nums) == 0:
        return 0
      elif len(nums)==1:
        return nums[0]
      else:
        sumas = nums[0]+nums[1]
        return sumas






Question:
Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

Solution:
def double_char(str):
  result = ""
  for i in range(len(str)):
    result = result + str[i]*2
  return result





Question: 
cat_dog
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

Solution:
def cat_dog(str):
  dog_count = 0
  cat_count = 0
  for i in range(len(str)-1):
    if str[i:i+3] == 'dog':
      dog_count += 1
    if str[i:i+3] == 'cat':
      cat_count += 1
  return cat_count == dog_count



Question:
count_code
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

Solution:
def count_code(str):
  counter = 0
  for i in range (len(str)-3):
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      counter += 1
  return counter




Question:
end_other
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True


Solution:
def end_other(a, b):
  aRes=a.lower()
  bRes=b.lower()
  if aRes.endswith(bRes) or bRes.endswith(aRes):
    return True
  else:
    return False
    




Question:
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

Solution:
def xyz_there(str):
 if len(str) < 3:
  return False
 for i in range(len(str)):
  if str[i-1]!= '.':
   if str[i:i+3]=='xyz' :
    return True
 else:
  return False

 Second Solution:

 def xyz_there(str):
  return str.count('.xyz') != str.count('xyz') 
  

Question:
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0

Solution:
def count_evens(nums):
  count = 0 
  for i in nums:
    if i % 2 == 0:
      count += 1
      
  return count


Question:

When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

Solution:
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >=40:
      return True
  elif cigars >=40 and cigars <=60:
      return True
  else:
      return False





Question:

Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

Solution:
def string_bits(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result =result + str[i]
  return result





Question:
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

Solution:
def string_splosion(str):
  result = ""
  for i in range(len(str)):
      result = result + str[:i+1]
  return result
       

Question:


Solution:






Question:

Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

Solution:
def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count



Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:





Question:


Solution:






Question:


Solution:


Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:





Question:


Solution:






Question:


Solution:


Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:








Question:


Solution:






Question:


Solution:


Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:




Question:


Solution:






Question:


Solution:

def front_back(str):
  if len(str) <=1:
    return str
  
  mid = str[1:len(str)-1]

  return str[len(str)-1] + mid + str[0]

***************

  def sum_double(a, b):
  sum = a + b
  if a==b:
    sum = (a+b)*2
  return sum
***************
  frontend = 3
  if len(str) < frontend:
    frontend = len(str)
  front = str[:frontend]
  #front = str[:frontend]:
  return front +front + front


***************

  front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  #return front
  result = ""
  for i in range(n):
    result = result + front
  return result

********************

  def string_bits(str):
  for i in str:
    for i in range(len(str)):
      if i % 2 ==0:
        result =  str[i]
        return result
    




  for first= str[0:3]:
    if len(str) < 1:
      return str
  return first


  
  
  if len(str) < 3:
    return str
  return str[0:3]


********************

  def first_half(str):
  first= abs(len(str)/2)
  third = str[0:first]
  return third



 las first_last6[-1]==6
  first = first_last6[0]==6
  while last or first:
    return True
  else:
    return False

*********************
    def rotate_left3(nums):
  for i in range(0,len(nums):
    print(list(i)+nums[1])
  
    

maidansx



def sum3(n):
  total=0
  for i in range (0,len(n)):
    total = total + n[i]
  return total
    
sum3([1, 2, 3])





[::-1]
[::1]

to calculate the max value


def max_numbers(nums):
max_number = ""
    for n in nums:
        if n > max_number:
            max_number = n 

max_numbers([2,6,3,8,5,56,25])





def max_numbers(nums):
    max_number = 0
    for n in nums:
        if n > max_number:
            max_number = n 
    return max_number

max_numbers([2,6,3,8,5,56,25])



 def max_end3(numba):

    max_numbers(numba)


def max_end3(nums):
  if nums[0]>nums[2]:
    return nums[0]

max_end3([1, 2, 3]) 





def sum2(nums):
  #if len(nums)<=1:
   # return nums
  #elif len(nums) == 0:
   # return 0
  #else:
   # return nums[0]+nums[1]


  sums = nums[:2]
  for i in range(0:len(nums)):
    return i[0]+i[1]
    
    
    
def sum2(nums):
  if len(nums)<=1:
    return nums
  elif len(nums) == 0:
    return 0
  else:
    return nums[0]+nums[1]



***************************************




def sum2(nums):
  #if len(nums)<=1:
   # return nums
  #elif len(nums) == 0:
   # return 0
  #else:
   # return nums[0]+nums[1]


  #sums = nums[:2]
  for i in range(0,len(nums)):
    result = i[0],i[1]
    return result
    
    
    front_len = 3
  if front_len > len(str):
    front_len = len(str)
  front = str[:front_len]
  #return front
  result = ""
  for i in range(n):
    result = result + front
  return result

    first_number = len(nums)

def sum2(nums):
first_number = 2
if first_number >= len(nums):
    sumas = i[0]+i[1]
else:
    sumas = len(nums)
    return sumas




len(nums) >= 2:
        sumas = nums[0]+nums[1]
        return sumas
      else len(nums)==1:
        return nums[0]
sum2([1, 2, 3])





  **********************************************

def count_hi(str):
  count = 0
  #finish='hi'
  for i in range(len(str)-1):
    #count = count + str[i:i+2] == 'hi'
    count +=  str[i] =='h' and str[i+1]=='i'
  return count

  #def double_char(str):
  #result = ""
  #for i in range(len(str)):
  #  result = result + str[i]*2
  #return result


#def count_hi(s):
    #count = 0
    #for i in range(len(s)-1):
        #count += s[i]=='h' and s[i+1]=='i'
    #return count

*******************************************************





def cat_dog(str):
  for i in range(0,len(str)):
  cat_true=str[i]=='c' and str[i+1]=='a' and str[i+2]=='t'
  dog_true=str[i]=='d' and str[i+1]=='o' and str[i+2]=='g'
    for
    

  def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    count +=  str[i] =='h' and str[i+1]=='i'
  return count
  
  
def cats_dog(str):
  dogs = 0
  cats = 0
  for i in range (len(str)-1):
    
    
    
    
    
def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str) - 2):
        if str[i:i+3] == 'dog':
            count_dog += 1
        if str[i:i+3] == 'cat':
            count_cat += 1
    return count_cat == count_dog

cat_dog('1cat1cadodog')


*************************************


cat_dog = 'catdog'
for i in range (len(cat_dog)-2):
    print(i)


cat_dog('catdog')
cat_dog('catcat')
'1cat1cadodog'

catd


cat_dogs = '1cat1cadodog'
for i in range (len(cat_dogs)-2):
    print(str[i])



    if str[i:i+2] == 'dog':
        print(str)



        print(str[i:i+3])



def cat_dogs(str):
    for i in range(len(cat_dogs)-2):
        if str[i:i+2] == 'dog':
    return(str)

cat_dogs('1cat1cadodog')



def cat_dog(str):
    for i in range(len(str) - 2):
        if str[i:i+3] == 'dog':
            return str[i:i+3]
cat_dog('catdog')







cat_dog('catdog') → True
cat_dog('catcat') → False
1cat1cadodog

            count_dog += 1
        if str[i:i+3] == 'cat':
            count_cat += 1
    return count_cat == count_dog



def count_code(str):
    countCode=0
    for i in range(len(str)-1):
        if str[i:i+2] == 'co' and str[i+4] == 'e':
            countCode += 1
    return countCode

count_code('aaacopebbb')



def cat_dog(str):
    for i in range(len(str) - 1):
        if str[i:i+2] == 'co':
            return str[i:i+2]
cat_dog('aaacopebbb')




count_code('codexxcode') → 2
count_code('cozexxcope') → 2


        if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':


def count_code(str):
  countCode=0
  for i in range(len(str)-4):
    #if str[i] =='c' and str[i+1] == 'o' and str[i+4] =='e':
      
    if str[i:i+2] == 'co' and str[i+4] == 'e':
      countCode += 1
  return countCode
  
  
def count_code(str):
    counter = 0
    for i in range (len(str)-1):
        if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
            counter += 1
    return counter
count_code('cozexxcope')




def xyz_there(str):
  for i in range(len(str)-3):
    if str[i] =='x' and str[i+1] == 'y' and str[i+2] =='z':
      return True
    elif str[i:i+5] == '.xyz':
      return True
    else:
      return False 

xyz_there('abcxyz')


    str[i:i+4] == 'xyz':






return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


*******************************************




#Count Evens
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
  count=0
  for x in range(len(nums)):
    if nums[x]%2 == 0:
      count+=1
  print(count)
count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])
'''
'''
#Big Difference
#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
  max_value = nums[0]
  min_value = nums[0]
  for x in range(len(nums)):
    if nums[x] > max_value:
      max_value = nums[x]
  for x in range(len(nums)):
    if nums[x] < min_value:
      min_value = nums[x]
  print(max_value - min_value)
big_diff([10, 3, 5, 6])
big_diff([7, 2, 10, 9])
big_diff([2, 10, 7, 2])
'''
'''
#Has 2 2
#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
  true_false = False
  for x in range(len(nums)-1):
    if nums[x] == 2 and nums[x+1] == 2:
      true_false = True
      break
    else:
      true_false = False
  print(true_false)
has22([1, 2, 2])# → True
has22([1, 2, 1, 2])# → False
has22([2, 1, 2])# → False
'''
'''
#Centered Average
#Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
# except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
# You may assume that the array is length 3 or more.
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)



#   max_value = nums[0]
#   min_value = nums[0]
#   for x in range(len(nums)):
#     if nums[x] > max_value:
#       max_value = nums[x]
#   for x in range(len(nums)):
#     if max_value==nums[x]:
#       nums.pop(x)
#       break
#   for x in range(len(nums)):
#     if nums[x] < min_value:
#       min_value = nums[x]
#   for x in range(len(nums)):
#     if min_value==nums[x]:
#       nums.pop(x)
#       break
#   mean = 0
#   for x in range(len(nums)):
#     mean+=nums[x]
#   print(int(mean/len(nums)))
centered_average([1, 2, 3, 4,100])# → 3
centered_average([1, 1, 5, 5, 10, 8, 7])# → 5
centered_average([-10, -4, -2, -4, -2, 0])# → -3
'''
'''

******************************************************************************************************
******************************************************************************************************
******************************************************************************************************


class MyClass:
  honk = 2 # a class variable - belongs to the class
  def __init__(self):
    self.bar = 1 # a member variable - its a variable on an instance of a class
    self.bin = 5
    
  def printAll(self):
    print("HONK", self.honk, "BAR", self.bar, "BIN", self.bin)
  def printHonk(self):
    print(self.honk)
  def printBar(self):
    print("BAR", self.bar)
  
    
f = MyClass() # f is variable that points to the instance
g = MyClass() # g is variable that points to an instance
foo = 1 # a variable

f.bar = 2 # f.bar is not the same as g.bar, because f is a different instance than g
g.bar = 3

c = MyClass # c points to myClass
d = MyClass() # d is an instance of MyClass
e = c() # e is an instance of MyClass

d.printBar()
d.bar = 3
d.printBar()
e.printBar() # what should e.bar be?

h = MyClass()
h.printHonk()
h.printBar()
h.printAll()

f = MyClass # c and f point to MyClass
******************************************************************************************************
******************************************************************************************************
******************************************************************************************************

https://pythonbasics.org/








def splicing(firstOne):
  pass


def splicing(LastOne):
  pass


def splicing(EveryOther):
  pass


def splicing(firstAndLast):
  pass


def splicing(LastOne):
  pass



Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number 
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)

###########################################################


for FizzBuzz in range(20):
  if FizzBuzz % 3 ==0 and FizzBuzz % 5 == 0:
    print ("FizzBuzz")
    continue
  elif FizzBuzz % 3 == 0:
    print("Fizz")
    continue
  elif FizzBuzz % 5 == 0:
    print("Buzz")
    continue
  print(FizzBuzz)


###########################################################





















