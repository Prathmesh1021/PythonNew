#public using  Attribute method  Example 
class A:
    a=21
    def show(self):
        print("hello i am public class in encapsulation")
class B(A):
    def show2(self):
        print(super().a)
        
obj=B()
obj.show2()
obj.show()

