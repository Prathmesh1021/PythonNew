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

#######break Example 

for i in range (1,21):
    if i==5:
     break
    print(i)

#######continue

for i in range (1,12):
    if i ==4:
        continue
    print(i)
    
##sample function
def hello():
    print("hello i am sample Function")
hello()

##using Argument Function
def add(a,b):
    print(f"Addition: {a+b}")
add(12,23)

#keyword Argument
def info(name,age):
    print(f"hello {name} and your age is {age}")
info(name="akash",age="21")

##default function 
def info2(name,age=12):
    print(f"hello {name} and your age is {age}")
info2(name="Rohit")

##Pallendrome Example 
def pallendrome(st):
    rev=""
    for i in range (len(st)-1,-1,-1):
        rev=rev+st[i]
    if rev==st:
        print(f"{st} is pallendrome")
    else:
        print(f"{st} is not pallendrome")
        
pallendrome("naman")
pallendrome("sakshi")
pallendrome("anam")
pallendrome("123456789987654321")
        
## function with rerurn 
def add(a,b):
    return f"Addition {a+b}"
print(add(12,34))

###list indexing 
l=[12,34,45,5786,5,4,35]
print(l[5])
print(l[-4])

##list Traversing Foor Loop
a=[12,23,54,76,89,887]
for i in range(len(a)):
    print(a[i])
    
##list Traversing Direct Values
c=[12,234,25,2,63,6,734,74,633]
for i in c:
    print(i)
    
##Append list 
a=[12,34,47,5,3,3]
a.append(-232)
print(a)

##INSERT LIST 
b=[12,56,57,97,365,54,97,53,25,59,97]
b.insert(4,342424)
print(b)

##extend
l=[23,56,96,3,68,2]
l.extend([10,20,30,40,50])
print(l)

##remove
h=[13,5675,95,346,2536,585,364875]
h.remove(13)
print(h)

##pop
l=[12,45,75,83,4785,58,5,5,5,8558]
pop_iteam=l.pop(7)
print(pop_iteam)
print(l)

###index
a=[2,5,9,5,85,3]
index=a.index(9)
print(index)

##count
b=[12,35,36,12,35,75,12]
c=b.count(12)
print(c)

##Sort
v=[13,6,7,895,3466,63,479,65,36]
v.sort()
print(v)

##Reverse 

r=[12,34,46,7,8,5,46,6,23,4]
r.reverse()
print(r)

##new 
n=[12,34,56,7,6,34,8]
new=n.copy()
print(new)

##clear 
k=[45,53,56,36,22,5,6,3,36,66,32,255455654,43434,54,235454,345645,346]
k.clear()
print(k)

#### Q1-->Print Positive and negative elements of an List
l=[1,42,-4,6,4,-45,453,-44,-44]

for i in l:
    if i>=0:
        print(f"positive numbers {i}")
        
for i in l:
    if i<0:
        print(f"negative numbers {i}")
        
##Q-Mean of the list 
a=[1,2,3,4,5,6,7,8,9]
sum=0
for i in a:
 sum=sum+i
print(sum/len(a))

###Q-Find The Gretest Number in list and also find index 
a=[12,23,34,236,3734,4,3626,2]
largest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
        index=i
print(f"largest value is {largest} and index is {index}")

##Q->Find Second Largest value in the list and also First value 
a=[12,23,45,5,7,7,64,3,3,35]
largest=a[0]
sec_largest=a[0]

for i in a:
    if i>largest:
        largest=sec_largest
        largest=i
    elif i>sec_largest:
        sec_largest=i
        
print(sec_largest,largest)

##Q-->Check if list is sorted or not 
a=[12,13,14,15,16]
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        continue
    else:
        print("list is not sorted")
        break
else:
    print("list is sorted ")
        

##tuple traversing with for i in range 

a=(1,234,4,5,76,5)
for i in range(len(a)):
    print(a[i])
#tuple 
t=(1,)
print(type(t))
t=(1)
print(type(t))

##tuple direct method 
t=(1,2,3,4,5,6,7)
for i in t:
    print(i)
    
##tuple method index
a=(2,4,5,6,7,8,9)
index=a.index(5)
print("index of 5 is :",index)

##count Example 
a=(12,13,14,15,151,6152,57,15)
Count=a.count(15)
print("Count of 15 is:-",Count)

##set Direct value 
s={12,34,25,47,58,3,74}
for i in s:
    print(i)
##set Methods #add
s={12,35,356,36,3}
s.add(1313)
print(s)
##remove 
r={12,35,47,374,235,36}
r.remove(374)
print(r)
##discard
d={12,132,34,36,74,85,555,43}
d.discard(132)
print(d)
##pop
s={100,23,4,5,6,7}
s.pop()
print(s)
#clear
s={12,3,5,6,447,3,}
s.clear()
print(s)
#union set
s={1,2,3}
t={3,4,5}
x=s|t
x1=s.union(t)
print(x)
print(x1)
##intersaction
s={1,2,3}
t={3,4,5}
x=s&t
x1=s.intersection(t)
print(x)
print(x1)
##diffrence 
s={1,2,3,42,42,43}
t={3,4,5,1,2,97}
x1=s-t
print(x1)
##symmetric 
s={1,2,3}
t={3,4,5}
x=s^t
print(x)
##Set with has 
a=hash("hello")
print(a)
b=hash("1131")
print(b)

