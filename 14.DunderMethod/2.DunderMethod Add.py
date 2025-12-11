#In dunder method Addition of ages using objects 
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        print("how are your and your name is {self.name}")
    def __add__(self,other):
        sum=0
        for i in other:
            sum=sum+i.age
        return f"Your sum of ages are {self.age +sum}"
obj=Animal("lion",12)
obj2=Animal("dolphin",14)  
obj3=Animal("tiger",34)

print(obj +(obj2,obj3))