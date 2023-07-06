# Juego del ahorcado: Crea un programa que implemente el juego del ahorcado. 
# El programa debe seleccionar una palabra al azar de una lista y permitir al 
# usuario adivinar letras. Muestra al usuario cuántas letras ha adivinado correctamente 
# y cuántas le quedan por adivinar.

# Importamos la libreria random para generar numeros aleatorios
import random

palabras_al_azar=['tomate', 'taxi', 'moto' , 'casa', 'perro', 'gato', 'raton', 'pajaro', 'pescado']

def selectionar_palabra():
    # Generamos un numero aleatorio entre 0 y la longitud de la lista de palabras
    numero_aleatorio = random.randint(0, len(palabras_al_azar)-1)
    # Devolvemos la palabra que se encuentra en la posicion del numero aleatorio
    return palabras_al_azar[numero_aleatorio]

def mostrar_palabra_oculta(palabras_al_azar, letras_adivinadas):
    palabra_oculta = ""
    for letra in palabras_al_azar:
        if letra in letras_adivinadas:
            palabra_oculta += letra + " "
        else:
            palabra_oculta += "_ "
    return palabra_oculta

def juego_ahorcado():
    intentos_maximos = 5
    intentos=0
    letras_adivinadas = []
    
    palabra=selectionar_palabra()
    
    while intentos < intentos_maximos:
        print("La palabra es: ", mostrar_palabra_oculta(palabra, letras_adivinadas))
        letra = input("Introduce una letra: ")
        
        if letra in palabra:
            print("Has acertado")
            letras_adivinadas.append(letra)
        else:
            intentos += 1
            print("Has fallado", intentos_maximos - intentos, "intentos restantes")
            
        if set(palabra) == set(letras_adivinadas):
            print("felicitaciones, has ganado")
            break
        
    if intentos == intentos_maximos:
        print("Has perdido, la palabra era: ", palabra) 
        
        
        

juego_ahorcado()
        
        


    
    
    