#multiple inheritance Example 5
class Animal1:
    def __init__(self,name):
        self.name=name
        
class Human1:
    def __init__(self,name1,age):
        self.name1=name1
        self.age=age
    
class Robort(Human1,Animal1):
    name2="AgenticAi"
    
    def __init__(self):
        Animal1.__init__(self, "Tiger")
        Human1.__init__(self, "Rohit",12)
obj=Robort()
print(obj.name)
print(obj.name1)
print(obj.age)
print(obj.name2)















































