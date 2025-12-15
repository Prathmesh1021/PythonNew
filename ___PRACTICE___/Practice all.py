##class 
class Factory:
    a="this is the attributes"
    def hello(self):
        print("how are you ")
print("welcome in class ")
print(Factory().a)
Factory().hello()
##
class Animal:
    a="dog"
    def sound(self):
        print("bhubhu")
print(Animal().a)
Animal().sound()
##
class Car:
    weel=4
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"your car name is {self.name}")
obj=Car("Creta")
obj.show()
class factory:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"Your age is :{self.age}")
    @classmethod
    def class1(cls):
        print("this is the class method")
    @staticmethod
    def static():
        print("this is the static method")
        
obj=factory(12)
obj.class1()
obj.static()

class Cons:
    def __init__(self,name):
        self.name=name
s=Cons("riya")
print(s.name)

class Cons2:
    def __init__(self,material,zip,pockets):
        self.material=material
        self.zip=z=zip
        self.pockets=pockets
    def show(self):
        print(f"Your comany details are :{self.material} ,{self.zip} ,{self.pockets}")
obj=Cons2("lather",3,3)
obj.show()

##
class obj:
    a=12
    def hello(delf):
        print("this is the object example")
print(obj().a)
obj().hello()
##
x=[]
y=[12,224,3453,53,36,663]
z=[23,"Akash",7346.34,"@%@%@",324j,True]
print(x)
print(y)
print(z)
##
r=[12,4254,6,743,64742,4,37,2,7,7,5,546]
r.append(342)
r.sort()
print(r)
##
mylist=[12,324,25,5,2,25,25,52]
myval=mylist[0]

for i in mylist:
    if i<myval:
        myval=i
        print("lowest value is :",myval)
## stack 

stack=[]

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

print("stack:",stack)

topelement=stack[-1]
print("Peek",topelement)

popelement=stack.pop()
print("pop",popelement)

print("after pop stack is ",stack)

isEmpty=not bool(stack)
print("Empty",isEmpty)

print("size",len(stack))

###
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
    
ms=Stack()

ms.push('A')        
ms.push('B')        
ms.push('C')        
ms.push('D')        
ms.push('E')        

print("Stack:",ms.stack)
print("Peek",ms.peek())
print("pop",ms.pop())
print("after pop stack is ")
print("Empty",ms.isEmpty())
print("size",ms.size())

##inheritamce syantax 
class parent:
    def hello(self):
        print("hello how are you")
class child(parent):
    pass
obj=child()
obj.hello()

##
class Animal:
    a="this is attribute"
    def hello(self):
        print("this is method")
class Human(Animal):
    pass
obj=Human()
print(obj.a)
obj.hello()

#inheritance using super class 
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class PuneFactory(Factory):
    def __init__(self, material, zip,pockets):
        super().__init__(material, zip)
        self.pockets=pockets
    def show(self):
        print(f"Details are :{self.material}, {self.zip}, {self.pockets}")

obj=PuneFactory("later",23,43)
obj.show()
## single level
class Animal:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your animal name is {self.name}")
class Human(Animal):
    pass
obj=Human("tiger")
obj.show()

##Multiple 
class Animal:
    def __init__(self,name):
        self.name=name
class Human:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
class Robort(Human,Animal):
    def __init__(self):
        Animal.__init__(self,"Lion")
        Human.__init__(self,"Rahul",13)
obj=Robort() 
print(obj.name)
print(obj.name1)
print(obj.age)


########multilevel inheritance 
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
        super().__init__(material, zip, pockets,)
        self.color=color
    def show(self):
        print(f"details are :- {self.material} ,{self.zip} ,{self.pockets} ,{self.color}")
obj=Pune("lather",34,23,"black")
obj.show()

### hierachical 
class Factory:
    def __init__(self,material,zip,pocket,color):
        self.material=material
        self.zip=zip
        self.pocket=pocket
        self.color=color
class pune(Factory):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket, color)
    def show(self):
        print(f"Pune Company Details are:{self.material} ,{self.zip} ,{self.pocket} ,{self.color}")
class bhopal(Factory):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket, color)    
    def show2(self):
                print(f"Bhopal Company Details are:{self.material} ,{self.zip} ,{self.pocket} ,{self.color}")
obj1=pune("lather",23,24,"black")
obj1.show()
obj2=bhopal("Nylon",2,4,"Red")
obj2.show2()

