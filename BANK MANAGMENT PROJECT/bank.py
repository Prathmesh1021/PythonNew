import json
import random
import string
from pathlib import Path

class Bank:
    database ='data.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read)
        else:
            print("no such file exist")  
    except Exception as err:
        print(f"an exception occured as{err}")
        
    @classmethod  
    def __update(cls):
        with open(cls.database,'w')as fs:
            fs.write(json.dumps(Bank.data))
            
    @classmethod
    def __accountgenerate(cls):
        alpha =random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchr=random.choices("@#$%^&*",k=1)
        id=alpha+num+spchr
        
    def Createaccount(self):
        info={
            "name":(input("Tell your Name :")),
            "age":int(input("tell your age :")),
            "email":str(input("tell Your Email :")),
            "pin":int(input("tell your 4 number pin")),
            "account no.":1234,
            "balance":0
        }
        
        if info['age']<18 or len(str(info['pin']))!=4:
            print("Sorry you cannot create account")
        else:
            print("Account has been created Successfully")
            for i in info:
                print(f"{i}:{info[i]}")    
            print("please note down your account number:")
            Bank.data.append(info)
            Bank.__update()
user=Bank()
print("press 1 for creating an account")
print("press 2 for Depositing the money in the bank ")
print("press 3 for withdrawing the money ")
print("press 4 for details")
print("print 5 for updating the details")
print("press 6 for deleting your account")

check=int(input("tell your response :-"))
if check ==1:
    user.Createaccount()