#There Are All MethodsAttributes 
class animal:
    name="tiger"#Class Methods 
    def __init__(self,age):
        self.age=age#instance attributes 
    def show (self):
        print(f"your age is {self.age} ") #Instance Methods
    
    @classmethod #Class Methods 
    def hello(cls):
        print("how are you bro")
        
    @staticmethod# static Method
    def static():
        print("how are you ")
        
obj=("lion")
obj.static()

n=animal(12)
n.show()
