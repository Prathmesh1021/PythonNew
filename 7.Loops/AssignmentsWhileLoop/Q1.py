# Q1--> Seperate each digit of a number and print it on the new line 

a=256
while a>0:
    print(a%10)
    a=a//10 
    
# Accept Input User 

b=int(input("Enter the Number :"))
while b>0:
    print(b%10)
    b=b//10
