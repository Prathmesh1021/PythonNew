#print the sum of all even and odd numbers in a range separately
n=int(input("Enter Your Number:"))
Even=0
Odd=0
for i in range(1,n+1):
    if i%2==0:
        Even = Even +i
    else:
        Odd =Odd +i
print(f"Your Even sum is {Even} and Your Odd Sum is {Odd}")