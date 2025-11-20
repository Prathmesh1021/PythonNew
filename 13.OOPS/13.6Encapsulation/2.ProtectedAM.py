#Protected  Attributes and Method Wols Same Like Public And It Defines _ Underscore 
class Factory:
    _a="pune"#Protected to use underscore _ for a 
    def _show(self):# #Protected to use underscore _ for show
        print("Hello I am In factory")
        
class Bhopal(Factory):
    def show2(Self):
        print(super()._a)
        
obj=Bhopal()

obj.show2()#Obj Calling 
obj._show()