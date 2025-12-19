#Q Accept a number and Check if it a perfect number or not.
#A number whose sum of factors is equal to the number itself
#Ex - 6=1,2,3=6

n=int(input("Enter Your Values"))
sum=0
for i in range(1,n):
    if n%i==0:
     sum=sum+i
if sum==n:
    print("This is the Perfect Number")
else:
    print("this is the Not Pefect Number")

    
    
   
 
    