# Private Attributes And Method Can't Access The attributes and method in another class 
class Factory:
    __a="pune"# __ Double Underscore Defines Private Attribute Method 
    def __show(self):
        print("Hello i am In Facrtory")
class Bhopal(Factory):
    def show2(self):
        print(super().__a)#Does Not Access Private 

obj=Bhopal()

obj.show2()
