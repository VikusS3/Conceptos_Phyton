#dos listas una con nombres y otra con apellidos
nombres = ["Juan", "Pedro", "Maria", "Ana", "Luis", "Jose", "Carlos", "Andres", "Jorge", "Alberto"]
apellidos = ["Gomez", "Perez", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Sanchez", "Torres", "Suarez", "Ramirez"]


#registrarlos en un txt


with open("archivos_resolviendo_problemas\\nombres_y_apellidos", "w") as archivo:
    archivo.write("Nombres y apellidos\n\n")
    [archivo.write(f"Nombre: {n}\nApellidos: {a}\n----------\n") for n,a in zip(nombres, apellidos)]
    
#leer el txt y mostrarlo en pantalla
