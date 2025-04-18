# Python Numbers:
x = 1    # int
y = 2.8  # float
z = 1j   # comple
print(type(x))
print(type(y))
print(type(z))

# Int
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float
# ex1:
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
# ex2:
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) #You cannot convert complex numbers into another number type.

# Random Number
import random
print(random.randrange(1, 10)) #random number between 1 and 9
