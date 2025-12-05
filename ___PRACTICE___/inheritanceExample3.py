class parent:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"your name is {self.name}")
                       
class child(parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age=age
    def show(self):
        print(f"hello {self.name}and your ages is {self.age}")
        
obj=child("akash",12)
obj.show()

        