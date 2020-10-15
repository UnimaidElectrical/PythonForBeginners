**************************************************


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:        
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


def traverse(node, output):
    if node is None:
      # we are visiting an empty child
      return
    # every recursive function needs a base case
    # print("VISITING", node.val) # preorder traversal
    traverse(node.left, output)
    # print("VISITING", node.val) # inorder traversal
    traverse(node.right, output)
    
    output.append(node.val)
    # print("VISITING", node.val) # post order traversal
    return output

traverse(root)


# traverse(root)
        
# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)

# import sys
# sys.setrecursionlimit(10)
# def traverse(node):
#     if node is None:
#       # we are visiting an empty child
#       return
#     # every recursive function needs a base case
#     print("VISITING", node, node.val)
#     traverse(node.left)
#     traverse(node.right)
  
# traverse(root)







 Python program to do inorder traversal without recursion 

# A binary tree node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None




# Iterative function for inorder tree traversal 
def inOrder(root): 
	
	# Set current to root of binary tree 
	current = root 
	stack = [] # initialize stack 
	done = 0
	
	while True: 
		
		# Reach the left most Node of the current Node 
		if current is not None: 
			
			# Place pointer to a tree node on the stack 
			# before traversing the node's left subtree 
			stack.append(current) 
		
			current = current.left 

		
		# BackTrack from the empty subtree and visit the Node 
		# at the top of the stack; however, if the stack is 
		# empty you are done 
		elif(stack): 
			current = stack.pop() 
			print(current.data, end=" ") # Python 3 printing 
		
			# We have visited the node and its left 
			# subtree. Now, it's right subtree's turn 
			current = current.right 

		else: 
			break
	
	print() 

# Driver program to test above function 

""" Constructed binary tree is 


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

inOrder(root) 
"""


***************************** RECURSION EXPLAINED*************************


Recursion is a function that calls itself
It calls itself till it does not call itself anymore. i.e the the conditon runs out 
The condition where it stops calling itself is called the base ccase
when thinking of recursion, try to think about the base case first




#Implementing a countdown timer using recursion

import time
def recur_countdown_timer(n):
	if n==0:
		return n
	else:
		print(n)
		time.sleep(1)
		return recur_countdown_timer(n-1)
z=5
print(recur_countdown_timer(z))



#Implementing a countdown timer using iteration

import time
def iter_countdown_timer(n):
	while n>0:
		print(n)
		time.sleep(1)
		n -=1
	print(n)
z=5
print(f"Counting down from {z}: ")
iter_countdown_timer(z)




