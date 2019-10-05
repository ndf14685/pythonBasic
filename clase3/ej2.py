#Crear una funcion que lea un archivo del sistema y devuelva un diccionario a partir del contenido del archivo
def recibeFuncion():
    diccionario=() 
    
        #print(i)
    with open("ejercicio2.txt", "r") as file:
        #print(i)
        #file.write(str(i)+"\n")
        for linea in file:
            linea = linea.replace(" ","")
            linea = linea.replace("\n","")
            linea = linea.split(":")
            diccionario[line[0]]=linea[1]
        #print(file.close)
            

print(recibeFuncion())