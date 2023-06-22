#formas de llamar a otros modulos desde este modulo
#llamar a otros modulos desde este modulo
import modulo_saludar

modulo_saludar.saludar("Juan")

#llamar a otros modulos desde este modulo
from modulo_saludar import saludar
saludar("Juan")

#llamar a otros modulos desde este modulo
from modulo_saludar import *
saludar("Juan")

#llamar a otros modulos desde este modulo
from modulo_saludar import saludar as saludar_persona
saludar_persona("Juan")

#llamar a otros modulos desde este modulo
import modulo_saludar as saludar
saludar.saludar("Juan")

#llamar a otros modulos desde este modulo
from modulo_saludar import saludar as saludar_persona
saludar_persona("Juan")



