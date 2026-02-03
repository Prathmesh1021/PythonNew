##class 
#class Simple Example 
"""
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
        print("After hello ")
        func()
        print("Before hello")
    return wrapper
@decorate
def hello():
    print("hello Rushikesh")
hello()
#Addition of 2 Example Using Decorators 
print("********************")
def decorate (func):
    def wrapper(a,b):
        print("After hello ")
        func(a,b)
        print("Before hello")
    return wrapper
@decorate
def hello(a,b):
    print(f"Addition is {a+b}")
hello(10,20)
#Args
print("*****************")
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(1,2,3,4,5,6,7,8,9)
#kwargs
print("****************")
def information(**kwargs):
    print("your information is ")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")
information(name="Rushikesh",age=12,salary="25000")
##Args Kwargs both
print("***********")
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(10,20,30,50)
print("**********")
def decorate (func):
    def wrapper(*args,**kwargs):
        print("After Addition")
        func(*args,**kwargs)
        print("Before Addition")
    return wrapper
@decorate
def addition(a,b,c,d,e):
    print(f"Total addtion is :{a+b+c+d+e}")
addition(10,20,30,40,50)
print("********************")
#################################################################################
##Lambda Add Two Values 
a=lambda x,y:x+y 
print(a(12,34))

##Lambada Even odd 
EO=lambda x: "Even" if x%2==0 else "Odd"
print(EO(12))
#################################################################################
##Map Square root of values 
"""#a=[1,2,3,4,5,6]
#result=map(lambda x:x*2,a)
#print(list(result))
"""
#Map Square Root Normal Method 
"""
#a=[1,2,3,4,5]
#def double(x):
   # return x*2
#result=map(double,a)
#print(list(result))
"""
###############################################################################
#Noramla Filter Method
""" 
#def even(x):
#    if x%2==0:
 #      return True
#  else:
 #       return False
