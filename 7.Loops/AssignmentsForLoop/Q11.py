#Q Reverse a string using build function
a="Avigna AI"
print(a[::-1])

#Q Reverse a string without using in build functions

b= "Avigna Ai is the Best Company"
c= ""
for i in range(len(b)-1,-1,-1):
    c = c + b[i]
print(c)