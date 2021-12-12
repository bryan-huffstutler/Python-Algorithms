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
      return self.que[-1]
    else:
      return None
    
class Stack:
  def __init__ (self):
    self.stack = []
    self.top = None
  
  def push (self, data):
    self.stack.insert(0, data)
    self.top = data
    
  def popTop (self):
    if(len(self.stack) != 0):
      return self.stack.pop(0) #Now returns the popped element
    else:
      return None
    
  def size (self):
    return len(self.stack)
  
  def isEmpty(self):
    if (len(self.stack) != 0):
      return False
    else: 
      return True
    
  def peek(self):
    if (len(self.stack) != 0):
      return self.stack[0]
    else:
      return None
    
def isPalindrome (data) :
  stack = Stack()
  que = Queue()
  for x in data:
    stack.push(x)
    que.enqueue(x)
  #no longer accessing the underlying data structure
  while stack.isEmpty() != True: 
    x = stack.peek()
    y = que.peek()
    if(x == y):
      stack.popTop()
      que.dequeue()
    else: 
      return False
  return True
    
print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))


#Expected Output
#True
#True
#False
#True