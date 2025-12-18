#Q3-->Count the Frequency of each elements in a list 

a=[1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,6,7,8,9]

d={}

for i in a:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] =1   
print(d)
