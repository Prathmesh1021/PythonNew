######################################################################################################

class Animal:
    a=12
    def hello(self):
        print("hello how are you")
print("Welcome in class")
print(Animal().a)
Animal().hello()

class animal:
    a="dog"
    def sound(self):
        print("bhubhu")
print(animal().a)
animal().sound()

class Car:
    wheel=4
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"hello your car name is {self.name}")
obj=Car("creta")
obj.show()

class Factory:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"your age is {self.age}")
    @classmethod
    def class1(cls):
        print("This is the class method")
    @staticmethod
    def static():
        print("this is the class method")
obj=Factory(12)
obj.show()
obj.class1()
obj.static() 
#####################################################################################
#Constructors       
class C:
    def __init__(self,name):
        self.name=name
s=C("Riya")
print(s.name)        

class C2:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
    def show(self):
        print(f"details are {self.material} ,{self.zip}")
obj=C2("Nylone",23)
obj.show()
#################################################################################
class object:
    a=12
    def hello(self):
        print("hello how are you ")
obj=object()
print(obj.a)
obj.hello()
###################################################################################
#create a list Example
x=[]
y=[12,24,56,6578,4785,373,36,47]
z=[13,"uyfweu",344.4634,True,"@#$@%@"]
print(x  ,y    ,z)

#list method .py
l=[123,34,254,25,45,68,658,68]
l.append(3432)
l.sort()
print(l)

##create algoritham
mylist=[12,35,645,2,353,536322,4]
myval=mylist[0]
for i in mylist:
    if i<myval:
        myval=i
print("lowest number", myval)

## 
stack=[]

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')

print("Stack",stack)

topelement=stack[-1]
print("peek",topelement)

popelement=stack.pop()
print("pop",popelement)

print("After pop stack is :",stack)

isEmpty=not bool(stack)
print("Empty",isEmpty)

print("size",len(stack))


class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
    def peek(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.stack[-1]
    def pop(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.stack.pop()
    def isEmpty (self):
        return len(self.stack)==0
    def size (self):
        return len(self.stack)

mystack=Stack()

mystack.push('A')    
mystack.push('B')    
mystack.push('C')    
mystack.push('D')    
mystack.push('E')

print("stack",mystack.stack)
print("peek",mystack.peek())
print("pop",mystack.pop())
print("After pop Stack is",mystack.stack)
print("Empty",mystack.isEmpty())
print("Size",mystack.size())  
###############################################################
class parent :
    a="this is class attributes"
    def hello(self):
        print("hello how are you ")
class child(parent):
    pass
obj=child()
print(obj.a)
obj.hello()

## Inheritance using super class 
class Animal:
    def __init__(self,material,zip,pockets):
        self.material=material
        self.zip=zip
        self.pockets=pockets
class Human(Animal):
    def __init__(self, material, zip, pockets,color):
        super().__init__(material, zip, pockets) 
        self.color=color
    def show(self):
        print(f"Details are {self.material} ,{self.zip} ,{self.pockets}, {self.color}")
obj=Human("lather",13,34,"black")
obj.show()
    
#3single level
class parent:
    def hello(self):
        print("hello how are you single level inheritance")
class child(parent):
    pass
obj=child()
obj.hello()

##multilevel inheritance 
class Animal:
    def __init__(self,name):
        self.name=name
class Human:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
        
class Robort(Human,Animal):
    def __init__(self):
        Animal.__init__(self,"tiger")
        Human.__init__(self,"Adhira",11)
obj=Robort()
print(obj.name)
print(obj.name1)
print(obj.age)

##multilevel inheritance 
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class Bhopal(Factory):
    def __init__(self, material, zip,pockets):
        super().__init__(material, zip)        
        self.pockets=pockets
class Pune(Bhopal):
    def __init__(self, material, zip, pockets,color):
        super().__init__(material, zip, pockets)
        self.color=color
    def show(self):
        print(f"your comany details are :-{self.material} ,{self.zip} ,{self.pockets} ,{self.color}")

obj=Pune("lather",223,34,"blue")
obj.show()
#####hier
class Factory:
    def __init__(self,material,zip,pocket,color):
        self.material=material
        self.zip=zip
        self.pocket=pocket
        self.color=color
class Pune(Factory):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket, color)
    def show(self):
        print(f"Pune company details are : {self.material} ,{self.zip} ,{self.pocket}, {self.color}")
class Mumbai(Factory):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket, color)
    def show(self):
        print(f"Pune company details are : {self.material} ,{self.zip} ,{self.pocket}, {self.color}")

obj=Pune("Nylon",23,43,"red")
obj1=Mumbai("Lather",3,4,"pink")

obj.show()
obj1.show()
#####################################################################################
#poly simple Example 
def show():
    print("Hello")
def show():
    print("Hello how are you")
