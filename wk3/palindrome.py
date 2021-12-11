class Queue:
  def __init__ (self):
    self.que = []
  
  def enqueue(self, data):
    self.que.insert(0, data)
    
  def dequeue(self):
    data = self.que.pop(0)
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
    self.top = None
  
  def add (self, data):
    self.stack.insert(0, data)
    self.top = data
    
  def popTop (self):
    self.stack.pop(0)
    self.top = self.stack[0]
    
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
  stackList = Stack()
  queList = Queue()
  def splitChar(string):
    return [char for char in string]
  splitData = splitChar(data)
  for x in splitData:
    queList.enqueue(x)
    stackList.add(x)

  for x in stackList.stack:
    if((stackList.isEmpty() != True)):
        if (x == queList.peek()):
          stackList.popTop()
          queList.dequeue()
          print(queList.que, stackList.stack)
        else:
          return print(False)
    else:
      return print(True)
      
      
   
  
  
  
# isPalindrome('racecar')
isPalindrome('noon')
# isPalindrome('python')
# isPalindrome('madam')

#Expected Output
#True
#True
#False
#True