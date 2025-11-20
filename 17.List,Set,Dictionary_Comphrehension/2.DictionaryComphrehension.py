#Dictionary Comphrehension for create power of given elements in the dictionary with condition
D={i:i**2 for i  in range(1,10)if i%2==0}
print(D)