#a=[1,2,3,4,5,6,7,8,9]
#re=filter(even,a)
#print(list(re))
"""
#Filter with lambda 
"""
#a=[1,2,3,4,5,6,7,8,9]
#result=filter(lambda x:x if x%2==True else False,a)
#print(list(result))
"""
#################################################################################
#Data Types 
#Numberic Variables 
a=12
b=12.23
c="Pranit More"
d=True
e=53j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
#Bollean Variables 
a=True
b=False
print(type(a))
print(type(b))
#String
s="hello welcome in avigna ai"
print(type(s))
#charector to unicode 
a="B"
print(ord(a))
#Ubicode to Charector 
b=76
print(chr(b))
#indexing and slicling
a="Avigna is the best company"
print(a[7])#indexing
print(a[1:9:1])#slicingy
###################################################################################
#Type Conversion 
#int to str 
i=12
i=str(i)
print(type(i))
#str to int 
a="25"
a=int(a)
print(type(a))
#for boolean 
a=12
print(bool(a))
b=12.3
print(bool(b))
c="3adsqaf%^$&424535c"
print(bool(c))
d=True
print(bool(d))
e={}
print(bool(e))
f=0
print(bool(f))
g=23j
print(bool(g))
#####################################################################################
##IO
#formated string 
name="Pritam"
age=21
print(f"hello {name} and your age is {age}")
#Non formated String
name="Ayub"
age=30
print("hello",name,"and your age is",age)
#input from user 

n=(input("Enter Your Name :"))
a=int(input("Enter your Age :"))
print(f"hello {n} and your age is {a}")
###########################################################################################
##Operators 
#Arthmatic Operator
a=int(input("Enter Your First Value:"))
b=int(input("Enter Your Second Value:"))
print(f"Addition is : {a+b}")
print(f"Substraction is : {a-b}")
print(f"Multiplication is : {a*b}")
print(f"Divide is : {a/b}")
print(f"Floor Divition is : {a//b}")
print(f"Modules is : {a%b}")
print(f"Exponenstional is : {a**b}")
#Assignment
a=10
print(a)
#Compound Operator 
a=10
print(a)
a+=10
print(a)
a-=2
print(a)
a*=3
print(a)
a/=2
print(a)
a//=2
print(a)
a%=2
print(a)
a**2
print(a)
#Comparision
a=12
b=23
print(a>b)
print(a<b)
print(a!=b)
print(a<=b)
print(a>=b)
print(233>4532)
print(232<=342)
##Logical Operator 
print(1212<32234 and 243124>352 and 3231412>3424 and 54325<535352)
print(2321<452352 and 3424235>4535636 and 23423523<436532 )
print(12>343 or 2324<5 or 2324>34325423 or 21>232134)
print(121>213 or 2334>45324552 or 132123>3324 or 73473>378323287)
print(not 2324>3425)
print(not 2324<3425)
##########################################################################################
##Conditional Statement Questions 
#Gretest Number
a=12
b=53
if a>b:
    print(f"{a} is greter than {b}")
else:
    print(f"{b} is greter than {a}")

##Gretest Number from user input
a=int(input("Enter Your frist Number:"))
b=int(input("Enter Your Second Number:"))

if a>b:
    print(f"{a} is greter than {b}")
else:
    print(f"{b} is greter than {a}")
    
##Accept gender from user and print (for Example Good Morning Sir/Madam)
gen=(input("Enter Your Gener Like (M/F) :"))
if gen=="M":
    print(f"Hello {gen}, Good Mirning Sir")

elif gen=="F":
    print(f"Heloo {gen}, Good Morning Madam")
    
else:
    print("Enter Correct Value")
##check Even Odd From User 
num=int(input("Enter Your Number for check it is Even or Odd:"))
if num%2==0:
    print(f"{num} is Even ")
else:
    print(f"{num} is Odd")
##Valid Voter or not
name=(input("Enter Your Name:"))
age=int(input("Enter Your Age :"))
if age>=18:
    print(f"Hello {name} you are valid for voter ")
else:
    print(f"Hello {name} you are not valid for voter")
##year leap or noiit 
y=int(input("Enter Your Number for check leap or not:"))

if y%4==0 and y%400==0 and y%100!=0:
    print(f"{y} is Leap Year")
else:
    print(f"{y} is not a leap year")
##Elif Ladder 
t=int(input("Enter your Temprature :"))

if t<0:
    print("Freezing Cool")
elif t>0 and t<10:
    print("Very Cool")
elif t>10 and t<20:
    print("Cool")
elif t>20 and t<30:
    print("pleasent")
elif t>30 and t<40:
    print("Hot")
elif t>40:
    print("Very Hot") 
##################################################################################
#Break & Continue
#break 
for i in range (1,23):
    if i==7:
        break
    print(i)
print("**********")
#Continue
for i in range (1,5):
    if i==3:
        continue
    print(i)
#####################################################################################
#function 
#Sample Function 
def hello():
    print("hello welcome in Avigna Ai ")
hello()
#Using Argument Addition
def add(a,b):
    print(f"Addition is :{a+b}")
add(12,42)
#KeyWord Argument
def info(name,age):
    print(f"hello {name} and your age is {age}")
info("Sudhir",13)
#Default Argument
def info2(name="Swapnil",age=12):
    print(f"hello {name} and your age is{age}")
info2()
#Palliendrome 
def pallindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev=rev+st[i]
    if rev==st:
        print(f"{st} is pallindrome")
    else:
        print(f"{st} is not a pallindrome")
pallindrome("naman")   
pallindrome("123321")
pallindrome("sakshi")
###################################################################################
##DAta Structure #List 
#List Trversing 
#List Indexing 
l=[1,2,3544,562,46,46,74,43,43,23]
print(l[5])
#List Traversing for Loop
l=[1,2,3,4,5,6,7,8,9]
for i in range(len(l)):
    print(l[i])  
#List Direct Traversing
l=[8,7,6,5,4,3,2,1]
for i in range(len(l)):
    print(i)
#List Append
l=[1,2,3,4,5,6,7,8,9]
l.append(1212)
print(l)
#List insert
l=[1,2,3,4,5,6,7,8,9]
l.insert(2,565)
print(l)
#List Extend 
l=[1,2,3,4,5,6,7,8,9]
l.extend([12,13,14])
print(l)
#Remove 
l=[1,2,3,4,5,6,7,8,9]
l.remove(2)
print(l)
#Popepd Item 
l=[1,2,3,4,5,6,7,8,9]
popeed_item=l.pop(4)
print(popeed_item)
#index
l=[1,2,3,4,5,6,7,8,9]
index=l.index(5)
print(index)
#Count
l=[1,1,1,1,2,3,4,5,6,7,8,9]
count=l.count(1)
print(f" Count of the 1 is:- {count}")
#Sort
l=[1,2,3,4,5,6,7,8,9]
l.sort()
print(l)
#reverse
l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)
#new 
l=[1,2,3,4,5,6,7,8,9]
new=l.copy()
print(new)
#clear 
l=[1,2,3,4,5,6,7,8,9]
l.clear()
print(l)

##List Assignments 
#Q-Find Positive Numbers And Negative Numbers in List
l=[1,2,3,4,5,6,7,8,9,-9,-8,-7,-6,-5,-4,-3,-2,-1]
for i in l:
    if i>=0:
        print(f"Positive Numbers Are :{i}")
    elif i<0:
        print(f"Positive Numbers are :{i}")
#Q-Mean Of the Listr
l=[1,2,3,4,5,6,7,8,9]
sum=0
for i in l:
    sum =sum+i
print(f"Mean of the List is :{sum/len(l)}")
#Q-Find Gretest number and print its index 
l=[1,2,3,4,5,6,7,8,9]
largest=l[0]
for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index=i
print(f"Your Largest Number is Largest {largest} and also index is {index}")
##Find the second gretest element in the list 
l=[12,4,35,35,22,256,456,7,253,6,45535345,3235,543,2,43]
largest=l[0]
sec_largest=l[0]
for i in l:
    if i>largest:
       sec_largest=largest
       largest=i
    elif i>sec_largest:
        sec_largest=i
print(f"largest is :{largest} and Second largest is: {sec_largest}")    
##cheak is list sorted or not 
l=[1,2,3,4,5,6,7,8,9]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print(f"List is not Sorted {l}")
        break
else:
    print(f"List is Sorted {l}")
##########################################################################################
#Tuple 
#tuple Traversing
#Index with for loop
t=(1,23,54,64,436,2,53,36)
for i in range(len(t)):
    print(t[i])
#direct Value in tuple 
t=(1,2,3,4,5,6,7,8,9)
for i in t:
    print(i)
#tuple Method
t=(1,23,54,64,436,2,53,36)
index=t.index(436)
print(index)
#count method 
t=(1,23,54,64,436,2,54,36)
count=t.count(54)
print("Count of 54:",count)
###########################################################################################
#Set Traversing 
#Direct Value
s={12,432,3,4534,6,245,34,2,52,4,262}
for i in s:
    print(i)
#Set Methods 
#add
s={12,432,3,4534,6,245,34,2,52,4,262}
s.add(1212313)
print(s)
#remove 
s={12,432,3,4534,6,245,34,2,52,4,262}
s.remove(432)
print(s)
#discard
s={12,3,432,3,4534,6,245,34,2,52,4,262}
s.discard(3)
print(s)
#pop
s={12,432,3,4534,6,245,34,2,52,4,262}
s.pop()
print(s)
##clear 
s={12,432,3,4534,6,245,34,2,52,4,262}
s.clear()
print(s)
#union Set
a={1,2,3}
b={3,4,5}
x=a|b
print(x)
#intersaction
a={1,2,3}
b={3,4,5}
x=a&b
print(x)
#Diffrence
a={1,2,3}
b={3,4,5}
x=a-b
print(x)
#symmetric 
a={1,2,3}
b={3,4,5}
x=a^b
print(x)
#Set with Hash 
a=hash("hello")
print(a)
b=hash("hello gyus")
print(b)
##############################################################################################
#Dictionary Traversing 
#Direct value 
d={1:10,2:20,3:30,4:40,5:50}
for i in d:
    print(i)
#Dictionary Methods 
d={1:10,2:20,3:30,4:40,5:50}
d.clear()
print(d)
#copy
d={1:10,2:20,3:30,4:40,5:50}
d.copy()
print(d)
#get 
d={1:10,2:20,3:30,4:40,5:50}
x=d.get(2)
print(x)
#itemas
d={1:10,2:20,3:30,4:40,5:50}
print(d.items())
##from key
a={'key1','key2','key3'}
b=0
this=dict.fromkeys(a,b)
print(this)
##pop
d={1:10,2:20,3:30,4:40,5:50}
d.pop(2)
print(d)
#keys 
d={1:10,2:20,3:30,4:40,5:50}
x=d.keys()
print(d)
#pop-iteams 
d={1:10,2:20,3:30,4:40,5:50}
d.popitem()
print(d)
#set default
d={1:10,2:20,3:30,4:40,5:50}
x=d.setdefault(1)
print(x)
#Update 
d={1:10,2:20,3:30,4:40,5:50}
d.update({5:500})
print(d)
##values 
d={1:10,2:20,3:30,4:40,5:50}
x=d.values()
print(x)

##CRUD DICTIONARY
d={1:10,2:20,3:30,4:40,5:50}
d[1]=100#update
d[6]=60#create 
del d[2]#delete
print(d)#read
#Demo Ditionary
d={1:10,2:20,3:30,4:40,5:50}
print(d[5])
##Ditionary Assignments 
#Merge Two python Ditionary 
d={1:10,2:20}
d1={3:30,4:40,5:50}
for i in d1:
    d[i]=d1[i]
print(d)
##Sum of the all values 
d1={3:30,4:40,5:50}
sum=0
for i in d1:
    sum=sum+d[i]
print(sum)
#Count the frequency of each element 
a=[1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,6,7,8,9]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
            d[i]=1
print(d)        
#Combine dictionary and adding values 

d1={10:100,20:200,30:300}
d2={10:300,30:345,40:700}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)
#######################################################################################
#Loop 
#for Loop 
#sample Example
for i in range (1,31):
    print(i)
#20 to 50
print("__________________________")
for i in range (20,51):
    print(i)
#16 to -1
print("__________________________")
for i in range (16,-2,-1):
    print(i)
#-3 to -15
print("__________________________")
for i in range(-3,-15,-1):
    print(i)
#lets print table of 5
print("__________________________")
for i in range(5,51,5):
    print(i)
#to print using for loop charector 
print("__________________________")
a="prathmesh patil"
for i in range(len(a)):
    print(a[i])
#to print using lenght 
print("__________________________")
a="prathmesh patil"
print(len(a))
for i in range (len(a)):
    print(a[i])
#Accept ip from usrer and print multiplicatiuon table 
print("__________________________")
n=int(input("Plesae Enter number for which you want Table:"))
for i in range (n,n*10+1,n):
    print(i)
###For Loop Assignments 
#Accept input and print n times hello word 
n=int(input("Enter your number for Print Hello World:"))
for i in range(1,n+1):
    print("hello world")
##Accept the input and print numbers 
n=int(input("Enter your number:"))
for i in range (1,n+1):
    print(i)
##Reverse Number Example 
n=int(input("Enter your number for reverse:"))
for i in range (n,0,-1):
    print(i)
##Take a Input From User And Print Multiplication table 
n=int(input("Plaese enter number for Muiltiplication table:"))
for i in range(1,11,1):
    print(f"{n} * {i} = {n*i}")
##Sum up to n numbers 
n=int(input("Enter your Number For sum:"))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(sum)
###Factorial Series
n=int(input("Enter your number for factorial:"))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print(fact)
#Print sum of even and odd numbers 
n=int(input("Enter your Number for Sum Even and Odd:"))
Even=0
Odd=0
for i in range(1,n+1):
    if i%2==0:
        Even =Even +i
    else:
        Odd =Odd+i
print(f"Sum of Even Number is: {Even} and Sum of Odd Number is: {Odd}")
#Print All Factorial Numbers 
n=int(input("Enter your Number for all Factorial :"))
for i in  range (1,n+1):
    if n%i==0:
        print(f"Your Factor is {i}")
###Q Accept a number and Check if it a perfect number or not.
#A number whose sum of factors is equal to the number itself
#Ex - 6=1,2,3=6
n=int(input("Enter Your Values"))
sum=0
for i in range(1,n):
    if n%i==0:
     sum=sum+i
if sum==n:
    print("This is the Perfect Number")
else:
    print("this is the Not Pefect Number")
#Q Check wether the number is prime or not 
n=int(input("cheack your number prime or not "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("your number is prime ")
else:
    print("your number is not prime ")"""
