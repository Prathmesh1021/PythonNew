#Constructor Example 2 
class Factory:
    def __init__(self,material,zip,pocket):
        self.material=material
        self.zip=zip
        self.pocket=pocket
        
    def show(self):
        print(f"Your Company Details Are : Material:{self.material}, Zip:{self.zip}, Pocket:{self.pocket}")
        
PuneCompany=Factory("later",45,36)
MubaiCompany=Factory("nylon",23,25)
        
PuneCompany.show()
MubaiCompany.show()