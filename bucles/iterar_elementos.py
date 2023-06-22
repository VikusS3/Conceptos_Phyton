#crear una lista tambien sirve los mismo para tuplas,conjuntos
animales = ['perro', 'gato', 'serpiente', 'tortuga', 'pez']
numeros = [50,41,45,25,32]

for animal in animales:
    print(animal)
    print('Este animal es un ' + animal + '\n')

for numero in numeros:
    resultado = numero * 2
    print(resultado)

#recorer dos listas a la vez usando el metodo zip
for animal, numero in zip(animales, numeros):
    print(f"recorriendo la lista 1 {numero}")
    print(f"recorriendo la lista 2 {animal}")

#forma correcta de recorrer una lista
for num in enumerate(numeros):
    indice=num[0]
    valor = num[1]
    print(f"el indice es {indice} y el valor es {valor}")

#usando el forelse
for numero in numeros:
    print(f"ejecuntando el ultimo bucle, valor actual {numero}")
else:
    print("el bucle a terminado")
    