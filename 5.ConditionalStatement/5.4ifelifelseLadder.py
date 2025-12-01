temp=int(input("Enter Temperature : "))

if temp< 0 :
   print("Freezing Cool")
elif temp>0 and temp<10:
   print("Very Cool")
elif temp>10 and temp<20:
   print("Cold")
elif temp>20 and temp<30:
   print("Pleasant")
elif temp>30 and temp<40:
   print("Hot")
elif temp >40:
   print("Very Hot")
else:
    print(" warning!!! Please Enter the Temparature ")
    
##########################################Practice 
#elif ladder 

t=int(input("Enter your temperature "))

if t<0:
     print("Freezing cool")
elif t>0 and t<10:
     print(" very cold")
elif t>10 and t<20:
     print("cool")
elif t>20 and t<30:
     print("pleasant")
elif t>30 and t<40:
     print("hot")
elif t>40:
     print("Very Hot")
else:
     print("Enter valid value ")