#Q Check String pallindrome or Not 

b= "naman"
c= ""
for i in range(len(b)-1,-1,-1):
    c = c + b[i]

if c==b:
    print("your String is pallindrome")
else:
    print("its not a pallindrome")