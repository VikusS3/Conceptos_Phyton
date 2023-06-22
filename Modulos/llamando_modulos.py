#importa modulos si no estan dentro de la carpeta del proyecto
# import sys

import sys
#agrega la ruta del modulo a la lista de rutas de python

sys.path.append("c:\\Users\\SAUL\\Documents\\Python\\Conceptos_Phyton\\funciones")

# print(sys.path)

import crear_funciones as cf    

#llamando a la funcion
cf.crear_contraseña(56)