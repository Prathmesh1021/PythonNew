#Q1 Accept two numbers and print the greatest between them
a=12
b=13
if a<b:
    print("b is greater than a")
else:
    print("a is greater than b ")
    
#Question2 ==>Accept two numbers from user and print the greatest number    
a=int(input("Enter your First Value: "))
b=int(input("Enter your Second Value: "))

if a>b:
    print(f"{a} is greather than {b}" )
else:
    print(f"{b} is greater than {a}")
#Q3 Accept The Gender From User as character and print the respective greeting meassage (EX:-Good Morning Sir/Madam)
gen=input("Enter your gender:")

if gen =="male " or gen=="Male" or gen=="MALE":
    print("Good Morning Sir")
elif gen=="fmail" or gen=="Fmale" or gen=="FMALE":
    print("Good Morning Madam")
else:
    print("please enter valid Value")
#Q4 Accept an integer and check whether it is even or odd number
a=int(input("Enter your value: "))
if a%2==0:
    print(f"{a} is even number ")
else:
    print(f"{a} is odd number ")
#Q5 Accept name and age from user.Cheack if the user is a valid voter or not?EX->Hello Rahul you are a valid voter  

name=(input("enter your name : "))
age=int(input("Enter your age: "))

if age>=18:
    print(f"hello {name} you are a valid voter  ")
else:
    print(f"Hello {name} you are a not valid voter  ")
#Question 6==>Accept a year from user and check whether it is a leap year or not?
year=int(input("Enter year :"))

if year%4==0 or year%400==0 and year %100 !=0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")
#Question 7==> You cna also create if elif ladder using multiple conditions of elif For understanding solve this question take the input of temperature in celsius.
# Below 0°C → "Freezing Cold 11
#0°C to 10°C → "Very Cold
#10°C to 20°C → "Cold 11
#20°C to 30°C "Pleasant
#30°C to 40°C → "Hot
#Above 40°C → "Very Hot

temp=int(input("enter temprature:"))

if temp<=0:
    print("Frezzing cold")
elif temp<10 and temp>0:
    print("very cold")
elif temp<20 and temp>10:
    print("cold")
elif temp<30 and temp>20:
    print("pleasant")
elif temp<40 and temp>30:
    print("cold")
elif temp>40:
    print("very cold")