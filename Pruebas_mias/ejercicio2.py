
#creamos una funcion que recibe como parametro la cantidad de alumnos
def obtener_alumnos(cantidad_de_alumnos):
    alumnos = []
    for i in range(cantidad_de_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        #creamos una tupla con los datos del alumno
        alumno = (nombre, edad)
        #agregamos la tupla a la lista de alumnos
        alumnos.append(alumno)
    #ordenamos la lista de alumnos por edad
    #la funcion sort() ordena la lista de menor a mayor
    alumnos.sort(key=lambda x:x[1])
    #el asistente es el primer alumno de la lista
    asistente = alumnos[0][0]
    #el profesor es el ultimo alumno de la lista
    profesor = alumnos[-1][0]
    return asistente, profesor

#llamamos a la funcion y guardamos los valores que retorna
#en las variables asistente y profesor
asistente, profesor = obtener_alumnos(5)

print(f"El asistente es {asistente} y el profesor es {profesor}")