#take a sorted list
#split it in half, check if half is the term
#if half is not the term, check if term is < or > than the half
#check either side depending on < or >
#repeat until it is determined if the term is in the list or not
list_one = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] #find 31
list_two = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] #find 77
list_three = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"] #find "Delta"

def binarySearch(list, term):
  low = 0
  mid = 0
  high = len(list) - 1
  
  while low <= high:
    mid=(high + low) // 2
    if list[mid] < term:
      low = mid + 1
    elif list[mid] > term:
      high = mid - 1
    else:
      return True
  return False

print(binarySearch(list_one, 31))
print(binarySearch(list_two, 77))
print(binarySearch(list_three, 'Delta'))