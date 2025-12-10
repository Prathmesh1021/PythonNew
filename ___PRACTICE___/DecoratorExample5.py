#using Boths Args And kwargs 
def decorate(func):
    def wrapper(*args,**wrargs):
        print("Your Addition is :")
        func(*args,**wrargs)
        print("thank you i hope you like it ")
    return wrapper    
@decorate
def addition(a,b,c,d,e,f):
    print(f"Total is{a+b+c+d+e+f}")
addition(10,20,30,40,50,60)