#############################################################################################
#class 
class Animal:
    a=12
    def hello(self):
        print("how are you")
print("hello welcome in class")
print(Animal().a)
Animal().hello()
#class Ex 2
class Animal:
    a="Dog"
    def sound(self):
        print("bhu bhu")
print(Animal().a)
Animal().sound()
#Class Ex3
class Car:
    wheel=4
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"Your car name is {self.name}")
obj=Car("TATA")
obj.show()        
#Class Ex4
class Animal:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"your age is {self.age}")
    @classmethod
    def class1(cls):
        print("this is the class method ")
    @staticmethod
    def static():
        print("this is the static method")
obj=Animal(12)
obj.show()
obj.class1()
obj.static()
########################################
#object Example 
class object:
    def hello(self):
        print("hello welcome in Object Example")
obj=object()
obj.hello()
########################################
#constructors Sample Example 
class Hello:
    def __init__(self,name):
        self.name=name
s=Hello("Rohit Sharma")
print(s.name)
#Constructor Example 2
class Hello:
    def __init__(self,material,zip,pocket):
        self.material=material
        self.zip=zip
        self.pocket=pocket
    def show (self):
        print(f"YOur Company Details are :{self.material}, {self.zip}, {self.pocket}")
obj=Hello("Lather",12,3)
obj.show()
###Inheritance 
#Inheritance Syntax 
class Parent:
    a=12
    def hello(self):
        print("hello welcome in Inheritance ")
