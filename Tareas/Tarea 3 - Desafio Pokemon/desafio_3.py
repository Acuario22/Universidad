import pandas as pd
from cargar_datos import df_pokemon
''' 
3. Estadística descriptiva básica
---------------------------------
- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
- ¿Cuántos Pokémon tienen dos tipos?
- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
'''

#Calculamos el promedio de Ataque de todos los Pokémon
ataque_promedio = df_pokemon["Ataque"].mean()
print()
print("El promedio del ataque de todos los pokemon es:")
print(round(ataque_promedio,1))

#Calculamos la mediana de Ataque de todos los Pokémon
ataque_mediana = df_pokemon["Ataque"].median()
print()
print("La mediana del ataque de todos los pokemon es:")
print(ataque_mediana)

#Calculamos la moda de Ataque de todos los Pokémon
#tomamos el primer valor si hay varias modas, ya que mode() devuelve una Serie.
ataque_moda = df_pokemon["Ataque"].mode()[0]   
print()
print("La moda del ataque de todos los pokemon es:")
print(ataque_moda)


#Buscamos el Pokémon con mayor Defensa
max_defend = df_pokemon["Defensa"].max()
pokemon_max_defend = df_pokemon[ df_pokemon["Defensa"] == max_defend ] ["Nombre"].values[0]
print()
print("El pokemon con mayor defensa es:", pokemon_max_defend, "con", max_defend)

#Buscamos el Pokémon con menor Velocidad
min_speed = df_pokemon["Velocidad"].min()
pokemon_min_speed = df_pokemon[ df_pokemon["Velocidad"] == min_speed ] ["Nombre"].values[0]
print()
print("El pokemon con menor velocidad es:", pokemon_min_speed, "con", min_speed)

#Contamos cuántos Pokémon tienen dos tipos (Tipo 2 distinto de "Ninguno")
dos_tipos = df_pokemon[df_pokemon["Tipo 2"] != "Ninguno"].shape[0]
#shape[0] nos da la cantidad de filas y shape[1] la cantidad de columnas.
print()
print("La cantidad de pokemones con dos tipos es de:", dos_tipos)