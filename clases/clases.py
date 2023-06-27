##clases##

class Persona:
    #la palabra reservada pass se utiliza para indicar que la clase esta vacia
    #de lo contrario se generaria un error
    pass

class Empleado:
    #esto de aca es un constructor de la clase se utiliza para inicializar los atributos de la clase
    #self es una referencia a la instancia de la clase
    def __init__(self, nombre, apellido, edad, sueldo):
        #el self es como el this de java y se utiliza para referenciar a los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sueldo = sueldo
    
    def caminar(self):
        print(f"{self.nombre} El empleado esta caminando")

my_empleado = Empleado("Juan", "Perez", 30, 50000)#se crea una instancia de la clase Empleado y se le pasan los parametros del constructor
print(my_empleado.nombre) #se imprime el atributo nombre de la clase Empleado

my_empleado.caminar() #se llama al metodo caminar de la clase Empleado