print "Evaluar 2 numeros y definir cual es mayor o si son iguales"

def ej1(a,b):
    if a>b: 
        return "A es mayor que B",
    elif b>a: 
        return "B es mayor que A",
    else: 
        return "Son iguales"

    
print(ej1(2,3))


print(ej1(5,4))

print ej1(5,5)

print ej1(5,4)


print "Evaluar un valor si es un numero"
def ej2(a,b):
    if type(a) is int or type(a) is float or type(a) is complex:
        return "Es un numero"
    else:
        return "No es un numero" 


print ej2(2,3)

print "Crear funcion que reciba un parametro y que no haga nada"

def ej3(a):
    pass

print ej3(234234234)