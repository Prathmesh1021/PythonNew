def pallendrome(st):
    rev=""
    for i in range (len(st)-1,-1,-1):
        rev=rev+st[i]
    if rev==st:
        print(f"{st} is pallendrome")
    else:
        print(f"{st} is not pallendrome")
        
pallendrome("naman")
pallendrome("sakshi")
pallendrome("anam")
pallendrome("123456789987654321")