def productoria(*args):
    print(args, type(args))
    total=1    
    for arg in args:
        total*=arg
    print total

productoria(1, 2, 3,4,9,8)
   


def enteros(*args):
    print(args, type(args))
    contador=0    
    for ent in args:
        if type(ent) is int:
            contador +=1

    return contador

print(enteros())
print(enteros("a"))

print(enteros(1, 2, 3))
print(enteros(1, "A"))
print(enteros(1,2,3,4,"A",9))



def sumaDiccio(**diccio):
    total=0
    for elem in diccio:
        total += diccio[elem]

    return len(diccio), total


print(sumaDiccio())
#print(sumaDiccio("a"))

print(sumaDiccio(1, 2, 3))
print(sumaDiccio(1, "A"))
print(sumaDiccio(1,2,3,4,"A",9))




def unpack1(a, b, c, d):
    print a, b, c, d

lista=(1,2,3,4)

unpack1(*lista)
