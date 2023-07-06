# Contador de vocales: Crea un programa que solicite una cadena de texto al usuario
# y cuente el número de vocales que contiene. 
# Puedes ignorar las mayúsculas y considerar solo las vocales sin tilde (a, e, i, o, u).

def contar_vocales(cadena):
    vocales = "aeiou"
    contador = 0
    # Recorremos la cadena de texto y comparamos cada letra con las vocales definidas en la variable vocales
    # Si la letra se encuentra en la variable vocales, aumentamos el contador en 1 unidad 
    for letra in cadena:
        if letra.lower() in vocales:
            contador += 1
    return contador


resultado = contar_vocales("Hola Mundo Me llamo saul y estoy resolviendo un ejercicio")
print(resultado)

