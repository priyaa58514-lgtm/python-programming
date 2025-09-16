a=int(input("Enter the value:"))
b=input("Enter another value:")
try:
    c=a+b
    print("result",c)
except TypeError:
    print("Type error has occured.Enter the correct type")
