# The break statement can be used to prematurely end the while loop
# The break statement can also be used to immediately end a loop.

i=0
while 1==1:  # the code will keep running as far as this remains true 
    print(i)
    i=i+1
    if i > 5:
        print("Breaking")
        break
print("Finished")


# using the break statement outside a loop can cause an error


#Break Statement:
'''
There is a shortcut to getting the program execution to break out of a while loops clause early. If the execution reaches a break statement, it immediately exits the while loops clause. 
In code, a break statement simply contains the break keyword 
'''

while True:
    print('Please type your name. ')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

#An infinite loop that never exits is a common programming bug





#Continue Ststement
'''
Like break statements, the continue statement are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluatess the loops condition.
(This also happens when the execution reaches the end of the loop)
'''

#Use the condition to as for a program that asks for a name and password. Enter the following codeinto the editor window and save the program.

while True:
    print('who are you? ')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password=input()
    if password=='swordfish':
        break
print('Access Granted.')





i=0
while True:
    j = int(input("Take a guess between 1 and 20: "))
    i+=1
    if j<18:
        print("Too Low")
    elif j>19 and j<20:
        print("Too High")
    elif j==19:
        print(f"Good Job! You guessed my number in {i} guesses!")
        break
    else:
        print("Too High")







