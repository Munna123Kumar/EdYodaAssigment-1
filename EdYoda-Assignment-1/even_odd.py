# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 4
#Number of odd numbers : 5

num=(1, 2, 3, 4, 5, 6, 7, 8, 9)
count_even=0
count_odd=0

for i in num:
    if not i%2:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers : ",count_even)
print("Number of odd numbers : ",count_odd)