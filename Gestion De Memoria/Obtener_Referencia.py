import sys

a = 'Cadena de Texto'
print(sys.getrefcount(a))   #Es el 4

b = a 
print(sys.getrefcount(b))

del a
print(sys.getrefcount(a))   #Error