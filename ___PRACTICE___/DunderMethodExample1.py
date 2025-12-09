#__INIT__&__Str___Using dunder method 
class D:
    def __init__(self,name):#init dunder method
        self.name=name
    def __str__(self):#str dunder method
        return f"hello how are you and your name is {self.name}"
obj=D("lion")
print(obj)
