def switching(a, b):
    temp = a
    a = b
    b = temp
    return a, b

a = input("what's a? ")
b = input("what's b? ")

# a, b = switching(a, b)
a, b = b, a
print(f'a is {a}')
print(f'b is {b}')