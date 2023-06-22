#creando una lista con list()
lista = list(["hola","mundo",36])

#agregando len podemos saber la cantidad de elementos de la lista
canitdad_de_elementos = len(lista)

#agregando append podemos agregar un elemento al final de la lista
lista.append("nuevo elemento")

#agregando un elemento en una posicion especifica
lista.insert(2,"elemento en la posicion 2")

#agregando varios elementos a la lista con extend
lista.extend(["elemento 1","elemento 2"])

#eliminando un elemento de la lista por su indice
lista.pop(3) #si ponemos -1 eliminamos el ultimo elemento

#removiendo un elemento de la lista por su valor
lista.remove("elemento en la posicion 2") #si no existe el elemento nos dara un error

#ordenando una lista con sort de forma ascendente
lista.sort(reverse=True) #si ponemos reverse=True ordenamos de forma inversa

#con clear eliminamos todos los elementos de la lista
#lista.clear()

print(lista)


