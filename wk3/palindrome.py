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
  
  def add (self, data):
    self.stack.insert(0, data)
    self.top = data
    
  def popTop (self):
    self.stack.pop(0)
    if(len(self.stack) != 0):
      self.top = self.stack[0]
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
  def splitChar(string):
    return [char for char in string]
  splitData = splitChar(data)
  for x in splitData:
    stack.add(x)
    que.enqueue(x)
  
  for x in stack.stack:
    if((stack.isEmpty() != True)):
        if (x == que.peek()):
          stack.popTop()
          que.dequeue()
          if(len(stack.stack) % 2 == 0):
            return print(True)
          else:
            continue
        else:
          return print(False)
    else:
      return print(True)
    
isPalindrome('racecar')
isPalindrome('noon')
isPalindrome('python')
isPalindrome('madam')


#Expected Output
#True
#True
#False
#True




  # for x in que.que:
  #   if(x == stack.top):
  #     stack.popTop()
  #   else: 
  #     return print(False)
  # return print(True)
  
  
# def isPalindrome(n):
#   if n == n[::-1]:
#     print("This word is palindrome")
#   else:
#     print("This word is not palindrome")

   
  
  
  
