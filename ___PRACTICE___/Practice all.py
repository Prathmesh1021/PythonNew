## class 1
class Factory:
    a=12
    def hello(self):
        print("how are you")
print("welcome in class")
print(Factory().a)
Factory().hello()
######class 2
class Animal:
    type="dog"
    def sound(self):
        print("bhu bhu")
print(Animal().type)
Animal().sound()
######class 3
class Car:
    wheel=4
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"your car name is {self.name}")
obj=Car("TATA")
obj.show()
#######class 4
class Factory:
    def __init__(self,age):
            self.age=age
    def show(self):
        print(f"your age is {self.age}")
    @classmethod
    def Class1(cls):
        print("this is the class method")
        
    @staticmethod 
    def statsic():
        print("this is the static method")
        
obj=Factory(12)
obj.show()
obj.Class1
obj.statsic

###Constructor Ex1
class Cons:
    def __init__(self,name):
        self.name=name
s=Cons("riya")
print(s.name)
##Const 2
class Cons2:
    def __init__(self,material,zip,pockets):
        self.material=material
        self.zip=zip
        self.pockets=pockets
    def show(self):
        print(f"Your Company details are :{self.material} , {self.zip} , {self.pockets}")
Pune=Cons2("lather",23,24)
Mumbai=Cons2("nylon",23,45)

Pune.show()
Mumbai.show()

###Object
class A:
    a=3123
    def hello(self):
        print("this is the object ")
print(A().a)
A().hello()

##########Creatig list

x=[]

y=[12,34,36,47,548,547,47,4]

z=[23,"akdajd",35432.345,"@$@%%"]

print(x)
print(y)
print(z)

##list methods 
a=[23,33,53,3,6,3,2,36,7,36,74,367]

a.append(542)
a.sort()
print(a)

###Creating algoritham 
mylist=[12,43,36,55,5,35,74,56]
myval=mylist[0]

for i in mylist:
    if i<myval:
        myval=i
        print("lowest value : ",myval)
        
##stack Example
stack=[]
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')
stack.append('F')
stack.append('G')
stack.append('H')
stack.append('I')

print("Stack:",stack)

topelement=stack[-1]
print("Peek:",topelement)

popelement=stack.pop()
print("pop:",popelement)

print("After pop list are :",stack)

isEmpty=not bool(stack)
print("Empty:",isEmpty)

print("size",len(stack))

#stack class 
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
mystack.push('F')
mystack.push('G')

print("Stack:",mystack.stack)
print("peek",mystack.peek())
print("Pop",mystack.pop())
print("After pop stack are ",mystack.stack)
print("Empty ",mystack.isEmpty())
print("size ",mystack.size())

###Syntax of inheritance 
class parent:
    def hello(self):
        print("hello")
class child(parent):
    pass
obj=child()
obj.hello()

##
class Factory:
    a="this is the class attribite mention inside factory"
    def hello(self):
        print("this is the method mention inside factory")
class PuneaFactory(Factory):
    pass
obj=PuneaFactory()
print(PuneaFactory().a)
PuneaFactory().hello()    

##inheritance usig super class 
class Factory:
    def __init__(self,material,zips):
        self.material=material
        self.zips=zips
class PuneFactory(Factory):
    def __init__(self, material, zips,pockets):
        super().__init__(material, zips)
        self.pockets=pockets
    def show(self):
        print(f"your company details are {self.material} , {self.zips} ,{self.pockets}")
Pune=PuneFactory("Nylon",23,25)
Pune.show()

##Single level inheritance 
class parent:

    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your name is {self.name}")
class child(parent):
    pass

obj=child("sudir")
obj.show()

##multilple inheritance 
class Animal:
    def __init__(self,name):
        self.name=name
class Human:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
class Robort(Human,Animal):
    def __init__(self):
        Animal.__init__(self,"Black Panther")
        Human.__init__(self,"Rohit",32)
obj=Robort()
print(obj.name)
print(obj.name1)
print(obj.age)

##inheritance multilevel
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class BhopalFactory(Factory):
    def __init__(self, material, zip,pockets):
        super().__init__(material, zip)
        self.pockets=pockets
