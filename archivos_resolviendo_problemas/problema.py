import pandas as pd

df=pd.read_csv('archivos_resolviendo_problemas\\datos.csv')

#cambiar el tipo de un dato de una columna a string
#astype(str) convierte a string
df['edad']=df['edad'].astype(str)

#mostrar el tipo de dato de la columna edad
# print(type(df['edad'][0]))


#reemplazar un valor de una columna por otro
df['apellido'].replace('gomez', 'Pancracios', inplace=True)


#eliminar filas con datos que faltan
df=df.dropna()


#eliminar las filas repetidas
df=df.drop_duplicates()

#creando un cvs con los datos del dataframe resultante
df.to_csv('archivos_resolviendo_problemas\\datos_resultantes.csv', index=False)
