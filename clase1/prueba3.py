for i in range(1,101):
    #print("Valor de 3 x",i," es ", 3*i)
    pass

print("--------------------------------------------------------")
print("------------Con While ------------------------")
print("--------------------------------------------------------")

i=1
while i<100:
    print("Balor de 3 x",i," es ", 3*i)
    i+=1 


print("--------------------------------------------------------")
print("---------Martin tiene hambre?---------------------------")
print("--------------------------------------------------------")

hambre=False
ganas=True


if not hambre and not ganas:
    print("Se va a dormir")



if hambre and not ganas:
    print("Se prepara un te")
    
if not hambre and ganas:
    print("Se come una mandarina ")
    
if hambre and ganas:
    print("Se prepara un sanguche ")
    


print("--------------------------------------------------------")


if hambre:
    if ganas:
        print("Se prepara un sanguche ")
    else:
        print("Se prepara un te")
else:
    if ganas:
        print("Se come una mandarina ")
    else:
        print("Se va a dormir")