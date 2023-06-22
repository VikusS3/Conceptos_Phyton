#escribir en un archivo de texto con with open as archivo (no es necesario cerrar el archivo)
#con w sobreescribe el archivo y con a agrega al final del archivo
with open("Conceptos_Phyton\\archivos\\archivo_saul.txt", "w", encoding="utf8") as archivo:
     #con el metodo write se escribe en el archivo de texto
     #archivo.write("hola como estas")
     #con el metodo writelines se escribe en el archivo de texto pero se puede escribir mas de una linea
     archivo.writelines(["Hola mundo\n","estoy casi por finalizar phyton"])
