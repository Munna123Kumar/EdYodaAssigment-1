#---Lets play with fibonacci series---
#The Fibonacci Sequence is the series of numbers :0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34...'''

n=int(input('Enter the number :'))
#Let the consider
a=0
b=1
c=0

while c<=n:
    print(c)
    a=b
    b=c
    c=a+b