# Q3 Accept a number and check if it is a pallindromic number (if number and its reverse are equal)

a=int(input("Enter the Number : "))
copy =a
rev =0
while a > 0:
    rev =rev *10 + a %10
    a=a//10

if copy ==rev:
    print("pallindromic number ")
else:
    print("not a pallindronic number ")