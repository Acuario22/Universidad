import pandas as pd

from cargar_datos import df_pokemon
#print(df_pokemon)

'''
2. Filtrado y selección
-----------------------
- Filtra todos los Pokémon de tipo "Fuego".
- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
'''


#tipo_fuego = df_pokemon["Tipo 1"].all(lambda x:x "")
#all es para verficar o aplicar a todos, no filtrar

tipo_fuego = df_pokemon[ (df_pokemon["Tipo 1"] == "Fuego") | (df_pokemon["Tipo 2"] == "Fuego") ]
print("Pokemons tipo fuego")
print(tipo_fuego)


#Se usa doble corchetes para seleccionar varias columnas
select = df_pokemon[ ["Nombre", "Tipo 1", "Ataque", "Velocidad"] ]
print()
print(select)