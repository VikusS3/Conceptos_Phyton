#creando un diccionario con dic
diccionario= dict({"nombre":"Carlos", "edad":22, "cursos":["Python", "Django", "JavaScript"]})


#las listas no pueden ser llaves de un diccionario y usamos frozenset para meter un conjunto
diccionario= {frozenset([1,2,3]):"valor"}

#creando un diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido"])


print(diccionario)