show()    
###poly overriding 
class Animal:
    def show(self):
        print("hello how are you and welcome poly")
class Human(Animal):
    def show(self):
        print("hello I am fine ")
obj=Human()
obj.show()
##Duck typing
class Animal:
    def show(self):
        print("i am showing")
class Human:
    def show(self):
        print("i am also showing")
obj=Animal()
obj.show()
obj1=Human()
obj1.show()
#####################################################################################
##Encapsulation
#public
class Factory:
    a="this is the class public attributes"
    def show1(self):
        print("hello welcome in public method")
class Pune(Factory):
    def show2(self):
        print(super().a)
obj=Pune()
obj.show1()
obj.show2()
#protected 
class Animal:
    _b="This is the Protected Attributes"
    def _show3(self):
        print("hello welcome in protected Method")
class Human(Animal):
    def _show4(self):
        print(super()._b)
obj=Human()
obj._show3()
obj._show4()
#Private not access 
class Animal:
    __a="this is the private attributes"
    def __show(self):
        print("hello welcome in private method")
class Human(Animal):
    def show(self):
        print(super().__a)
obj=Human()
#obj.__show() ## not acces private Encapsulation
#obj.show() ## not acces private Encapsulation

##private access with class 
class Factory:
    __a="This is the private Attribute with acsess Class"
    def show(self):
        print(Factory().__a)
obj=Factory()
obj.show()
#####Public Protected Private 
class Factory:
    def __init__(self):
      self.name= " Pritam Das" #public
      self._age=12 #protected 
      self.__salary=23000 #private 
      
    def show(self):
        print("inside the class")
        print("Name:",self.name)
        print("Age:",self._age)
        print("Salary:",self.__salary)
obj=Factory()
obj.show()

#################################################################################
#dunder init str
class A:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"hello how are you and your name is {self.name}"     
obj=A("Rushikesh")
print(obj)   

###Dunder init and Add
class B:
    def __init__(self,age):
        self.age=age
    def __add__(self, other):
        sum=0
        for i in other:
            sum=sum+i.age
            print("sum of ages are :",self.age +sum)
obj=B(12)
obj1=B(10)
obj2=B(10)
print(obj+(obj1,obj2))

####################################################################################
#Ternary operators 
a=11
print("Even") if a%2==0 else print("odd")
#####################################################################################
#comprehensions 
#list 
l=[i for i in range(1,31) if i%2==0 ]
print(l)
#Dictionary
d={i:i**2 for i in range(1,10) if i%2==0}
print(d)
#Set
s={i*i for i in range (1,10) if i%2==0}
print(s)
###########################################################################################
##Abstraction
from abc import ABC,abstractmethod 
class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Square (abstract):
    def __init__(self,side):
        self.side=side
    def perimeter (self):
        print("i have class")
    def area(self):
        print("i have also class")
class Circle (abstract):
    def __init__(self,radious):
        self.redious=radious
    def perimeter(self):
        print("i have class")
    def area(self):
        print("i also have a class")
obj=Circle(7)
obj=Square(2)    
####################################################################################
#Decorators 
def decorate (fun):
    def Wrapper():
        print("Before")
        fun()
        print("after")
    return Wrapper
@decorate
def hello():
    print("hello")
hello()
#decorator addition using 
def decorate (func):
    def wrapper(x,y):
        print("after")
        func(x,y)
        print("before")
    return wrapper
@decorate
def add(x,y):
    print(f"Addition is {x+y}")
