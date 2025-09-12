import pandas as pd
from cargar_datos import df_pokemon

'''
5. Manipulación de datos
------------------------
- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
- Ordena el DataFrame por "Poder Total" de mayor a menor.
'''
#Crear una nueva columna "Poder Total.
poder_total = df_pokemon["Ataque"] + df_pokemon["Defensa"] + df_pokemon["Velocidad"] + df_pokemon["PS"]
df_pokemon["Poder Total"] = poder_total

#Ordenar el DataFrame por "Poder Total" de mayor a menor.
df_pokemon_ordenado= df_pokemon.sort_values(by="Poder Total", ascending=False)
print(df_pokemon_ordenado.to_string(index=False))