class Child(Parent):
    pass
obj=Child()
obj.hello()
print(obj.a)        
#Using Super Class 
class Animal:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class Human(Animal):
    def __init__(self, material, zip,pockets):
        super().__init__(material, zip)
        self.pockets=pockets
    def show(self):
        print(f"Your Company Details are: {self.material} ,{self.zip} ,{self.pockets}")
obj=Human("Nylon",3,5)
obj.show()
#Single level inheritance 
class Single:
    a="This is Single level inheritance Attribute"
    def Hello(self):
        print("This is Single Level method")
class Level(Single):
    pass
obj=Level()
obj.Hello()
print(obj.a)
#Multiple inheritance 
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
        Human.__init__(self,"Aditya",12)
obj=Robort()
print(obj.name)
print(obj.name1)
print(obj.age) 
##Multilevel inheritance 
class Factory:
    def __init__(self,material,zip):
        self.material=material
        self.zip=zip
class Pune(Factory):
    def __init__(self, material, zip,pocket):
        super().__init__(material, zip)
        self.pocket=pocket
class Bhopal(Pune):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket)
        self.color=color
    def show(self):
        print(f"Your Comapny Details are:  {self.material} ,{self.zip} ,{self.pocket} ,{self.color}")
obj=Bhopal("Nylon",12,34,"Black")
obj.show()
#Hierarchical 
class Factory:
    def __init__(self,material, zip, pocket, color):
        self.material=material
        self.zip=zip
        self.pocket=pocket
        self.color=color
class Pune(Factory):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket, color)
    def show(self):
        print(f"Pune Factory Details are:{self.material} ,{self.zip} ,{self.pocket} ,{self.color}")
class Bhopal(Factory):
    def __init__(self, material, zip, pocket, color):
        super().__init__(material, zip, pocket, color)
    def show(self):
        print(f"Bhopal Factory Details are:{self.material} ,{self.zip} ,{self.pocket} ,{self.color}")
