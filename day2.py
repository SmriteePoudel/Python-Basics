# data types

# int
a = 10
print(a)
print(type(a))

# string
a = "Hello, World!"
print(a)
print(type(a))
a = "Hello, World!"
print(a)

# float
a = 3.14
print(a)
print(type(a))

# boolean
is_raining = True
print(is_raining)
print(type(is_raining))

is_sunny = False
print(is_sunny)
print(type(is_sunny))
# complex
a = 2 + 3j
print(a)
print(type(a))
# NoneType
a = None
print(a)
print(type(a))

# diffence between these two
a = None  # storage is allocated but it doesnt contain any value
a = ""  # empty string doesnt contain any character and storage is not allocated

a = 30
b = 4
print(a // b)  # gives lowest whole number
print(a % b)  # gives remainder
print(a**b)  # gives power


a = "Hello"
b = "World"
print(a + " " + b)


a = "hari"
b = "om"
print(a + " " + b)

# multiple

name = "Hari"
value = 5
print(name * value)

print("..." * 10)

# wrong type causes TypeError
# print(name + value)  # cannot concatenate string and int

print("..." * 10)

# type conversion
# int to string
a = "10"
b = int(a)
print(type(b))

# string to string
a = "10"
print(str(a))

x = int("10")
print(type(x))

y = float("3.14")
print(type(y))

z = str(100)
print(type(z))
# isinstance checks if the variable is of a certain type
b = "10"
print(str(b))
print(isinstance("10", int))
