#write a program to swap two numbers

A=int(input("Enter First Number"))
B=int(input("Enter Second Number"))

print("Before Swapping",A,B)
#First Method using Thired Variable
C=A
A=B
B=C

print("After Swapping",A,B)

#Second Method without using Thired Variable
A,B=B,A

print("After Swapping",A,B)

#Without Using Third Variable
A=A+B
B=A-B
A=A-B

print("After Swapping",A,B)