obj1=Pune("Lather",12,23,"Yellow")
obj2=Bhopal("Nylone",34,45,"Green")
obj1.show()
obj2.show()
########################################################################
#DSA python list and Array 
#create a list 
l=[]
m=[12,12313,23,24,2,342,4]
n=[1322,23.34,"3421","adeqwer","#$@#%@#",True]
print(l)
print(m)
print(n)
#List Method Example 
a=[12,34,67,25,675,24,67,43]
a.append(42)
a.sort()
print(a)
#Algorithm
mylist=[12,343,567,3,2146,46,2355]
myval=mylist[0]

for i in mylist:
    if i<myval:
      myval=i
print(f"Lowesat Value ",myval)
#####################################
#Stack Sample Example 
stack=[]
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

print("Stack",stack)

topelement=stack[-1]
print("Peek:",topelement)

popelement=stack.pop()
print(f"pop:",popelement)

print("After Pop Stack is ",stack)

isEmpty=not bool(stack)
print("Empty",isEmpty)

print("Size of Stack is",len(stack))
###Stack Class 
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
            return "Stack is Empty"
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len (self.stack)
mystack=Stack()
mystack.push('A')
mystack.push('B')
mystack.push('C')
mystack.push('D')
mystack.push('E')

print("Stack is :",mystack.stack)
print("Peek:",mystack.peek())
print("Pop:",mystack.pop())
print("After Pop Stack is :",mystack.stack)
print("Empty:",mystack.isEmpty())
print("Size of Stack is :",mystack.size())     
####################################################################
print("******************************")
##PolyMorphisam
# Sample Poly 
def show():
    print("hi")
def show():
    print("hello")
show()
#ploy overriding 
class Animal:
    def show(self):
        print("Hello How Are you")
class Human(Animal):
    def show(self):
       print("hello What about You")
obj=Human()
obj.show()
#Duck Typing 
class Animal:
    def show(self):
        print("i am showing ")
class Human:
    def show(self):
       print("i am also showing")
obj1=Animal()
obj=Human()
obj.show()
obj1.show()
#Functional Approach 
def add(a,b):
    print(f"Addition {a+b}")
add(12,34)
#imparative Approach
a=123
b=234
print(f"Addition is {a+b}")
##################################################
#class Public Method
class Animal:
    a="this is public attribute"
    def show(self):
        print("this is public method")
class Human(Animal):
    def show1(self):
        print(super().a)
obj=Human()
obj.show1()
obj.show()
#class Protected method 
class Animal:
    _a="this is Protected attribute"
    def _show(self):
        print("this is Protected method")
class Human(Animal):
    def show1(self):
        print(super()._a)
obj=Human()
obj.show1()
obj._show()
#private method not acceable 
class Animal:
    __a="this is Private attribute"
    def __show(self):
        print("this is Private method")
class Human(Animal):
    def show1(self):
        print(super().__a)
obj=Human()
#obj.show1()
#obj.__show()
#Private access with class 
class Factory:
    a="this is the private method with class"
    def show(self):
        print(Factory().a)
obj=Factory()
obj.show()
##Public protected private all 
class Animal:
    def __init__(self):
        self.name="Rohit Kumar"
        self._age=23
        self.__Salary=25000
    def show(self):
        print("Inside the class:--- ")
        print("Name",self.name) 
        print("Age",self._age)
        print("Salary",self.__Salary)   
obj=Animal()
obj.show()
#########################################################################
#dunder Method 
class A:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        print(f"heelo your name is {self.name}")
obj=A("surya")
print(obj.name)
#dunder ex2 add 
class Animal:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        sum=0
        for i in other:
            sum=sum+i.age
        return f"Your sum of ages are {self.age +sum}"
obj=Animal(12)
obj2=Animal(14)  
obj3=Animal(34)
print(obj +(obj2,obj3))
##################################################################################
##Ternary Operator 
a=12
print("Even") if a%2==0 else ("Odd")
#Comprehension
#list
l=[i for i in range (1,31) if i%2==0 ]
print(l)
#Dictionary 
d={i:i**2 for i in range(1,10) if i%2 ==0}
print(d)
#set
s={i*i for i in range(1,10) if i%2 ==0}
print(s)
###########################################
#Abstraction method 
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
    def area (self):
        print("i have also cretated ")
class Circle (abstract):
    def __init__(self,radious):
        self.radious=radious
    def perimeter(self):
        print("i have created")
    def area(self):
        print("i have also created")
obj=Circle(7)
obj1=Square(4)
####################################################################
#Decorators 
#Sample Example 
def decorator (func):
    def wrapper():
        print("befor")
        func()
        print("after")
    return wrapper
@decorator
def hello():
    print( "i am prathmesh")
hello()
#Sample Decorator addition Example 
def decorator (func):
    def wrapper(a,b):
        print("befor")
        func(a,b)
        print("after")
    return wrapper
@decorator
def hello(a,b):
    print(f"Addition is:{a+b}")
