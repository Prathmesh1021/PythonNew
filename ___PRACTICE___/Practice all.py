#class example using attributes and methods 
class A:
    a=13
    def hello(self):
        print("how are you")
print("welcome in class ")
print(A().a)
A().hello()
#attribute And Method
class B:
    type ="dog"
    def sound(self):
        print("bhu bhu")
print(B().type)
B().sound()
##Claass Attributes instance attributes
class Car :
    def __init__(self,name ):
        self.name=name
    def show(self):
        print(f"welcome in {self.name}")
obj=Car("TATA")
obj.show()

###Class All method and Attributes 
class D:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"Your age is {self.age}")
    @classmethod
    def class1(cls):
        print("this is the class method")
    @staticmethod
    def static():
        print("this is the static method")

obj=D(221)
obj.show()
obj.class1
obj.static

##constructors 1

class C1:
    def __init__(self,name):
         self.name=name
obj=C1("riya")

print(obj.name)

#const 2
class C2:
    def __init__(self,m,z,p):
        self.m=m
        self.z=z
        self.p=p
        
    def show(self):
        print(f"your compay details are : {self.m},{self.z},{self.p}")

pune=C2("Lather",23,45)
mumbai=C2("nylon",43,32)

pune.show()
mumbai.show()

#object 

class object1:
    a=12
    def hello(self):
        print("how are you bro ")
print(object1().a)
object1().hello()
#List Method 
x=[]
y=[121,34,1,52,4]
z=["sd",34,"#@$%@"]

print(x)
print(y)       
print(z)
 
 #Algorithm Example
list=[2143,452,25,52,25]
list.append(5624)
list.sort()
print(list)

list=[23442,24,2,522,2]
v=list[0]

for i in list:
    if i <v:
        v=i
        print("Lowest value:",v) 
#Stack Example   
stack=[]
stack.append('A')
stack.append('B')
stack.append('C')
te=stack[-1]
print("peek:",te)
pe=stack.pop()
print("pop",pe)
print("after pop",stack)
ie=not bool (stack)
print("Empty",ie)
print("size",len(stack))

#Class Stack Example 
class S1:
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
            return "stack is empty"
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
        
mystack=S1()

mystack.push('A')
mystack.push('B')
mystack.push('C')

print("Stack:",mystack.stack)
print("peek:",mystack.peek())
print("pop",mystack.pop())
print("After stack pop are ",mystack.stack)
print("Empty ",mystack.isEmpty())
print("size:",mystack.size())


##inheritance Syntax
class parent:
    def hello(self):
        print("hello welcom in avignaai")
class child(parent):
    pass
obj=child()
obj.hello()


## Attributes method using inheritance 
class P:
    a="This is Class Attribute"
    def h(self):
        print("this is method attribute")
class C(P):
    pass
obj=C()
print(C().a)
obj.h()
    
##class USing Super class Example
class AB:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your name is {self.name}")
        
class BA(AB):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
        
    def show(self):
        print(f"Your name is {self.name} And your age is {self.age}")
obj=BA("Rohit",23)
obj.show()

##Single Level Inheritance 
class Animal:
    def __init__(self,name):
        self.name=name
        
    def show(self):
        print(f"Your name is {self.name}")
class Human(Animal):
    pass
obj=Human("Prathmesh")
obj1=Animal("Lion")

obj.show()
obj1.show()

### multiple inheritance 
class Animal:
    def __init__(self,name ):
        self.name=name
class Human:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
class Robort(Human,Animal):
    def __init__(self, name1, age):
        super().__init__(name1, age)
        
    def __init__(self):
        Animal.__init__("Tiger")
        Human.__init__("Akash","Lion")

###Multilevel inheritance 
#Factory -->material,zip
#Bhopal Factory-->maerial,zip,color
#pune Factory-->material,zip,color,pockets
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

#obj=PuneFactory()


###hierarchical

class FactoryF:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class BhopalF(FactoryF):
    def __init__(self, material, zip,pockets):
        super().__init__(material, zip)
        self.pockets=pockets
class PuneF(BhopalF):
     def __init__(self, material, zip, pockets):
         super().__init__(material, zip, pockets)
         
class PuneF(FactoryF):
    def __init__(self, material, zip):
        super().__init__(material, zip)
        
        
        
        
        
        
######syntax inheritance 

class parent:
    def hello(self):
        print("Hello welcome in Ai")
class Child(parent):
    pass

obj=Child()
obj.hello()

##inheritance parent child using attributribues method 

class Parent:
    a="This is the class method"
    def hello(self):
        print("this is the method mention")
class  Child(Parent):
    pass
obj=Child()
print(Child().a)
obj.hello()

##inheritance using super class 
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
    
        
class Pune(Factory):
    def __init__(self, material, zip,color):
        super().__init__(material, zip)
        self.color=color
    
    def show(self):
        print(f"your comapny details are :{self.material},{self.zip},{self.color}")

obj=Pune("lather",12,34)
obj.show()

##single leve

class parent:
    def hello(self):
        print("hello i am Prathmesh")
class child(parent):
    pass
obj=child()
obj.hello()

##multiple inheritance 

class Animal:
    def __init__(self,name):
        self.name=name
class Human:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
        
class Robort(Human,Animal):
    def __init__(self):
        Animal.__init__(self,"lion")
        Human.__init__(self,"rahul",46)
        
obj=Robort()
print(obj.name)
print(obj.name1)
print(obj.age)

##multilevel 

class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class BhopalFactory(Factory):
    def __init__(self, material, zip,color):
        super().__init__(material, zip)
        self.color=color
        
class PuneFactory(BhopalFactory):
    def __init__(self, material, zip, color,pockets):
        super().__init__(material, zip, color)
        self.pockets=pockets

#obj=PuneFactory()        

##hierachical 
class Factory:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Pune(Factory):
    def __init__(self, name, age,address):
        super().__init__(name, age)
        self.address=address
class Mumbai(Factory):
    def __init__(self, name, age,mobile):
        super().__init__(name, age)
        self.mobole=mobile

#obj=Factory()
        
###Polymorphisam 1

    def show():
        print("how are you")
    def show():
         print("who is the best")
    show()
    
##polymorphisam Example 2 

class Animal:
    def show(self):
        print("how are you ")
class Human(Animal):
    def show(self):
        print("What about you")    
         
obj=Human()
obj.show()

#polymorphisam duck typing

class Parent:
    def show(self):
        print("i am showing")
class Child:
    def show(self):
        print("i am also showing")
        
obj1=Parent()
obj2=Child()

obj1.show()
obj2.show()

#Functional Approach in Opps 
def add(a,b):
    return a+b
print(add(12,34))
print(add(12,45))

#imperative method 
a=13
b=24
print(a+b)

##poly
def show():
    print("how are you")
def show():
    print("what about you ")
show()

#poly2
class Animal:
    def show(self):
        print("i am showing")
class Human(Animal):
    def show(self):
        print("i am also showing")
obj=Human()
obj.show()
    
#poly Duck 
class Animal1:
    def show(self):
        print("hi")
class Human1:
    def show(self):
        print("hello")
        
obj1=Animal1()
obj2=Human1()
obj1.show()
obj2.show()

####################################
