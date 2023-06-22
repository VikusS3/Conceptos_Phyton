diccionario ={
    "nombre": "Carlos",
    "edad": 22,
    "meta" : 1000000
}

##metdo keys sirve para mostrar las claves del diccionario
clave = diccionario.keys()
#obte4niendo el valor de la clave con el metodo get
clave = diccionario.get("edad")

#eliminando un elemento del diccionario con pop
diccionario.pop("meta")

#obteniendo un valor del diccionario con diccionario
diccionario_iterable = diccionario.items()

print(diccionario_iterable)

#eliminando todos elemento del diccionario con clear
##diccionario.clear()

