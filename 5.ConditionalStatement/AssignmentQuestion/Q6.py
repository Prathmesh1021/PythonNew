#Question 6==>Accept a year from user and check whether it is a leap year or not?
year=int(input("Enter The Year ="))

if year%400==0 or year % 4 == 0 and year%100!=0:
     print("Leap Year ")
else:
     print("Not a Leap year")