#Q4-->Write a python program to combine two dictionary by adding valuesfor common keys

d1={10:100,20:200,30:300}
d2={10:300,30:345,40:700}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
         d1[i]=d2[i]
print(d1)