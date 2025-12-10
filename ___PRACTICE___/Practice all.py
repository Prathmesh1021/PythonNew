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
        
        