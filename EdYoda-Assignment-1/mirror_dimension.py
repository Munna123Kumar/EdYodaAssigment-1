# Write a Python program that accepts a word from the user and reverse it.

a=input("Enter the string :")
for i in range((len(a)-1),-1,-1):
    print(a[i],end="")