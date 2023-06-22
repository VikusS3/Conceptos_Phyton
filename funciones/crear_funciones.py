# creando una funcion
def saludar():
    print("hola mundo")

# llamando a la funcion
# saludar()

# agregando parametros a la funcion
def saludo(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "hombre":
        adjetivo = "guapo"
    elif sexo == "mujer":
        adjetivo = "guapa"
    else:
        adjetivo = "guap@"

    print("hola " + nombre + " que " + adjetivo + " eres")


# llamando a la funcion
saludo("jose", "ninguno")

#creando funciones para que nos retornen valores
def crear_contraseña(num):
    chars="12sdqwd5fa9s6d"
    num_entero=str(num)
    num=int(num_entero[0])
    c1=num-2
    c2=num-1
    c3=num
    contraseña=f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    #la palabra reservada return nos permite retornar un valor para que sea usado en otra parte del codigo
    print(contraseña)
    return contraseña
    
# password=crear_contraseña(123)
# print(password)


