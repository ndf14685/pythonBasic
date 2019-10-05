def recibeFuncion(a): 
    for i in a:
        #print(i)
        with open("coleccionEj1.txt", "a") as file:
            print(i)
            file.write(str(i)+"\n")
            
            print(file.close)
            pass
    print(file)




a=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes','Sábado', 'Domingo']

recibeFuncion(a)