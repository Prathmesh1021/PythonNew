#use Kwargs for display information
def information(**kwargs):
  print("your information is :")
  for i in kwargs:
      print(f"{i}:{kwargs[i]}")
    
information (name="prathmesh",age=23,designation ="Developer")