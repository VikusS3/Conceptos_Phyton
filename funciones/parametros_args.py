#utilizando el *args para pasar un numero indeterminado de parametros

def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}" 

resultado= suma("saul",7,1,5,10,25)
print(resultado)