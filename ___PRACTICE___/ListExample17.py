#Q-->find the Greatest element and print its index too.
a=[12,23,4,242,34,456,36]
largest=a[0] 
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
        index=i
print(f"largest value in list {largest} and index is {index}")
