#Q Accept a number and Check if it a perfect number or not.
#A number whose sum of factors is equal to the number itself
#Ex - 6=1,2,3=6

n = int(input("check your number is perfect or not :"))
sum = 0
for i in range(1,n):
    if n%i== 0:
        sum = sum + i
if sum == n:
    print("your number is perfect")
    
else:
    print("not a perfect numer")
