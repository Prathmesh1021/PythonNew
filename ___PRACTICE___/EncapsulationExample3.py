#Private Encapsulation Example --not access 
class Factory:
    __a=132
    def __show(self):
        print("this is the private mrthos in Encapsulation")
class Bhopal(Factory):
    def show2(self):
        print(super().__a)#dose not acces private 
obj=Bhopal()
obj.__show()#not access private method SS
obj.show2()
