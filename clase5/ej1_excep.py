while True:
    a = input("> ")

    if a == "SALIR":
        break
        try:
            int(float(a))
        except Exception as e:
            print("Ha ingresado un NO numerico")
        else:
            print("Ha ingresado un valor Numerico")