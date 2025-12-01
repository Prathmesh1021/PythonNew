#Q5 Accept name and age from user.Cheack if the user is a valid voter or not?EX->Hello Rahul you are a valid voter  

name=str(input("Enter Your Name:"))
age=int(input("Enter Your Age :"))

if age>=18:
     print(f"Hello {name} you are a valid voter")
else:
     print(f"Hello {name} you are not a valid voter")
     
######################practice 
print("Practice******************************")
#Q5 Accept name and age from user.Cheack if the user is a valid voter or not? EX->Hello Rahul you are a valid voter 

name =(input("Enter your Name:"))
age =int(input("Enter your Age :"))

if age>=18:
     print(f"Hello {name} you are a valid voter ")
else:
     print(f"Hello {name} you are a not valid voter because your age is {age} year old")