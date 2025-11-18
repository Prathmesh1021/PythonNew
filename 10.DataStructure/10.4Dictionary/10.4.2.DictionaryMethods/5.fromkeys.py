x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

#Same example as above, but without specifying the value:
x = ('key1', 'key2', 'key3')

thisdict = dict.fromkeys(x)

print(thisdict)