hello(12,43)
#Arges Example Addition 
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(sum)
add(10,20,30)
##kwargs
def info(**kwargs):
    print("Your Information is ")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")
info(name="Sudhir",age=13,address="pune")
#Args And Kwargs Boths 
def decorator (func):
    def wrapper(*args,**kwargs):
        print("hello Welcom in Args  & Kwargs")
        func(*args,**kwargs)
        print("Thank you i hope you like it")
    return wrapper
@decorator
def add(a,b,c,d,e,f,g):
    print(f"Addition is {a+b+c+d+e+f+g}")
add(10,20,30,40,50,60,70)
#############################################################
#lambda 
a=lambda x,y: x+y
print(a(1,2))
#Lambda even odd 
a=lambda x: "even" if x%2==0 else "odd"
print(a(12))

#map
#Map Using Lambda
a=[1,2,3,4,5,6,7,8]
result=map(lambda x:x*2,a)
print(list(result))
#map Using Normal method 
a=[11,12,13,14,15,16,17,18,19]
def double(x):
    return x*2
result=map(double,a)
print(list(result))

#Filter with lambda 
a=[1,2,3,4,5,6,7,8]
result=filter(lambda x:x if x%2==True else False ,a  )
print(list(result))

#Filter with normal 
def even(x):
    if x%2==0:
        return True
    else:
        return False
a=[1,2,3,4,5,6,7,8,9]
result=filter(even,a)
print(list(result))
################################################
##Data Types 
# Numbric Variables 
a=12
b=12.2
c="Akash"
d=23j
e={}
f=()
g=[]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
#Boolean 
a=True 
b=False
print(type(a))
print(type(b))
#String 
s="Sudhir is the good man, 132321 #@$@#$%$@%$@#"
print(s,type(s))
a="A"
print(ord(a))
b=89
print(chr(b))
####################################################
#type Conversion 
#int to str 
a=12
a=str(a)
print(type(a))
#Str to int 
b="243"
b=int(b)
print(type(b))
#For Boolean 
a=12
print(bool(a))
c=True
print(bool(c))
d={}
print(bool(d))
e=0
print(bool(e))
#####################################################################################
#I/O
# Formated string 
name="Reyansh"
age =12
print(f"hello {name} your age is {age} year old ")

## non Formated string
name="Reyansh"
age =12
print("hello ",name,"your age is",age)
"""
##I/O From User 
name=(input("Enter your Name :"))
std=int(input("Enter Your age "))
print(f"hello {name } and age {age}")

##Operators 
#Arthmatic Operator
a=int(input("Enter Your First Value:"))
b=int(input("Enter Your Second Value:"))"""
print(f"Addition is : {a+b}")
print(f"Substraction is : {a-b}")
print(f"Multiplication is : {a*b}")
print(f"Divide is : {a/b}")
print(f"Floor Divition is : {a//b}")
print(f"Modules is : {a%b}")
print(f"Exponenstional is : {a**b}")
#Assignment
a=10
print(a)
#Compound Operator 
a=10
print(a)
a+=10
print(a)
a-=2
print(a)
a*=3
print(a)
a/=2
print(a)
a//=2
print(a)
a%=2
print(a)
a**2
print(a)
#Comparision
a=21
b=54
c="D"
d="C"
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a!=b)
print(121<34)
print(ord(c)>=ord(d))
print(ord(c)<=ord(d))
#Logical Operators 
print(213>34 and 2242>343 and 342<5424 and 3424<435252)
print(234<34523 and 3423>432432 and 342<43524 and 23414>4321)
print(23>234131 or 232>321 or 341<3 or 2431<34)
print(34214>34 or 3432>34524 or 34224<2452234 or 3241<3424121)
print(not (23134>341234))
print(not (23134<341234))
##################################################################################
#conditional Statment 
#gretest number 
a=12
b=10
if a>b:
    print(f"{a} is geter then {b}")
else:
    print(f"{b} is geter than {a}")
# user input and print getest number 
"""
a=int(input("Enter your Firsrt Number:"))
b=int(input("Enter your Second Number:"))
if a>b:
    print(f"{a} is geter then {b}")
else:
    print(f"{b} is geter than {a}")
#accept gender from user and print ex good morning sir or madam 
gen=(input("Enter your Genter (M/F):"))
if gen=="M" or gen=="m":
    print("Good Morning Sir")
elif gen=="F" or gen=="f":
    print("Good Morning Madam")
else:
    print("Enter valid Value")
##Check value Even Or Odd Taking Input From User 
n=int(input("Enter Your Value For Checking Even or Odd:"))
if n%2==0:
    print(f"{n} is Even")
else:
    print(f"{n} is Odd")
##Valid Voter Or NOt 
name=(input("Enter Your Name:"))
age=int(input("Enter Your Age:"))
if age>=18:
    print(f"hello {name} your are valid voter")
else:
    print(f"hello {name} your are not valid voter bacause your age below 18 years")
#Cheak leap year or Not 
y=int(input("Enter Your Year to cheack leap or not :"))
if y%4==0 or y%400==0 and y%100!=0:
    print(f"{y} is Leap Year")
else:
    print(f"Not a Leap Year")
##If Else Ladder 
t=int(input("Enter Temparature :"))
if t<0:
    print("Freezing")
elif t>0 and t<10:
    print("Very Cool")
elif t>10 and t<20:
    print("cool")
elif t>20 and t<30:
    print("pleasent")
elif t>30 and t<40:
    print("Hot")
elif t>40:
    print("very Hot")
else:
    print("Enter Valid Value")"""
