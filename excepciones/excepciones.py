#creando una funcion que sume dos numeros
def sumar_numeros():
    #creando un bucle infinito para que el usuario ingrese los numeros
    while True:
        a = input("Ingrese un número: ")
        b = input("Ingrese otro número: ")
        #creando un try para que el programa no se caiga si el usuario ingresa letras
        try:
            #convirtiendo los numeros a enteros
            resultado = int(a) + int(b)
        #creando un except para que el programa no se caiga si el usuario ingresa letras
        except ValueError:
            print("No se puede sumar letras")
        #con el else se rompe el bucle infinito si el usuario ingresa numeros
        else:
            break
        #el finally se ejecuta siempre independientemente de si se ejecuta el try o el except
        finally:
            print("Manejo de excepciones finalizado")
                    
    return resultado

print(sumar_numeros())