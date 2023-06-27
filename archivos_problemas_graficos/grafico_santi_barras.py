import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("archivos_problemas_graficos/santi_ingresos.csv")

sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo el total de ingresos de todas las fuentes para mostrarlo en el grafico
total_de_ingresos=df["ingresos"].sum()

print(f"El total de ingresos es: ${total_de_ingresos}")

plt.show()