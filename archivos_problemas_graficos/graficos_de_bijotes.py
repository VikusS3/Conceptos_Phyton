import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("archivos_problemas_graficos/bigotes.csv")

#con boxplot se crea el grafico de bigotes estos graficos son muy utiles para ver la distribucion de los datos
sns.boxplot(x="categoria",y="valor",data=df)

plt.show()