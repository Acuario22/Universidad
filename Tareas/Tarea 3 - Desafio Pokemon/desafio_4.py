import pandas as pd

from cargar_datos import df_pokemon

import seaborn as sns
import matplotlib.pyplot as plt         #Para mostrar los gráficos  
import numpy as np

'''
4. Visualización de datos
-------------------------
- Haz un histograma de los valores de ataque.
- Realiza un gráfico de dispersión entre ataque y velocidad.
- Haz un boxplot de los PS por tipo principal (Tipo 1).
- Grafica la distribución de la defensa usando un diagrama de violín.
'''

#1-Crear un histograma de los valores de ataque.

#histplot de Seaborn para graficar histogramas
sns.histplot(df_pokemon["Ataque"], edgecolor = "black")

#Agregamos un título al gráfico para describirlo
plt.title("Histograma de los valores de ataque")
plt.xlabel("Valor del ataque")
plt.show()

#2-Crear un gráfico de dispersión entre ataque y velocidad.
#Ataque será el eje X y Velocidad el eje Y. 
#El argumento data indica de dónde se sacan esas columnas.
sns.scatterplot(x="Ataque", y="Velocidad", data=df_pokemon, edgecolor="black")

plt.title("Grafico de dispersión ataque vs velocidad")
plt.xlabel("Ataque")
plt.ylabel("Velocidad")
plt.show()

#3-Crear un boxplot de los PS por tipo principal (Tipo 1)
sns.boxplot(x="Tipo 1", y="PS", data=df_pokemon)

plt.title("Boxplot de PS por Tipo 1")
plt.xlabel("Tipo 1")
plt.ylabel("PS")
plt.show()

#4-Grafica la distribución de la defensa usando un diagrama de violín.
sns.violinplot(y="Defensa", data=df_pokemon)

plt.title("Diagrama de violín de la defensa")
plt.ylabel("Defensa")
plt.show()