##poly sample example 
def show():
    print("hi")
def show():
    print("hello")
show()
## poly Method ovverriding 
class Animal:
    def show1(self):
        print("hello how are you")
class Human(Animal):
    def show1(self):
        print("hello what about you ")#method overriding
obj=Human()
obj.show1()

##poly 3 Example 
class A:
    def show(self):
        print("i am showing")
class B:
    def show(self):
        print("i am also Showing")
        
obj1=A()
obj1.show()

obj2=B()
obj2.show()

## functional Approach 
def add(a,b):
    return a+b
print(add(346,34))
print(add(341,45))
##imperative Approach
a=23
b=23
print(a+b)
##Encapsulation 
## public Accsess Method 
class parent:
    a="this is class Attribute"
    def show(self):
        print("this is class method ")
class child(parent):
    def show2(self):
        print(super().a)
obj=child()
obj.show()
obj.show2()

##protected
class Animal:
    _a="this is protected attribute"
    def _show(self):
        print("this is protected method")
class Human(Animal):
    def show2(self):
        print(super()._a)
obj=Human()
obj._show()
obj.show2()

##classs private not accesseble 
class Factory:
    __a="this is private class attribute not accesible "
    def __show(self):
        print("this is private method can not me acceas it ")
class Pune(factory):
    def show(self):
        print(super().__a)#Can't access because this on is private Encapsulation 
#obj=Pune()
#obj.__show()
#obj=show()

## private acees with class 
class animal:
    __b="this one private Attribute"
    def show4(self):
        print(animal().__b)
obj=animal()
obj.show4()

###public private protected 
class Factory:
    def __init__(self):
        self.name="public member "#public
        self._age=21#Protected
        self.__Salary=50000#private
    def show (self):
        print("Inside the class")
        print("name",self.name)
        print("age",self._age)
        print("Salary",self.__Salary)
        
##dander method

class Factory:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"hello how are you and your name is {self.name}"
obj=Factory("Rahul")
print(obj)

##dandar method 
class Animal:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        sum=0
        for i in other:
            sum=sum+i.age
            return "sum of ages is:", {self.age +sum}
            
obj=Animal(12)
obj1=Animal(13)
obj2=Animal(14)
print(obj +(obj1,obj2))


## teernary operator
a=64
print("even") if a%2==0 else print("odd")

##Comperehention 
#list Comperehension 
l=[i for i in range(1,21) if i%2==0]
print(l)
#Dictionary Comperehention
D={i:i**2 for i in range (1,11)if i%2==0}
print(D)
#set Comperehension 
S={i*i for i in range(1,10) if i%2==0}
print(S)
        
