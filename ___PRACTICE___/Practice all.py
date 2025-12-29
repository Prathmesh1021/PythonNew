##class 
#class Simple Example 
class Animal:
    a=10
    def hello(self):
        print("hello how are you")
print("welcome in class")
print(Animal().a)
Animal().hello()
#class Example 2
class Animal:
    b="Dog"
    def sound(self):
        print("BhuBhu")
print(Animal().b)
Animal().sound()
##class Example Car 
class Car:
    def __init__(self,name):
        self.name=name 
    def show(self):
        print(f"Your car name is {self.name}") 
obj=Car("TATA")
obj.show() 
##Class All Exmple 4
class Factory:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"Your Age is {self.age}")
    @classmethod
    def class1(cls):
        print("this is class method")
    @staticmethod
    def static():
        print("this is static method")
obj=Factory(12)
obj.show()
obj.static()
obj.class1()
#######################################################################################
##constructors 
#sample Example Constructor 
class A:
    def __init__(self,name):
        self.name=name
s=A("sunita")
print(s.name)
###Constructor 2 Example 
class C2:
    def __init__(self,material,zip,pocket):
        self.material=material
        self.zip=zip
        self.pocket=pocket
    def show(self):
        print(f"Hello Your company details are: {self.material}, {self.zip}, {self.pocket} ")
obj=C2("nylone ",12,34)
obj.show()
#################################################################################################
#Object Example 
class Object:
    a=4235252
    def hello(self):
        print("hello")
print(Object().a)
Object().hello()
########################################################################################
##Pytjon list and Array 
#Creating list
l=[]
m=[12,13,24,35,46,65,56,7,4]
n=[12,13.234,"234",True,print()]
print(l)
print(m)
print(n)
###List method
list=[12,243.67,79,13,5]
list.append(23)
list.sort()
print(list )
##Creating algorithrm 
mlist=[12,2,34,65,25,25,7]
mv=mlist[0]
for i in mlist:
    if i < mv:
        mv=i
