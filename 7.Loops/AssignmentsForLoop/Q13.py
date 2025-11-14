#QCount All Letters ,digits,and special Symbols from a given string 
#Given:"Str1=P@#yn26at^&i5ve"
#Expected Outcome:
#Total counts of chars.digits,and symbols
#Chars=8
#Digits=3
#Symbol=4
a="Str1=P@#yn26at^&i5ve"
char= 0
dig= 0
spchr= 0
for i in a:
    if i.isdigit(): 
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchr+=1
print(f"your digit are :{dig}\n your alphabets are :{char}\n your special characters are :{spchr}") 
        
    