# implementing SinglyLinkedList,DoubleLinkedList and DoubleEndedQueue using stack and queue  

class Stack:
  def __init__(self):
    self.values = []
    self.values = SinglyLinkedList()
    
  def push(self, val):
    self.values.push_front(val)
  
  def pop(self):
    val = self.values.front()
    self.values.remove_front()
    return val
  
class Queue:
  def __init__(self):
    self.list = DoubleLinkedList()
    
  def push(self, val):
    self.list.insert_front(val) # O(1)
  
  def pop(self):
    val = self.list.get_back() # O(1)
    self.list.remove_back() # O(1) for DLL, O(N) for SLL
    return val
  
# also known as deque
# from collections import deque
class DoubleEndedQueue():
  def appendleft():
    pass
  
  def popleft():
    pass
  
  def appendright():
    pass
  
  def popright():
    pass