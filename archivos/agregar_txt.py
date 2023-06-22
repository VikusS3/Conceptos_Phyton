# Agregar texto a un archivo de texto con with open as archivo (no es necesario cerrar el archivo)
# con w sobreescribe el archivo y con a agrega al final del archivo

with open("Conceptos_Phyton\\archivos\\archivo_saul.txt", "a", encoding="utf8") as archivo:
    #usa un for para agregar 10 lineas al archivo
    # for i in range(10):
    #     archivo.write(f"esta es la linea {i}\n")

    #adaptar todo el codigo anterior a una sola linea de codigo
    #usa un list comprehension para agregar 10 lineas al archivo
    [archivo.write(f"esta es la linea {i}\n") for i in range(10)]
