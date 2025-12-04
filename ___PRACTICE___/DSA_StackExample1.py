#stack Example 1
stack=[]

stack.append('A')
stack.append('B')
stack.append('C')

print("Stack:",stack)

#peek 
TopElement=stack[-1]
print("Peek:",TopElement)

#POP
popelement=stack.pop()
print("pop:",popelement)

#After Pop Stack 
print("After pop Stack:",stack)

#is Empty
isempty=not bool(stack)
print("isEmpty:",isempty)

#size
print("size:",len(stack))