archivo=open("Conceptos_Phyton\\archivos\\archivo_saul.txt", "r", encoding="utf8")


#leer linea por linea
linea_1=archivo.readlines()

#cerrar archivo
archivo.close()

print(linea_1)
# print(archivo.read())