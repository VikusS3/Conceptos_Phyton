#creando una excepcion personalizada
class MiExcepcion(Exception):
    #con def __init__ se crea el constructor de la clase y se le pasa el parametro err
    #el parametro self es obligatorio en python, el cual hace referencia al objeto que se esta creando
    #el parametro err es opcional, el cual es el mensaje que se le pasa a la excepcion
    def __init__(self, err):
        print(f"Comentiste un error: {err}")
    
try:
    raise MiExcepcion("Error de prueba")
except:
    print("Se produjo un error")
    
#lanzando una excepcion con raise
raise MiExcepcion("Error de prueba")