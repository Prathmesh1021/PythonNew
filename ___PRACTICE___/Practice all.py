#
class A:
    a=12
    def hello(self):
        print("how are you")
print("welcome in class")
print(A().a)
A().hello()
#
class B:
    type="dog"
    def sound(self):
        print("bhubhu")
print(B().type)
B().sound()

#
class Car:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your car name is {self.name}")
s=Car("creta")
s.show()
        
#
class D:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"your age is {self.age}")
    @classmethod
    def class1(cls):
        print("this is the class method")
    @staticmethod
    def static():
        print("this is the static method")
obj=D(23)
obj.show()
    
# constructors 
class Cons:
    def __init__(self,name):
        self.name=name

s=Cons("riya")
print(s.name)

#constructor Ex2
class Factory:
    def __init__(self,m,z,p):
        self.m=m
        self.z=z
        self.p=p
    def show(self):
        print(f"Your Company Details are: {self.m} {self.z} {self.p}")
pune=Factory("Lather",23,76)
mumbai=Factory("nylone",34,65)
pune.show()
mumbai.show()
###Python list and array
##creating List 

x1=[]
y1=[1,23,4,5,6,7,8,9]
z1=[2,"sfs",33.22,"@@$&$&$"]
print(x1)
print(y1)
print(z1)

##
g=[12,35,35,36,435,53,35,35622,22,244,221]
g.append
g.sort()
print(g)
##
mylist=[1,42,36,74,473,25,36,3]
myval=mylist[0]

for i in mylist:
    if i<myval:
        myval=i
        print("lowest number :",myval)
    
##Stack Example
stack=[]

stack.append('A')
stack.append('B')
stack.append('C')

print("stack:",stack)

#peek 
tp=stack[-1]
print("Peek:",tp)

#pop
pt=stack.pop()
print("Pop:",pt)

#After pop stack 
print("After pop stack is :",stack)

#empty
iE=not bool (stack)
print("Empty",iE)

#size 
print("Size:",len(stack))

###Class Stack
class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0

    def size(self):
        return len(self.stack)
    
mystack=Stack()

mystack.push('A')
mystack.push('B')
mystack.push('C')

print("stack:",mystack.stack)
print("pop:",mystack.pop())
print("After pop stack are :",mystack.stack)
print("peek :",mystack.peek())
print("Empty:",mystack.isEmpty())
print("Size:",mystack.size())      

##inheritance syntax

class parent:
    def a():
        print("hello")
class child(parent):
    pass 
        

                 