###################################################################################
#Break 
for i in range (1,31,2):
    if i ==9:
        break
    print(i)
# Continue
for i in range (1,21):
    if i ==7:
        continue
    print(i)
################################################
# Functions 
# Sample Function
def hello():
    print("hello how are you guys")
hello()
#Using Argument Addition 
def Add(a,b):
    print(f"Addition is {a+b}")
Add(12,34)
##Keywords Argument
def info(name,age):
    print(f"Hello {name} and Your age is {age}")
info("Prathmesh",23)
#Default Argument 
def info2(name,age=12):
    print(f"hello {name} and your age {age}")
info2("Sunita")
#Pallindrome 
def pallindrome(st):
    rev=""
    for i in range (len(st)-1,-1,-1):
        rev=rev+st[i] 
    if rev==st:
        print(f"{st} is pallindrome")
    else:
        print(f"{st} is not a pallindrome")
pallindrome("naman")
pallindrome("123321")
pallindrome("sakshi")
#Function with return 
def add (a,b):
    return a+b
print(add(12,21))        
################################################################
#list indexing
l=[12,13,14,15,16,17,18]
print(l[4])
#list Travesing for loop
l=[12,13,14,15,16,17,18]
for i in range (len(l)):
    print(l[i])  
#list Travesing for loop Direct value method 
l=[12,13,14,15,16,17,18]
for i in l:
    print(i)
#list append
l=[12,13,14,15,16,17,18]
l.append(19)
print(l)
#list insert 
l=[12,13,14,15,16,17,18]
l.insert(2,56)
print(l)
#list extend
l=[12,13,14,15,16,17,18]
l.extend([10,20,30])
print(l)
#list remove 
l=[12,13,14,15,16,17,18]
l.remove(18)
print(l)
#list Popped iteam 
l=[12,13,14,15,16,17,18]
Pop_Item=l.pop(1)
print(Pop_Item)
print(l)
#list index 
l=[12,13,14,15,16,17,18]
index=l.index(18)
print(index)
#list Count
l=[12,12,12,13,14,15,12,16,17,18]
Count_12=l.count(12)
print(Count_12)
#listS Sort
l=[12,12,12,13,14,15,12,16,17,18]
l.sort()
print(l)
#list Reverse 
l=[12,12,12,13,14,15,12,16,17,18]
l.reverse()
print(l)
#list new
l=[12,12,12,13,14,15,12,16,17,18]
new=l.copy()
print(new)
#list Copy
l=[12,12,12,13,14,15,12,16,17,18]
l.copy()
print(l)
############List Assignments 
#Find Positive And Negative Numbers 
l=[12,12,-12,-13,14,-15,12,16,-17,18]
for i in l:
    if i>=0:
        print(f"{i} is positive")
    elif i<0:
        print(f"{i} is Negative")
####mean of the list 
l=[12,12,12,13,14,15,12,16,17,18]
sum =0
for i in l:
    sum=sum+i
print(sum/len(l))
##find gretest element in the list 
a=[12,12,12,13,45,15,12,16,17,18]
largest=a[0]
for i in range (len(a)):
    if a[i]>largest:
        largest=a[i]
        index=i
print(f"largest value {largest} and index is {index}")
##Find Second largest value in the list 
b=[12,14,15,56,34,56,574,453,53,74,742,25]
largest=b[0]
sec_largest=b[0]
for i in b:
    if i>largest:
        sec_largest=largest
        largest=i
    elif i>sec_largest:
        sec_largest=i
print(sec_largest,largest)
#cheack if list is sorted or not 
s=[12,13,14,15,16,17]
for i in range (len(s)-1,):
    if s[i]<s[i+1]:
        continue
    else:
        print(f"List is Not Sorted:-{s}")
        break
else:
    print(f"List is Sorted:-{s}")
###########################################################
#Tuples
#for loop index 
t=(13,4,25,74,12245,46,4,34,4)
for i in range (len(t)):
    print(t[i])
#Direct Value 
t=(12,43,5,56,745,24,45,325)
for i in t:
    print(i)
# tuple index 
t=(10,11,12,13,14,15,16,17,18)
index=t.index(14)
print(index)
#Count 
t=(10,11,10,13,14,10,16,17,10)
count=t.count(10)
print(count)
########################################################################################
##Set 
s={12,13,14,15,16,17}
for i in s:
    print(i)
