#there are all methods attributes.
class Animal:
    name="Tiger"
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"Your age is {self.age}")
   
    @classmethod
    def class1(self):
        print("This uis the class Methods")
    @staticmethod
    def static1(self):
        print("this is the static methods")
        
obj=Animal(54)
obj.show()


