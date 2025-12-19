#Q Print all the factor of a number 
n=int(input("Which Number You Want For Factor:"))
for i in range(1,n+1):
    if n%i==0:
     
     print(f"your Factor is ",i)