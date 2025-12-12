#with lambada Filter 
a=[1,2,3,4,5,6,7,8,9]
result=filter(lambda x: x if x%2==True  else False,a  )
print(list(result))