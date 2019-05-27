import math
n = int(input("Enter the first number : "))
m = int(input("Enter the seond number : "))

x = math.gcd(n,m)
print("The GCD is",x)


""" (or)

x = int(input("enter value of a"));       #taking user input

y = int(input("enter value of b"));       # taking user input
l = x * y
rem = 0
while(a != 0):
    rem = b % a
    b = a
    a = rem
print("gcd =",b)
"""
