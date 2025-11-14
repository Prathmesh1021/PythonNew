#Q Factorial of a number 
n=int(input("Enter tell your Number:"))
Fact = 1
for i in range(1,n+1):
    Fact = Fact *i
    
print(f"your Factorial  is {Fact} ")