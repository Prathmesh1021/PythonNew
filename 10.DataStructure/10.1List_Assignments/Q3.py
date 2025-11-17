#Q-->find the Greatest element and print its index too.

a=[5,2,9,1,5,6,]
largest=a[0]
for i in range (len(a)):
    if a[i] >largest:
        largest=a[i]
        index = i
        
print(f"your largest number is {largest} at {index}")
        
