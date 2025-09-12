import pandas as pd

from cargar_datos import df_pokemon

'''
6. Agrupamiento y análisis por grupo
-------------------------------------
- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
- ¿Qué tipo tiene el mayor promedio de velocidad?
- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
'''

#a)
#Seleccionar solo las columnas Tipo 1 y Ataque
ataque_and_tipo1 = df_pokemon[["Tipo 1", "Ataque"]]

#groupby("Tipo 1") separa el DataFrame en grupos, en este caso, un grupo por cada tipo principal de Pokémon.
#agg(...) sirve para aplicar una o varias funciones estadisticas a cada grupo.

estadistica_por_ataque = ataque_and_tipo1.groupby("Tipo 1").agg(
    Promedio=("Ataque", "mean"),        #calcula el promedio dentro de cada grupo
    Mediana=("Ataque", "median"),       #calcula la mediana dentro de cada grupo
    Desviación=("Ataque", "std")        #calcula la desviación estándar dentro de cada grupo
).round(1)

print("Estadísticas de promedio, mediana y desviación estándar de ataque por cada tipo principal (Tipo 1):")
print(estadistica_por_ataque)

#b)

#seleccionar solo las columnas Tipo 1 y Velocidad
velocidad_and_tipo1 = df_pokemon[["Tipo 1", "Velocidad"]]

#Agrupar por Tipo 1 y calcular el promedio de Velocidad
tipo_velocidad_promedio = velocidad_and_tipo1.groupby("Tipo 1").agg(
    Promedio = ("Velocidad","mean")
).round(1)

#Encontrar el tipo con mayor promedio de velocidad
mayor_velocidad = tipo_velocidad_promedio["Promedio"].max()
print()
print("El tipo con mayor promedio de velocidad es:")
print(tipo_velocidad_promedio[tipo_velocidad_promedio["Promedio"] == mayor_velocidad])

#c)
#Agrupamos los Pokémon por su tipo principal 
#y usamos idxmax()/idxmin() para encontrar el índice de la fila que tiene el PS más alto/bajo en cada grupo.
#idxmax()/idxmin() devuelve la posición exacta de la fila con el valor máximo de la columna "PS".
max_ps = df_pokemon.groupby("Tipo 1")["PS"].idxmax()
min_ps = df_pokemon.groupby("Tipo 1")["PS"].idxmin()

#.loc para seleccionar las filas del DataFrame usando los índices que encontramos con idxmax()/idxmin().
#Solo seleccionamos las columnas "Tipo 1", "Nombre" y "PS" para mostrar lo necesario.
pokemon_mayor_ps = df_pokemon.loc[max_ps, ["Tipo 1", "Nombre", "PS"]]
pokemon_menor_ps = df_pokemon.loc[min_ps, ["Tipo 1", "Nombre", "PS"]]

print()
print("Pokémon con mayor PS por cada tipo principal es:")
print(pokemon_mayor_ps.to_string(index=False))
print()
print("Pokémon con menor PS por cada tipo principal es:")
print(pokemon_menor_ps.to_string(index=False))