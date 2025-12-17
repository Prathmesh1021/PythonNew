###Q-->Find the second greatest element
a=[3,35,457,2,2153,24,6,36,45,5]
largest=a[0]
sec_largest=a[0]

for i in a:
    if i>largest:
        sec_largest=largest
        largest=i
    elif i>sec_largest:
        sec_largest=i
        
print(sec_largest,largest)