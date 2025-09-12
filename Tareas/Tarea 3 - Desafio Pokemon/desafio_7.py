import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from cargar_datos import df_pokemon

'''
7. Análisis exploratorio (EDA)
------------------------------
- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
- Identifica posibles outliers en los valores de ataque y PS usando boxplots.
'''


#Promedio de Ataque y Defensa por tipo para ver tendencias
ataque_defensa_promedio = df_pokemon.groupby("Tipo 1")[["Ataque", "Defensa"]].mean().round(1)
print()
print("Promedio de Ataque y Defensa por Tipo:")
print(ataque_defensa_promedio)

#Correlación entre ataque y velocidad
correlacion = df_pokemon["Ataque"].corr(df_pokemon["Velocidad"])
print()
print("Coeficiente de correlación entre Ataque y Velocidad:", round(correlacion, 2))
#Un valor cercano a 1 indica correlación positiva fuerte,
#cercano a 0 indica poca  correlación,
#cercano a -1 indica correlación negativa.

#Dispersión de PS por tipo usando desviación estándar
ps_dispersion = df_pokemon.groupby("Tipo 1")["PS"].std().round(1)
print()
print("Desviación estándar de PS por tipo:")
#Tipos con mayor desviación estándar tienen PS más dispersos,
#mientras que los de menor desviación estándar son más homogéneos.
print(ps_dispersion)

# Detectar posibles outliers en Ataque y PS con boxplots

# Boxplot de Ataque por tipo
plt.subplot(1, 2, 1)        #Crear un subplot (gráfico dentro de la figura) en una fila y dos columnas,
sns.boxplot(x="Tipo 1", y="Ataque", data=df_pokemon)
plt.xticks(rotation=90)     # Rotar las etiquetas del eje x para mejor visibilidad
plt.title("Boxplot de Ataque por Tipo")

# Boxplot de PS por tipo
plt.subplot(1, 2, 2)        #Crear el segundo subplot en la misma figura (misma fila, segunda columna),
sns.boxplot(x="Tipo 1", y="PS", data=df_pokemon)
plt.xticks(rotation=90)
plt.title("Boxplot de PS por Tipo")

plt.tight_layout()          #ajustar espacios
plt.show()
#Los puntos que aparecen fuera de los "bigotes" de los boxplots son posibles outliers.