print(f"Lowest Value:",mv)
###############################################################################
#Stacks
#Stack Example 1 Without class 
stack=[]
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print("Stack:",stack)
topelement=stack[-1]
print("Peek",topelement)
popelement=stack.pop()
print("Pop:",popelement)
print("After pop stack is ",stack)
isEmpty=not bool(stack)
print("Empty",isEmpty)
print("Size",len(stack))
###Stack With class 
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    def pop(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
mystack=Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.push('D')
mystack.push('E')
print("Stack:",mystack.stack)
print("Peek:",mystack.peek())
print("Pop:",mystack.pop())
print("After pop stack is ",mystack.stack)
print("Empty",mystack.isEmpty())
print("Size:",mystack.size())
###########################################################################################
#inheritance 
#sample Example 
class Parent:
    a="This is class Attributes"
    def hello(self):
        print("hello How are you")
class child(Parent):
    pass
obj=child()
print(obj.a)
print(obj.hello())
#Inheritance using super class 
class parent:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
    
class child(parent):
    def __init__(self, material, zip,pocket):
        super().__init__(material, zip)
        self.pocket=pocket
    def show(self):
        print(f"Your Comapy Details {self.material} ,{self.zip} ,{self.pocket}")
obj=child("nylone",12,2)
##single level 
class Animal:
    a="this is class Attribute for single level"
    def hello(self):
        print("this is single level method")
class Human(Animal):
    pass
obj=Human()
print(obj.a)
print(obj.hello())
##multiple 
class Animal:
    def __init__(self,name):
        self.name=name
class Human:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
class Robort(Human,Animal):
    def __init__(self):
        Animal.__init__(self,"Tiger")
        Human.__init__(self,"Rushikesh",26)
obj=Robort()
print(obj.name)
print(obj.name1)
print(obj.age)    
##multilevel
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class PuneFactory(Factory):
    def __init__(self, material, zip,pockets):
        super().__init__(material, zip)
        self.pockets=pockets
class MumbaiFactory(PuneFactory):
    def __init__(self, material, zip, pockets,color):
        super().__init__(material, zip, pockets)
        self.color=color
    def show(self):
        print(f"Your Company Details Are :{self.material} ,{self.zip} ,{self.pockets} ,{self.color}")
obj=MumbaiFactory("Lather",1,4,"Black")
obj.show()
##Hierarchical inheritance 
class Factory:
    def __init__(self,material,zip,pockets,color):
        self.material=material
        self.zip=zip
        self.pockets=pockets
        self.color=color
class PuneFactory(Factory):
    def __init__(self, material, zip, pockets, color):
        super().__init__(material, zip, pockets, color)
    def show(self):
        print(f"Pune Company Details are : {self.material} ,{self.zip} ,{self.pockets} ,{self.color}")     
class MumbaiFactory(Factory) :
    def __init__(self, material, zip, pockets, color):
        super().__init__(material, zip, pockets, color)
    def show(self):
        print(f"Mumbai Company Details are : {self.material} ,{self.zip} ,{self.pockets} ,{self.color}")  
#########################################################################################################################
#Poly-Morphisam
def show():
    print("hi")
def show():
    print("hello")
show()
 #Poly Overriding
class Animal:
    def show(self):
        print("hello how are you")
class Human(Animal):
    def show(self):
        print("hello what about you")
obj=Human()
obj.show()
###Duck Typing
class Animal:
    def show(self):
        print("i am showing")
class Human:
    def show(self):
        print("i am also showing")
obj1=Animal()
obj1.show()
obj=Human()
obj.show()
##Functiuonal Approach
def addition(a,b):
    return a+b
print(addition(12,23))
##imparetive Approach
a=10
b=14
print("Addition :-",a+b)
############################################################################################
#Encapsulation 
#Public 
class Animal:
    a="This is the public attribute"
    def show(self):
        print("This is the Public Method")
class Human(Animal):
    def show1(self):
        print(super().a)
obj=Human()
obj.show()
obj.show1()
#protected
class Animal:
    _a="This is the Protected attribute"
    def _show(self):
        print("This is the Protected Method")
class Human(Animal):
    def show1(self):
        print(super()._a)
obj=Human()
obj._show()
obj.show1()
#Private no accsess
class Animal:
    __a="This is the Private attribute"
    def __show(self):
        print("This is the Private Method")
class Human(Animal):
    def show1(self):
        print(super()._a)
#obj=Human()
#obj._show()
#obj.show1()

###Private accsess with class 
class Animal:
    a="this is the private method "
    def show(self):
        print(Animal().a)
obj=Animal()
obj.show()
##Public private protected 
class Factory:
    def __init__(self):
        self.name="Prathmesh"
        self._age=12
        self.__Salary=12131
    def show(self):
        print("Inside Class")
        print("Name:",self.name)
        print("Age",self._age)
        print("Salary",self.__Salary)
        
obj=Factory()
obj.show()
######################################################################################
#Dunder Method 
class Factory:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"hello {self.name} how are you?"
obj=Factory("Pritam Das")
print(obj)
## Addition of two ages 
class D:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        sum=0
        for i in other:
            sum=sum+i.age
            return f"your sum of ages are :{self.age+ sum}"
obj=D(12)
obj1=D(34)
obj2=D(23)
print(obj+(obj1,obj2))
##################################################################################
##ternary Operator Even
a=12
print("Even") if a%2==0 else("false")
##Comphrehension list
l=[i for i in range (1,31) if i %2==0 ]
print(l)
##Comphrehension Dictionary
d={i:i*2 for i in range (1,10) if i%2==0}
print(d)
##Comphrehension Set
s={i*i for i in range(1,9) if i%2==0}
print(s)
#######################################################################################
#AbstractionMethod 
from abc import ABC,abstractmethod
class abstract (ABC):
    @abstractmethod
    def perimeter (self):
        pass
    @abstractmethod
    def area (self):
        pass
class square (abstract):
    def __init__(self,side):
        self.side=side
    def perimeter (self):
        print("i have created ")
    def area(self):
        print("i have also created")
class Circle (abstract):
    def __ini__(self,radious):
        self.radious=radious
    def perimeter(self):
        print("i have created ")
    def area(self):
        print("i have also created")
#obj=Circle(7)
#obj=square(4)
####################################################################################
#decorators
#Sample Example Print 
def decorate (func):
    def wrapper():
        print("Before the Print")
        func()  
        print("After the Print")
    return wrapper
@decorate
def hello():
    print("hello i am prathmesh")
hello()

#Addition of 2 Example Using Decorators 
print("********************")
def decorate (func):
    def wrapper(a,b):
        print("Before the Print")
        func(a,b)  
        print("After the Print")
    return wrapper
@decorate
def hello(a,b):
    print(f"Addition is : {a+b}")
hello(12,34)
#Args
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(1,2,3,4,5,6,7,8,9)
#kwargs
def information(**kwargs):
    print("your information is ")