class PuneFactory(BhopalFactory):
    def __init__(self, material, zip, pockets,color):
        super().__init__(material, zip, pockets)
        self.color=color
    def show(self):
        print(f"Your Company Details are :{self.material} ,{self.zip} ,{self.pockets} ,{self.color}")
        
obj=PuneFactory("Lahter",2,4,"black")
obj.show()

## hierarcical inheritance 

class MegaFactory:
    def __init__(self,material,zips,pockets,color):
        self.material=material
        self.zips=zips
        self.pockets=pockets
        self.color=color
class PuneFactory(MegaFactory):
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets, color)
    def show(self):
        print("Welcome in Pune Factory")
        print(f"Pune Factory Details:- Materials:-{self.material}  zips:-{self.zips} ,Pockets:- {self.pockets},Color :- {self.color}")
        
class MumbaiFactory(MegaFactory):
    def __init__(self, material, zips, pockets, color):
        super().__init__(material, zips, pockets, color)
    def show(self):
        print("Welcome in Mumbai Factory")
        print(f"Mumbai Factory Details :- Material:-{self.material}, zips:-{self.zips} ,Pockets:- {self.pockets} ,Color :- {self.color}")
obj=MumbaiFactory("lather",2,5,"black")
obj.show()
obj1=PuneFactory("nylon",22,3,"yellow")
obj1.show()

##polymorphisam simple example
def show():
    print("hello")
def show():
    print("hi")
show()

##polymorphisam method overriding example 
class animal:
    def show():
        print("how are you")
class human(animal):
    def show():
        print("what about you")#method overriding
    show()
        
##polymorphiam duck typing example 
class animal:
    def show(self):
        print("i am showing")
class Human:
    def show(self):
        print("i am also showing")
obj1=animal()
obj2=Human()

obj1.show()
obj2.show()
##functional Approch
def add(a,b):
    return a+b
print(add(12,34))
print(add(23,45))
#Imparative Approch
a=13
b=34
print(a+b)

#####public Attributes method Example In Encapsulation 
class Animal:
    a="This is the Public Attribute"
    def show(self):
        print("This is the Public Method")
class Human(Animal):
    def show2(self):
        print(super().a)
obj=Human()
obj.show()
obj.show2()

##Protected Encapsulation

class Factory:
    _a="This is the Protected Attribute"
    def _show(self):
        print("This is the Protected Method ")
class Bhopal(Factory):
    def show2(self):
        print(super()._a)
obj=Bhopal()
obj.show2()
obj._show()

##Private not accesseble 
class Animal:
    __a="12 This is the Private Attribute"
    def __show(self):
        print("This is the Private Method")
class Human(Animal):
    def show(self):
        print(super().__a)#does not access private method
#obj=Human()
#obj.show()
#obj.__show()

##private Attribute Method Example with acceseeing Class 
class Factory:
    __a="THIS ONE PRIVATE ATTRIBUTE"
    def show(self):
        print(Factory().__a)
obj=Factory()
obj.show()

####Private public And Protected in one class 

class Factory:
    def __init__(self):
        self.name="Prathmesh Patil"#public
        self._age=21#protected 
        self.__salary=5000#private
    def show(self):
        print("inside the class ")
        print("name:",self.name)
        print("age:",self._age)
        print("Salary:",self.__salary)
obj=Factory()
obj.show()

##Dander Method 
class Animal:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"hello how are you and your name is {self.name}"
obj=Animal("tiger")
print(obj)

##Dander method Add 
class Factory:
    def __init__(self,age):
        self.age=-age
    def __add__(self,other):
        sum=0
        for i in other:
            sum=sum+i.age
            return f"your sum of numbers are {self.age +sum}"
obj=Factory(12)
obj1=Factory(15)
obj2=Factory(11)

print(obj+ (obj2,obj1))

###Ternary Operation 
a=12
print("even") if a%2==0 else print("odd")
            
##comperehension 
#list
l=[i for i in range (1,21)if i%2==0]
print(l)

#Dictionary
D={i:i**2 for i in range (1,11)if i%2==0}
print(D)

#Set
S={i*i for i in range(1,21)if i%2==0}
print(S)