##Abstraction Method Example 
from abc import ABC, abstractmethod
class abstract (ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass
class Square(abstract):
    def __init__(self,side):
        self=side=side
    def perimeter(self):
        print("i have created")
    def area(self):
        print("i have created this ")
class Circle (abstract):
    def __init__(self,radious):
        self.radious=radious
    def perimeter(self):
       print("i have created ")
    def area (self):
       print("i have created this ") 
#obj=Circle(7)
#obj=Square(4)  
        
###Decorator Example 1 --Using Decorator and Wrapper Class 

def decorate(func):
    def Wrapper():
        print("before")
        func()
        print("after")
    return Wrapper
@decorate
def hello():
    print("hello i am prathmesh patil")
hello()

###Decorator Example 2__ Addition of two numbers 
def decorate(func):
    def Wrapper(a,b):
        print("before addition")
        func(a,b)
        print("after addition")
    return Wrapper
@decorate
def add(a,b):
    print(f"your addithion is: {a+b}")
add(12,56)

###Decorator Example 3 --- usinf args addition
def addition(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
addition(12,20,40,70)   

##decorator Example ---Using Kwargs information details 
def information(**kwargs):
    print("your information is :")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")
    
information (name="prathmesh",age=23,designation ="Developer",mobile=1213131313)


##Decorators Example 5 Args And Kwargs Both 
def decorate(func):
    def Wrapper(*args,**kwargs):
        print("before adddition")
        func(*args,**kwargs)
        print("After addition ")
    return Wrapper
@decorate
def add(a,b,c,d,e,f):
    print(f"Total is {a+b+c+d+e+f}")
add(10,20,30,40,50,60)

##Lambda addition operation
Add=lambda a,b:a+b
print(Add(12,33)) 
##Lambada Example 2 Even Odd
evenodd=lambda c:"even" if c%2==0 else "odd"
print(evenodd(13)) 
##map 
a=[1,2,3,4,5,6]
result=map(lambda x:x*2,a)
print(list(result))
##map2
b=[1,2,3,4,5,6]
def double(x):
    return x*2
result=map(double,b)
print(list(result))
#filter
def even(x):
    if x%2==0:
        return True
    else:
        return False
a=[1,2,3,4,5,6,7,8,9]
result=filter(even,a)
print(list(result))
#filter 2
a=[1,2,3,4,5,6,7,8,9]
result=filter(lambda c:c if c%2==True else False,a)
print(list(result))

##Addition Using Lambada 
addition=lambda a,b:a+b
print(addition(12,32))
##use ternary operation in lambada add check even odd 
evenodd=lambda x: "even" if x%2==0 else "odd"
print(evenodd(32))
##map using squre of lists 
a=[1,2,3,4,5,6,7]
result=map(lambda x:x*2,a)
print(list(result))
##map2 traditional method 
a=[7,6,5,4,3,2,1]
def double(x):
    return x*2
result=map(double,a)
print(list(result))
##filter method using ======>even odd operations 
def even(x):
    if x%2==0:
        return True
    else:
        return False
a=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
result=filter(even,a)
print(list(result))

##filter 2
a=[34,34,2,24,35,465,85,6]
result=filter(lambda x:x if x%2==True else False,a)
print(list(result))

#####################################################################
class A:
    a=12
    def hello(self):
        print("how are you")
print("Welcome in class")
print(A().a)
A().hello()

class B:
    a="dog"
    def sound(self):
        print("bhubhu")
print(B().a)
B().sound()

class Car:
    wheel=4
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"your car name is {self.name}")
obj=Car("TATA")
obj.show()

class Animal:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"Your age is {self.age}")
    @classmethod
    def class1(cls):
        print("This is the class method")
    @staticmethod
    def static():
        print("this is the static method")
        
obj=Animal(12)
obj.show()
obj.class1()
obj.static()

###
class Cons:
    def __init__(self,name):
        self.name=name
s=Cons("Reyansh patil")
print(s.name)
##constructor 2
class Cons2:
    def __init__(self,material,zip,pocket):
        self.material=material
        self.zip=zip
        self.pocket=pocket
    def show(self):
        print(f"your company details are {self.material},{self.zip},{self.pocket}")
obj=Cons2("lather",33,32)
obj1=Cons2("Nylon",2,4)

obj.show()
obj1.show()

## Simple Object 
class object:
    def hello(self):
        print("hello")
print(object().hello())
####
x=[]
y=[12,3,4,5,6,6,7,]
z=[232,24.34,"fuiwgfiu","##%@#%@^#&$&",34j,True]
print(x)
print(y)
print(z)

#####
a=[324,364,44,7,4,3,9,3,9,4]
a.append(35)
a.sort()
print(a)

##create algoritham 
list=[13,5467,7,36,4,563,63]
v=list[0]

for i in list:
    if i <v:
        v=i
print("lowest value :",v)

###########
stack=[]

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
stack.append('E')

print("stack:",stack)

topelement=stack[-1]
print("peek:",topelement)

popelement=stack.pop()
print("pop:",popelement)

print("After pop Stack are",stack)

isEmpty=not bool(stack)
print("empty",isEmpty)

print("size:",len(stack))

##stack using class

class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
        
    def peek(self):
        if self.isEmpty():
            return "the stack is Empty"
        return self.stack[-1]
    def pop(self):
        if self.isEmpty():
            return "the stack is Empty"
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

print("Stack:",mystack.stack)
print("Peek:",mystack.peek())
print("pop:",mystack.pop())
print("After Pop Stack are",mystack.stack)
print("Empty:",mystack.isEmpty())
print("size:",mystack.size())

#####class 
class Parent:
    a=12
    def hello(self):
        print("hello guys")
class child(Parent):
    pass
print(child().a)
child().hello()

####
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class Pune(Factory):
    def __init__(self, material, zip,pocket):
        super().__init__(material, zip)
        self.pocket=pocket
    def show(self):
        print(f"Your company details is :{self.material},{self.zip},{self.pocket}")

