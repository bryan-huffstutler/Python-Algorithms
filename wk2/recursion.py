
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum
print(loop1())

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum
print(loop2())

def loop1Rec(num,odd_sum):
    # Duplicate the loop1 function using recursion
    if num <= 0 : #base of 0 because counting down from 20
        return odd_sum
    else: 
        if num % 2==1: #checks if number is odd
            odd_sum+=num #adds odd number to odd_sum
        return loop1Rec(num-1, odd_sum) #recalls itself moving state toward the base

print(loop1Rec(20, 0))

def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
    if num >= 20: #while loop dictates going from 0 to 20 as its base, instead of 20 to 0
        return even_sum 
    else: 
        if num % 2 == 0: #checks if number is even or not
            even_sum += num #adds even number to even_sum
        return loop2Rec(num+1, even_sum) #recalls itself moving state toward base

print(loop2Rec(0,0))
