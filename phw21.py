def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    return a/b

print("Lets do some math with just funcions!")

age = add(30,5)
height = sub(78,4)
weight = multiply(90,2)
iq = div(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight} and IQ: {iq}")

what = add(age, sub(height, multiply(weight, div(iq,2))))
print(what)