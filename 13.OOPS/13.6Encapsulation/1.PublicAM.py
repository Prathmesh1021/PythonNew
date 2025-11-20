#Public Attribites And Methods 
class Factory:
    a="pune"
    def show(self):
        print("Hello i am a pune factory")
        
class Bhopal(Factory):
    def show2(self):
        print(super().a)
        
obj=Bhopal()

obj.show2()
obj.show()
    