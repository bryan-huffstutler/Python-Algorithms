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
      return self.stack.pop(0)
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
  
  while stack.isEmpty() != True:
    x = stack.peek()
    y = que.peek()
    if(x == y):
      stack.popTop()
      que.dequeue()
    else: 
      return False
  return True
  
  # for x in stack.stack:
  #   if((stack.isEmpty() != True)):
  #       if (x == que.peek()):
  #         stack.popTop()
  #         que.dequeue()
  #         if(len(stack.stack) % 2 == 0):
  #           return True
  #         else:
  #           continue
  #       else:
  #         return False
  #   else:
  #     return True
    
print(isPalindrome('racecar'))
print(isPalindrome('noon'))
print(isPalindrome('python'))
print(isPalindrome('madam'))


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

   
  
  
  
