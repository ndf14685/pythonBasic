file = open("fileCreado.txt", "r")

print (file.read())


print(file.readlines())



file2=open("file2.txt", "r")
print(file2.readlines())



with open("archivo.txt","r") as file:
for linea in file:
    print(linea)