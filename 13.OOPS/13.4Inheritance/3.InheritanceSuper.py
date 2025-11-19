#using Super()
class Animal: #parent class 
    def __init__(self,name):
        self.name=name
    def show(self):
         print(f"your name is   {self.name}")
         
class human(Animal):#child class 
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        
    def show(self):
        print(f"Hello your name is  {self.name},{self.age}")

person1=human("prathm",23)

person1.show()