#tipo de dato compuesto: listas y tuplas
#en las "listas" se pueden modificar los elementos mientras que en las "tuplas" no
lista = ["Saul Orellana",True, 1.75, "Python"]
tupla = ("Saul Orellana",True, 1.75, "Python")

lista[3]="Java"

print(lista[3])

#creando un conjunto set
#en un conjunto no se pueden repetir elementos y no se accede a los datos por su indice
conjunto = {"Saul Orellana",True, 1.75, "Python"}
print(conjunto)

#creando un diccionario (dict), su estructura es clave:valor y separados por comas
diccionario =  {
    'nombre': 'Saul Orellana',
    "canal": "VikusS3",
    'edad': 21,
    'altura': 1.75,
    'dato_duplicado':'Saul Orellana'
}

print(diccionario['edad'])