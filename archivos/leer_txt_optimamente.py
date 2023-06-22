# Leer un archivo de texto optimamente con with open as archivo (no es necesario cerrar el archivo) 
with open("Conceptos_Phyton\\archivos\\archivo_saul.txt", encoding="utf8") as archivo:
    print(archivo.read()) 