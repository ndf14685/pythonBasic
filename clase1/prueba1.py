a = 5
b = 3.14
c = "Soy un string"
d = False
e = 6+3j


print(a +b, type(a+a))


print (a +a, type(a+a))
print(b*b, type(b*b))
print(a**a, type(a**a))
print(a**b, type(a**b))

print(c+c, type(c+c))
print(a/5, type(a/5))

print(c*a)

enumerate([1,2,3])



a = 0

for i in range(0,10):
    a = a + 0.1

print(a, type(a))




a = 0.0000000000000000000000000000000001

for i in range(0,10):
    a = a + 0.1

print(a, type(a))