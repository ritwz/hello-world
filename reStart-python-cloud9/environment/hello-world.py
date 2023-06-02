print("Hello World")

def fib(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
        
print(fib(6))

print("Python has three numeric types: int, float, and complex")

myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myString="This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))