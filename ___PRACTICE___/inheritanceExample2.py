#Inheritanmce using Super Class 
class Mumbai:#parentclass /super class
    a="i am attribute mention inside factory"
    
    def hello(self):
        print("i am method mention inside factory") 
class Pune(Mumbai):#child class/sub class 
    pass
print(Pune().a)
obj=Pune()
obj.hello()


    
        