#set add 
s={12,13,14,15,16,17}
s.add(234)
print(s)
#set remove
s={12,13,14,15,16,17}
s.remove(13)
print(s)
#set Discard 
s={12,13,14,15,16,17}
s.discard(16)
print(s)
#set pop 
s={12,13,14,15,16,17}
pop=s.pop()
print(pop)
#set clear 
s={12,13,14,15,16,17}
s.clear()
print(s)
#set  union 
a={10,20,30}
b={30,40,50}
x=a|b
print(x)
#set insertion 
a={10,20,30}
b={30,40,50}
x=a&b
print(x)
#set diffrence 
a={10,20,30}
b={30,40,50}
x=a-b
print(x)
#set Symmetric 
a={10,20,30}
b={30,40,50}
x=a^b
print(x)
#set with hash 
abcd=hash("hello")
print(abcd)
####################################################################################################
#Dictionary Example 
#For Loop Traversing 
d={1:10,2:20,3:30,4:40,5:50}
for i in d:
    print(i)
## Dict Clear 
d={1:10,2:20,3:30,4:40,5:50}
d.clear()
print(d)
## Dict Copy
d={1:10,2:20,3:30,4:40,5:50}
d.copy()
print(d)
##Dict get
d={1:10,2:20,3:30,4:40,5:50}
x=d.get(1)
print(x)
## dict items
d={1:10,2:20,3:30,4:40,5:50}
a=d.items()
print(a)
#From key 
x={'key 1','key 2','key 3'}
y=0
a=dict.fromkeys(x, y)
print(a)
#pop dict 
d={1:10,2:20,3:30,4:40,5:50}
d.pop(5)
print(d)
#keys dict
d={1:10,2:20,3:30,4:40,5:50}
x=d.keys()
print(x) 
#pop items
d={1:10,2:20,3:30,4:40,5:50}
ppd=d.popitem()
print(ppd)
#set default dict 
d={1:10,2:20,3:30,4:40,5:50}
x=d.setdefault(6,60)
print(x)
##Dict update 
d={1:10,2:20,3:30,4:40,5:50}
d.update({1:100})
print(d)
##Dict values 
d={1:10,2:20,3:30,4:40,5:50}
x=d.values()
print(x)
#CRUD Ditionary 
d={1:10,2:20,3:30,4:40,5:50}
d[1]=100 #update 
d[6]=600 #create 
del d[2] #delete 
print(d) #Read 
#Demo Dictionary
d={1:10,2:20,3:30,4:40,5:50}
print(d[4])
###########
#Dictionary Assignments 
#merge Rwo Python Dict 
d={1:10,2:20,3:30,4:40,5:50}
d1={6:60,7:70,8:80,9:90}
for i in d1:
    d[i]=d1[i]
print(d)

##Sum of all Values in Dictionary
d={1:10,2:20,3:30,4:40,5:50}
sum=0
for i in d:
    sum =sum+d[i]
print(sum)

#Count Of Eatch Element in Dictionary 

#######################################################################################################
#For Loop Example 
#sample Example 
for i in range(1,31):
    print(i)
#20 to 50
for i in range (20,51):
    print(i)
#16 to -1
for i in range (16,-2,-1):
    print(i)
#-3 to -15
for i in range(-3,-16,-1):
    print(i)
#lets print table of 5
for i in range(5,51,5):
    print(i)
# to print using lenght 
a="prathmesh"
for i in range(len(a)):
    print(a[i])
# to print using for loop charector 
b="Avigna Ai is the best Company"
print(len(b))
for i in range(len(b)):
    print(i)
#Accept input from user and print Multiplication tables 
n=int(input("enter your number for Multiplication table :"))
for i in range(n,n*10+1,n):
    print(i)
##########Assignmental Questions#################################################
#Accept input print n times hello world 
n=int(input("enter your number for Hello world :"))
for i in range(1,n+1):
    print("hello World")
#Number up to n 
n=int(input("enter your number for print Numbers:"))
for i in range(1,n+1,):
    print(i)
#Accept input from user and multiplication tables 
n=int(input("Enter Number For Multiplication Table :"))
for i in range (1,11,1):
    print(f"{n} * {i} = {n*i}")
#Reverse Numbers
n=int(input("Enter Number For Reverse Number :"))
for i in range(n,0,-1):
    print(i)
##Sum Up to n  turms 
n=int(input(" Enter Your Number for Sum Of the Values: "))
sum=0
for i in range (1,n+1):
    sum=sum+i
print(sum)
##FactoriaL Numbers 
n=int(input("Enter Number For Factorial Number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"Your Factorial is :{fact}")
##Print Sum of Even & Odd Numbers 
a=int(input("Tell your Number:"))
Even=0
Odd=0
for i in range(1,n+1):
    if i%2==0:
        Even = Even+i
    else: 
        Odd = Odd+i
print(F"Your Even Sum is {Even} and Your Odd Sum is {Odd}")
##Print all factorial 
n=int(input("Enter Number For Factorial :-"))
for i in range(1,n+1):
    if n%i==0:
        print(f"This is Your Factor:{i}")
##check perfect number or not 
n=int(input("Cheack perfect Number :"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum = sum + i
if sum == n:
    print("This is perfect number ")
else:
    print("this is not a perfect number")