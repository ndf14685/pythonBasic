def esPrimo(numA):

    if(numA<2):
        #No es primo
        print(numA, "No es Primo")
        return False
    for i in range (2,numA):
        if(numA%i==0):
            print(numA, "No es Primo")
            return False
    print(numA, " Es primo")
    return True

esPrimo(2)

def promedio(*listaPromedio):

    tot=0
    for ent in listaPromedio:
        if type(ent) is int:
            tot+=ent
            
    
    if len(listaPromedio)==0:
        return 0

    prom=tot/len(listaPromedio)
    print("El promedio es: ", prom)
    return prom

promedio(1,200,3,4,5,6)




def ej3(*lista):
    primos=0
    media=promedio(*lista)
    sumatoria=0


    for elem in lista:
        if esPrimo(elem):
            primos+=1
        sumatoria+=elem

    return primos,media,sumatoria


print(ej3(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))