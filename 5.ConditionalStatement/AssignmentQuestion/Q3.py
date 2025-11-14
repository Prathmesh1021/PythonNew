#Q3 Accept The Gender From User as character and print the respective greeting meassage (EX:-Good Morning Sir/Madam)
gender=str(input("Enter your Gender :"))

if gender =="Male" or gender=="male " :
     print("Good Morning sir")
elif gender =="Female" or gender =="female ":
     print("Good Morning Madam")
else:
     print("Good morning")