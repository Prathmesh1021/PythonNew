#Q2--> Accept the number and print its reverse\

a=int(input("Enter the Number : "))
rev =0
while a > 0:
    rev =rev *10 + a %10
    a=a//10
print(rev)