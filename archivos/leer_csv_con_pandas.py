import pandas as pd

# Leer un archivo csv con pandas es muy sencillo y se hace con la función read_csv()
# que recibe como parámetro el nombre del archivo a leer. 
#el df es un dataframe que es una estructura de datos de pandas que es muy similar a una tabla de excel
#ponerle names a las columnas del dataframe se unsa names ejemplo names=['nombre', 'edad', 'ciudad']
df = pd.read_csv('Conceptos_Phyton/archivos/datos.csv')
df2 = pd.read_csv('Conceptos_Phyton/archivos/datos.csv')

# para imprimir el dataframe se usa la función print() y se pasa como parámetro el nombre del dataframe
#especificando el nombre de la columna que se quiere imprimir  
nombres=df['nombre']


#ordenando el dataframe por la edad forma ascendente
df_ordenado_ascendente=df.sort_values("edad")
# print(df_ordenado)

#ordenando el dataframe por la edad forma descendente
df_ordenado_descendente=df.sort_values("edad", ascending=False)
# print(df_ordenado_descendente)

#concanetando dos dataframes
df_concatenado=pd.concat([df,df2])
# print(df_concatenado)


#accediendo a la primera fila con head() y especificando el número de filas que se quiere
df_primer_fila=df.head(1)
# print(df_primer_fila)

#acciediendo a la última fila con tail() y especificando el número de filas que se quiere
df_ultima_fila=df.tail(1)
# print(df_ultima_fila)

#accediendo a la cantidad de filas y columnas del dataframe
df_filas_columnas=df.shape
# print(df_filas_columnas)


#obtiniendo estadisticas del dataframe  
df_estadisticas=df.describe()
# print(df_estadisticas)


#accediendo a un elemento espeficico del dataframe con loc
df_elemento_especifico=df.loc[0, 'nombre']
# print(df_elemento_especifico)


#accediendo a un elemento espeficico del dataframe con iloc
df_elemento_especifico_iloc=df.iloc[0, 1]
# print(df_elemento_especifico_iloc)

#la difenrecia entre loc y iloc es que loc accede a los elementos por el nombre de la columna 
#y iloc accede a los elementos por el indice de la columna 



#accediento a todas las filas de una columna
apellidos=df.iloc[:,1]
# print(apellidos)


#accediendo a la fila 3 con loc
df_fila_3=df.loc[2,:]
# print(df_fila_3)


#accediendo a filas con la edad mayor a 20
df_mayor_20=df[df['edad']>20]
print(df_mayor_20)