##Dictionary traversing 
D5={10:100,20:200,30:300,40:400,50:500}

for i in D5:
    print(i)
for i in D5.values():
    print(i)

###Dictionary Methods 
#clear
D5={10:100,20:200,30:300,40:400,50:500}
D5.clear()
print(D5)
#copy
d={10:100,20:200,30:300,40:400,50:500}
d.copy()
print(d)
#get
D5={10:100,20:200,30:300,40:400,50:500}
x=D5.get(30)
print(x)
#iteams
d={10:100,20:200,30:300,40:400,50:500}
print(d.items())
#from key
x=10,20,30
y=0
thisdict=dict.fromkeys(x, y)
print(thisdict)
#without value
x='key1','key2','key3'
thisd=dict.fromkeys(x, y)
print(thisd)
##pop
d={10:100,20:200,30:300,40:400,50:500}
d.pop(30)
print(d)
##keys
d={10:100,20:200,30:300,40:400,50:500}
x=d.keys()
print(x)
#pop iteams
d={10:100,20:200,30:300,40:400,50:500}
x=d.popitem()
print(x)
#setdefault
d={10:100,20:200,30:300,40:400,50:500}
x=d.setdefault(60,600)
print(x)
##Update
d={10:100,20:200,30:300,40:400,50:500}
d.update({60:600})
print(d)
#values 
d={10:100,20:200,30:300,40:400,50:500}
x=d.values()
print(x)

##Ditionary CRUD
d1={10:100,20:200,30:300,40:400,50:500}

d1[10]=10000  #updating
d1[60]=232  #creating
del d1[40]  #deleting
print(d1)   #read 

###Ditionary calling Key demo 
d2={10:100,20:200,30:300,40:400,50:500}
print(d2[40])

###merge two python dict
d1={10:100,20:200,30:300}
d2={40:400,50:500}

for i in d2:
    d1[i] = d2[i]
print(d1)

#Q2-->Write a program to sum of all values in a dictionary.

d1={10:100,20:200,30:300}

sum=0
for i in d1:
    sum=sum+d1[i]
print(sum)
##Count of Each element frequency same

a=[1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,4,4]

d={}

for i in a:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1
print(d)

#Q4-->Write a python program to combine two dictionary by adding valuesfor common keys

d1={10:100,20:200,30:300}
d2={10:300,30:345,40:700}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i] 
    else:
        d1[i]=d2[i]
print(d1)
#sample for Example 
for i in range(1,90,10):
    print(i)
#Example 20 to 50
for i in range(20,51,1):
    print(i)
#Example 16 to -1
for i in range(16,-2,-1):
    print(i)
#Example -1 to -15
for i in range(-3,-16,-1):
    print(i)
#lets print table of 5
for i in range(5,51,5):
    print(i)
#to print using for loop charectors 
a="rohitkumar"
for i in range(len(a)):
    print(a[i])
#to print using lenght charector 
b="this is the tiger"
print(len(b))
for i in range(len(b)):
    print(b[i])


########################################################################################################
#Q1 Accept two numbers and print the greatest between them
a=12
b=34

if a>b:
    print(f"{a} is greter thean {b}")
else:
    print(f"{b} is greter than {a}")
    
#Question2 ==>Accept two numbers from user and print the greatest number    
a=int(input("Enter the Frist value:"))
b=int(input("Enter the second value:"))

if a>b:
      print(f"{a} is greter thean {b}")
else:
    print(f"{b} is greter than {a}")
    
#Q3 Accept The Gender From User as character and print the respective greeting meassage (EX:-Good Morning Sir/Madam)
gen=(input("enter your gender:"))

if gen=="male" or gen=="Male" or gen=="MALE":
    print("Good morning sir")
elif gen=="fmail" or gen=="Fmale" or gen =="FMALE":
    print("good morning madam")
    
#Q4 Accept an integer and check whether it is even or odd number
a=int(input("Enter your Value:"))

if a%2==0:
    print(f"{a} is EVEN Number ")
    
else:
    print(f"{a} is ODD Number")

#Q5 Accept name and age from user.Cheack if the user is a valid voter or not?EX->Hello Rahul you are a valid voter  
name=(input("Enter your name :"))
age=int(input("Enter your age: "))

if a>=18:
    print(f"hello {name} you are valid voter")
else:
    print(f"hello {name} you are not valid voter")
    

#Question 6==>Accept a year from user and check whether it is a leap year or not?
year=int(input("Enter your Year: "))
if year%4==0 or year %400==0 and year%100!=0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
#Question 7==> You cna also create if elif ladder using multiple conditions of elif For understanding solve this question take the input of temperature in celsius.
# Below 0°C → "Freezing Cold 11
#0°C to 10°C → "Very Cold
#10°C to 20°C → "Cold 11
#20°C to 30°C "Pleasant
#30°C to 40°C → "Hot
#Above 40°C → "Very Hot

temp=int(input("enter temprature :"))

if temp<0:
    print("freezing cool")
elif temp>0 and temp<10:
    print("very cold")
elif temp>10 and temp<20:
    print("cold")
elif temp>20 and temp<30:
    print("pleasent")
elif temp>30 and temp<40:
    print("hot")
elif temp>40:
    print("very hot")
else:
    print("please enter valid value ")
    
######################################################################################################
