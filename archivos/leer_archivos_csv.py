import csv

with open("Conceptos_Phyton\\archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)



# forma de leer archivos csv
# with open("Conceptos_Phyton\\archivos\\datos.csv", "r") as archivo:
#     for linea in archivo:
#         print(linea, end=" ")