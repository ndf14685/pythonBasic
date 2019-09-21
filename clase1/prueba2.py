bool("")
bool("Soy un string")
bool(0)
bool(1)
5 and True
7 and True
"" and True
"Soy un simple string" and True
"A" and "B"

""" Truthy Falsy concepto de tratar cosas que no son bool como si lo fueran """


print(9, () and "") 


True or 7/0  #No evalua el segundo termino 

if False:
    print("Soy verdadero")
else:
    print("Soy falso")
    

while True:
    print("AAAAAA")
    #print("Tabbb")
    break
    

"""
CRLF = "Enter: Heredado de las epocas de maquina de escribir carrying "
""" 

for i in range(0,10):
    print (i);


j=("a", "b", "c", "d", "e", "f", "g", "h")
for i in range(0,8):
    print(j[i])


for i in range(0,10):
    for j in range(6,9):
        
        print("Hola ", (i,j))


print("---------------------------------------------------------------------")
for i in range(0,10):
    for j in range(6,9):
        break
        print("Hola ", (i,j))
    print("SARAZA ")


print("---------------------------------------------------------------------")
for i in range(0,10):
    for j in range(6,9):
        break
        print("Hola ", (i,j))
    print("SARAZA ")