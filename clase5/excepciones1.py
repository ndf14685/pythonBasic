#a= 7/0

try:
#    a=7/0
    a=dict()
    a['Pepe']

    raise(ZeroDivisionError("Dividiste por 0"))

except KeyError: as eKeyError:
    print(eKeyError)

except ZeroDivisionError as eZeroDivisionError:
    print(eZeroDivisionError)

except Exception as eException:
    print(eException)

else:
    print("No ocurrio ninguna excepcion")

finally:
    print("Bloque no CONDICIONAL")

print("------------------------------")
print("Fin del Programa")