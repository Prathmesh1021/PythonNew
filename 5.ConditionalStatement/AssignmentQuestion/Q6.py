#Question 6==>Accept a year from user and check whether it is a leap year or not?
year=int(input("Enter The Year ="))

if year%400==0 or year % 4 == 0 and year%100!=0:
     print("Leap Year ")
else:
     print("Not a Leap year")

#######################################Practice 
#Question 6==>Accept a year from user and check whether it is a leap year or not?
print("Practice********************************")
year =int(input("Please tell your : "))

if year %400==0 and year % 4 ==0 and year %100 !=0:
     print("Leap year ")
else:
     print("Not a Leap Year ")
