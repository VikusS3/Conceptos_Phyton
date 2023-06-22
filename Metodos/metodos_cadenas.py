cadena1= "Hola soy Saul"
cadena2 = "Bienvenido,a,Python"

#la funcion dir nos muestra todos los metodos que podemos usar con la varibale expecificada
#print(dir(cadena1))


#Los metodos funciona dato + . + metodo + ()
resultado =  cadena1.upper() #metodo upper convierte la cadena a mayusculas
print(resultado)

resultado = cadena1.lower() #metodo lower convierte la cadena a minusculas
print(resultado)

resultado = cadena1.capitalize() #metodo capitalize convierte la primera letra de la cadena a mayuscula
print(resultado)

resultado = cadena1.find("z") #metodo find busca la palabra en la cadena y devuelve la posicion de la primera letra si no la encuentra devuelve -1
print(resultado)

resultado = cadena1.index("S") #metodo index busca la palabra en la cadena y devuelve la posicion de la primera letra
print(resultado)

#si es numero devuelve true si no false
resultado = cadena1.isnumeric() #metodo isnumeric
print(resultado)

#si es alfanumerico devuelve true si no false
resultado = cadena1.isalpha() #metodo isalpha
print(resultado)

resultado =cadena2.count("i") #metodo count cuenta cuantas veces se repite la letra en la cadena
print(resultado)

resultado = len(cadena2) #funcion len devuelve la longitud de la cadena
print(resultado)

resultado= cadena2.startswith("B") #metodo startswith devuelve true si la cadena empieza con la letra especificada
print(resultado)

resultado= cadena2.endswith("m") #metodo endswith devuelve true si la cadena termina con la letra especificada
print(resultado)

cadena_nueva = cadena1.replace("Saul","Saulo") #metodo replace remplaza la palabra especificada por la nueva palabra
print(cadena_nueva)

#separar cadenas con una que le damos
cadena_separada= cadena2.split(",") #metodo split separa la cadena en una lista
print(cadena_separada)