#Question 7==> You cna also create if elif ladder using multiple conditions of elif For understanding solve this question take the input of temperature in celsius.
# Below 0°C → "Freezing Cold 11
#0°C to 10°C → "Very Cold
#10°C to 20°C → "Cold 11
#20°C to 30°C "Pleasant
#30°C to 40°C → "Hot
#Above 40°C → "Very Hot

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