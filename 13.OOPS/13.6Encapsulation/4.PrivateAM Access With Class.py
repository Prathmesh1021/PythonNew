# Private Attributes Methonds Access with classs

class Factory:
     __a="Mumbai"#private AM
     def show(self):
         print(Factory.__a)# For In class Access Calliung
         
obj=Factory()

obj.show()