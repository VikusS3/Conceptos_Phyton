import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dt=pd.read_csv("archivos_problemas_graficos/cambios.csv")

#la funcion lineplot de seaborn nos permite graficar una linea x serian las fechas y las y los valores
# y el tercer parametro es el dataframe para que tome los datos
sns.lineplot(x="fecha", y="cambio", data=dt)

#creando un punto en el grafico con la funcion plot de matplotlib donde
#donde indica el eje x, el eje y y el tipo de punto
plt.plot("01-07",9,"o")

#mostrando el grafico
plt.show()