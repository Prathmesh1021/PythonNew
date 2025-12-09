#In dunder method Addition of ages using objects 
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