def suma(p, s):
    print(p+s)


suma(p=2,s=5)
suma(s=5,p=2)


def division(p, s):
    print(p/s)


division(p=10,s=5)
division(s=5,p=10)

def suma1(p, s=8):
    print(p+s)

suma1(1)



def suma2(*ops):
    print(ops, type(ops))
    total=0
    for op in ops:
        total+=op
    print total

suma2()

suma2(1,2,3,4)


def guia(**registros):
    print(registros,type(registros))

guia()

guia(juan=1234, pepe=6789, Roberto=123)
        
        
def super_funcion(a,b,c,d="",e=5,*f,**g):
    print(a,b,c,d,e,f,g)

#super_funcion()

super_funcion(9,132,"A","B", None, 1, 7, 9, 8, Roberto="ASD")


super_funcion(9,132,"A","B", None, Roberto="ASD", pepe="pqpw")


def funcion(a,b,c):
    return a,b,c

print(funcion(1,2,3))

