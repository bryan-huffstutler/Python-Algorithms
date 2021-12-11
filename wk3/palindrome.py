# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# class Stack:
#   def __init__ (self):
#     self.top = None
#     self.size = 0
    
#   def push (self, data):
#     node = Node(data)
#     if self.top :
#       node.next = self.top
#       self.top = node
#     else:
#       self.top = node
#     self.size += 1
    
#   def count (self):
#     return self.size
  
#   def pop (self):
#     if self.top:
#       data = self.top.data
#       self.size -= 1
#       if self.top.next :
#         self.top = self.top.next
#       else: 
#         self.top = None
#       return data
#     else:
#       return None
    
#   def peek (self):
#     if self.top:
#       return self.top.data
#     else: 
#       return None
  
#   def isEmpty (self):
#     if self.top:
#       return False
#     else:
#       return True
    
class Queue:
  def __init__ (self):
    self.que = []
  
  def enqueue(self, data):
    self.que.insert(0, data)
    
  def dequeue(self):
    data = self.que.pop()
    return data
  
  def size (self):
    return len(self.que)
  
  def isEmpty (self):
    if(len(self.que) < 1): 
      return True
    else: 
      return False
  
  def peek(self):
    if(len(self.que) > 0):
      return self.que[0]
    else:
      return None
    
class Stack:
  def __init__ (self):
    self.stack = []
  
  def add (self, data):
    self.stack.insert(0, data)
    self.top = data
    
  def popTop (self):
    self.stack.pop(0)
    
  def size (self):
    return len(self.stack)
  
  def isEmpty(self):
    if (len(self.stack) > 0):
      return False
    else: 
      return True
    
  def peek(self):
    if (len(self.stack) > 0):
      return self.stack[0]
    else:
      return None
    
def isPalindrome (data) :
  stackList = Stack()
  queList = Queue()
  def splitChar(string):
    return [char for char in string]
  splitData = splitChar(data)
  stackList.add(splitData)
  queList.enqueue(splitData)
  for item in stackList.stack:
    for que in queList.que:
      if stackList.stack[item] != queList.que[que] :
        return print(False)
      else:
        if len(stackList.stack) == 0 & len(queList.que) == 0 :
          return True
  
isPalindrome('kayak')
