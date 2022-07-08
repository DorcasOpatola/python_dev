#!/usr/bin/python3
"""
Python Numbers

There are three numeric types in Python:
    int: whole numbers, '+ve' or '—ve'
    float: numbers with decimals, '+ve' or '—ve'.
           can also be scientific numbers with an "e" to
           indicate the power of 10.
    complex: int or float written with a "j".
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

"""convert from int to float:"""
a = float(x)

"""convert from float to int:"""
b = int(y)

"""convert from int to complex:"""
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# It is not possible to convert a complex number to another type.