add(20,34)
##Args 
def addition(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
addition(12,23,43,25,25,25,2,52)
     
###Kwargs 
def information(**kwargs):
    print("Your Information is")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")
information(name="Swapnil",age =28,address="pune")

######Args Kargs
def decorate(func):
    def wrapper(*args,**kwargs):
        print("Your Addition is :")
        func(*args,**kwargs)
        print("thank you i hope you like it ")
    return wrapper    
@decorate
def addition(a,b,c,d,e,f):
    print(f"Total is{a+b+c+d+e+f}")
addition(10,20,30,40,50,60)
######################################################################################
#lambada sample addition
add=lambda x,y:x+y
print(add(13,32))
##Use Ternary in Lambda 
a=lambda c:"even"if c%2==0 else "odd"
print(a(11))
#########################################################################################
###map Example1
a=[1,2,3,4,5,6]
result=map(lambda x:x*2,a)
print(list(result))
###map normal method
a=[1,2,3,4,5]
def double(x):
    return x*2
result=map(double,a)
print(list(result))
#############################################################################################
# Filter Normal Function 
def even(x):
    if x%2==0:
        return True
    else:
        return False
a=[1,2,3,4,5,6,7,8,9]
result=filter(even,a)
print(list(result))
##Filter with lambda 
a=[1,2,3,4,5,6]
result=filter(lambda x:x if x%2==True else False,a )
print(list(result))
####################################################################################
##Data Types
##Numbric Values 
a=10
b=12.3
d="342"
e=34j
print(type(a))
print(type(b))
print(type(d))
print(type(e))

##Boolen Values 
a=True
b=False
print(type(a))
print(type(b))

##String 
a="Hello How are you"
b="A"
print(ord(b))
d=86
print(chr(d))
e="Rushikesh Power"
print(e[6])#Indexing
print(e[2:7:1])#slicing
####################################################################################
####Type conversion 
#int to str 
a=12
a=str(a)
print(type(a))

#str to int 
b="23"
b=int(b)
print(type(b))

##for boolean 
a=10
print(bool(a))
b=12.3
print(bool(b))
c="narendra"
print(bool(c))
d=0
print(bool(d))
e=12j
print(bool(e))
f=[]
print(bool(f))
g={}
print(bool(g))
#######################################################################################
#Input Output
#formated string
name="Prathmesh Patil"
age=23
print(f"Hello {name} your age is {age}")

##non formated String 
name="akash mulik"
age=12
print(f"hello ",name,"your age is ",age)

##traking input from user 
#name=(input("Enter your Name "))
#age=int(input("enter your age "))
print(f"your name is {name} and your age is {age}")
###########################################################################################
### arithmatic operations 
a=10
b=5
print("Addition",a+b)
print("Addition",a-b)
print("Addition",a*b)
print("Addition",a/b)
print("Addition",a//b)
print("Addition",a**b)

##Assignmesnt 
a==10
print(a)

##compound 
a=10
print(a)
a+=20
print(a)
a-=2
print(a)
a*=2
print(a)
a/=2
print(a)
a**2
print(a)

#comparision 
a=12
b=12.1
print(a>b)
print(a<b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a>10)
print(a<10)
print(ord("A"))
print(ord("B"))
##logical operator 
print(12>232 and 122>43 and 22432>4342423)
print(12>2 and 35432>4534 and 43<3434)
print(2134>4534 or 24<4 or 643<432)
print(232425>452 or 342525<525 or 2334>521)
print(not 232>342 )
print(not 232<342 )
####################################################################################
#Conditional Statement 
##gretest number 
a=13
b=12
if a>b:
    print(f"{a} is grether than {b}")
else:
    print(f"{b} is grether than {a}")

##input from user 
a=int(input("Enter your First Number:"))
b=int(input("Enter your Second Number:"))

if a>b:
    print(f"{a} is grether than {b}")
else:
    print(f"{b} is grether than {a}")
    
##gender 
gen=(input("Enter Your Gender :"))

if gen == "male" or gen =="Male" or gen=="MALE":
    print("Hello Good Morning Sir")
elif gen == "fmale" or gen =="Fmale" or gen=="FMALE":
    print("Good Morniung Madam")
else:
    print("Enter valid value")

##Check even odd from user
n=int(input("Enter your Number:"))
if n%2==0:
    print("Even")
else:
    print("odd")

##Voter valid or not 
name=(input("Enter your name :"))
age=int(input("Enter your age:"))

if age>=18:
    print(f"hello {name} you are valid voter")
else:
    print(f"Sorry {name} you are not valid voter ")
    
#cleap or not 
year=int(input("Enter your year:"))

if year%4==0 and year%400==0 and year%100!=0:
    print(f"{year }Leap Year")
else:
    print(f"{year} is not a leap year ")
#elif ladder 
temp=int(input("Enter your temparature :"))

if temp<0:
    print("Frezzing cool")
elif temp>0 and temp<10:
    print("Very Cool")
elif temp>10 and temp<20:
    print("Cool")
elif temp>20 and temp<30:
    print("normal")
elif temp>30 and temp<40:
    print("hot")
elif temp<40:
    print("Very Hot")   
###################################################################################
##break 
for i in range (1,24):
    if i==8:
        break
    print(i)
##continue
for i in range(1,25):
    if i==15:
        continue
    print(i)
######################################################################################
##function 
#sample function Structure 
def hello():
    print("hello world")
hello()
##Using Argument Addition
def add(a,b):
    print(f"Addition {a+b}")
add(12,32)
##keyword Argument 
def hello(name,age):
    print(f"your name is {name} and age is {age}")
hello("sudhir",12)
##Default keyword
def info(name,age=23):
    print(f"hello {name} and your age is {age}")
info("Govind")
##pallindrome 
def pallindrome(st):
    rev=""
    for i in range (len(st)-1,-1,-1):
        rev=rev+st[i]  
    if rev==st:
        print(f"{st} is pallendrome")
    else:
        print(f"{st} is not pallendrome")
        
pallindrome("naman")
pallindrome("sakshi")
pallindrome("anam")
pallindrome("123456789987654321")  

#function with return 
def sub(a,b):
    return f"Substraction {a-b}"
print(sub(12,2))
    
        
        