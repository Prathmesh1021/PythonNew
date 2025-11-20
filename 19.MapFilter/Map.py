#Using Map And Lambda do squere operation
a=[1,2,3,4,5]

result= map (lambda x:x*2 ,a)

print(list(result))

#Normal Functions way
a=[1,2,3,4,5]

def double(x):
    return x*2
result=map(double,a)
print(list(result))