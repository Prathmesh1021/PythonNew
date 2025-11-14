#Q Print all the factor of a number 

n=int(input("Which Number Factor you want:"))
for i in range (1,n+1):
    if n%i==0:
        print("this is your Factor",i)