age=int(input("Enter your age :"))
try:
     if age < 10 or age >18:
       raise ValueError("Your age must be between 10 and 18")
     else:
       print("welcome to the club")
except Exception as err:
    print(f"an error occured as {err}")
    
    
print("The club will Stat Soon ")