import random

def shuffle (arr) :
  #Time complexity of this algorithm is O(n)
  #because it has to iterate through the list
  for i in range(len(arr)-1, 0, -1):
    #creates a random between 0, and i-1
    # was i+1, changed to i-1 to address 
    # the list index out of range error I would sometimes get
    x=random.randint(0, i-1)
    #sets a random index to equal the current index of for loop
    arr[i], arr[x] = arr[x], arr[i]
  return arr

input = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(shuffle(input))

# Would like to see an example of a recursive shuffle function