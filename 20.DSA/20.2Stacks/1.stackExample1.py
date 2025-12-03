#Using Python list as Stack 
stack =[]
#push
stack.append('A')
stack.append('B')
stack.append('C')

print("Stack:",stack)

# peek 
TopElement=stack[-1]
print("Peek:",TopElement)

#Pop
PopElement=stack.pop()
print("Pop:",PopElement)

#stack after pop
print("Stack After pop :",stack)

#is Empty

isEmpty =not bool(stack)
print("Empty:",isEmpty)

#Size
print("Size:",len(stack))