obj=Pune("lather",21,2)
obj.show()

class Single:
    a=34
    def hello(self):
        print("this is the single level inheritance ")
class Single1(Single):
    pass
print(Single1().a) 
Single1().hello()      

#########
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
        Human.__init__(self,"Akash",24)
obj=Robort()
print(obj.name) 
print(obj.name1)
print(obj.age)   
        
####multilevel
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class Pune(Factory):
    def __init__(self, material, zip,color):
        super().__init__(material, zip)
        self.color=color
class Bhopal(Pune):
    def __init__(self, material, zip, color,pocket):
        super().__init__(material, zip, color)
        self.pocket=pocket
    def show(self):
        print(f"Your comppany details are {self.material},{self.zip},{self.color},{self.pocket}")

obj=Bhopal("Lather",3,"black",44)
obj.show()

###########
class Factory:
    def __init__(self,material,zip,pocket):
        self.material=material
        self.zip=zip
        self.pocket=pocket
        
class Pune(Factory):
    def __init__(self, material, zip, pocket):
        super().__init__(material, zip, pocket)
    def show(self):
        print(f"Pune company details is:{self.material},{self.zip},{self.pocket}")   
class Bhopal(Factory):
    def __init__(self, material, zip, pocket):
        super().__init__(material, zip, pocket)
    def show(self):
        print(f"Bhopal company details is:{self.material},{self.zip},{self.pocket}")   

obj1=Pune("nylon",2,4)
obj2=Bhopal("lather",4,5)
obj1.show()
obj2.show()
####poly sample example
def show():
    print("hello")
def show():
    print("hi")
show()
###poly Example 2
##method overriding
class Animal:
    def show(self):
        print("hello how are you")
class Human(Animal):
    def show(self):
        print("hello what about you")
obj=Human()
obj.show()

###duck typing
class Animal:
    def show(self):
        print("i am showing")
class Human:
    def show(self):
        print(" i am also showing")
    
o=Animal()
o=Human()
o.show()
o.show()
###functional approach
def addition(a,b):
    return a+b
print(addition(12,34))    
        
### imperative approach
a=23
b=53
print(a+b)

##Encapsulation
#public
class A:
    a="hello this is the public class"
    def show(self):
        print("hello this is public method")
class B(A):
    def show2(self):
        print(super().a)     
ob=B()
ob.show2()
ob.show()

#####Protercted 
class A:
    _a="hello this is the protected class"#_undersorce is protected
    def _show(self):
        print("hello this is protected method")
class B(A):
    def show2(self):
        print(super()._a)     
ob=B()
ob.show2()
ob._show()
##private
class A:
    __a="hello this is the private class"#_undersorce is protected
    def __show(self):
        print("hello this is private method")
class B(A):
    def show2(self):
        print(super()._a)     
#ob=B()
#ob.show2()
#ob.__show()
##
class A:
    __a="hello this is the private class"#_undersorce is protected
    def show(self):
        print(A().__a)
obj=A()
obj.show()
#############
class All:
    def __init__(self):
      self.name="Prathmesh Patil"
      self._age=35
      self.__Salary=24242
    def show(self):
        print("Inside Class")
        print("Name:",self.name)
        print("Age:",self._age)
        print("Salary",self.__Salary)
        
obj=All()
obj.show()
#####Dunder method 1
class A:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"hello how are you and your name is {self.name} "
obj=A("Agnivesh")
print(obj)

##dunder add
class B:
    def __init__(self, age):
        self.age = age

    def __add__(self, others):
        total = 0
        for obj in others:
            total += obj.age
        return f"Sum of ages {self.age + total}"
obj3 = B(12)
obj1 = B(24)
obj2 = B(32)

print(obj3 + (obj1, obj2))

######### Tearnary even odd 
a=15
print("Even")if a%2==0 else print("odd")

l=[i for i  in range (1,21) if i%2==0 ]
print(l)

D={i:i**2 for i in range(1,21) if i%2==0}
print(D)

S={ i*i for i in range (1,10)if i%2==0}
print(S)

#############Abstraction metho
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
    def perimeter(self):
        print("i have created")
    def area(self):
        print("i have created this")
class Circle (abstract):
    def __init__(self,radious):
        self.radious=radious
    def perimeter(self):
        print("i have created")
    def area(self):
        print("i have created this")
#obj=Circle(7)
#obj1=Square(2)

