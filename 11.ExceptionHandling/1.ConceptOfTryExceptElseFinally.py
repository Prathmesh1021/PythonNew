n=int(input("Tell Your number :"))

try:
    print(10/n)
except Exception as err:
    print(f"Sorry there is an err as {err}")
else:
    print("good there is no exception")
finally:
    print("i will run no matter what ")
print("ok i have done the division")