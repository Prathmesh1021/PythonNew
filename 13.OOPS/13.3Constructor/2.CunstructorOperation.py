#Constructor Operation With Class 
class factory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
    def show(self):
        print(f"your object details are {self.material},{self.pockets},{self.zips}")
        
reebok =factory("lather",3,2)
campus =factory("nylon",3,3)     

reebok.show()   
campus.show()