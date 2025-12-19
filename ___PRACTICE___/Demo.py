#crud Ditionary 

d={10:100,20:200,30:300,40:400,50:500}
d[10]=1000 #updating
d[60]=600 #creating 
del d[40]  ##deleting
print(d) #read

##demo Dict

d1={10:100,20:200,30:300,40:400,50:500}
print(d1[50])

##merge two pthon dict 
d2={10:100,20:200,30:300}
d3={40:400,50:500,60:600}

for i in d3:
   d2[i]=d3[i]
print(d2)

##sum of all values in dict
d2={10:100,20:200,30:300}
sum=0
for i in d2:
    sum=sum+d2[i]
print(sum)
###Count Frequency of Each elements 
#Q3-->Count the Frequency of each elements in a list 

a=[1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,6,7,8,9]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)    

###Q4-->Write a python program to combine two dictionary by adding valuesfor common keys

d1={10:100,20:200,30:300}
d2={10:300,30:345,40:700}
    
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)

##Sample For 
print("********************")
for i in range(12,32,5):
    print(i)
##20 t0 50
print("********************")
for i in range (20,51,1):
    print(i)
##16 to -1
print("********************")
for i in range (16,-2,-1):
    print(i)
##-3 to -15
print("********************")
for i in range (-3,-16,-1):
    print(i)
#lets print table of 5
print("********************")
for i in range(5,51,5):
    print(i)
#to print using for loop charector 
print("********************")
a="prathmesh"
for i in range(len(a)):
    print(a[i])
##to print using lenght
print("********************")

l="Prathmesh Patil Intern At Avigna Ai"
len(l)
for i in range(len(l)):
    print(l[i])