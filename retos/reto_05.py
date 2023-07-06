# Validador de tarjetas de crédito: Escribe un programa que valide si un número 
# de tarjeta de crédito es válido utilizando el algoritmo de Luhn. El programa 
# debe solicitar al usuario que ingrese un número de tarjeta de crédito y determinar 
# si es válido o no.

def soliciat_tarjeta():
    numero_de_tarjeta = input("Introduce el numero de tarjeta: ")
    return numero_de_tarjeta

def validar_tarjeta_luhn(numero_de_tarjeta):
    # Convertimos el numero de tarjeta en una lista de digitos 
    digitos = [int(x) for x in str(numero_de_tarjeta)]
    #ponemos corchetes para que se convierta en una lista y no en un string 
    # Multiplicamos por 2 los digitos que se encuentran en las posiciones pares de la lista
    #enumerate nos permite recorrer la lista y obtener el indice de cada elemento
    digitos_duplicados = [x * 2 if i % 2 == len(digitos) % 2 else x for i, x in enumerate(digitos)]
    
    digitos_sumados = [x-9 if x>=10 else x for x in digitos_duplicados]
    
    # Sumamos todos los digitos de la lista 
    suma = sum(digitos_sumados)
    
    if suma%10 == 0:
        print("La tarjeta es valida")
    else:
        print("La tarjeta no es valida")
        

reultado = soliciat_tarjeta()

validar_tarjeta_luhn(reultado)

        

