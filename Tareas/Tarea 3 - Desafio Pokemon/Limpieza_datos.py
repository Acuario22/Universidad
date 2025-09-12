import pandas as pd
import os

base_dir = os.path.dirname(__file__)   # carpeta del script
csv_path = os.path.join(base_dir, "pokemon_primera_gen.csv")

df_pokemon = pd.read_csv(csv_path)


'''
#Leemos el archivo CSV y lo almacenamos en un DataFrame.
df_pokemon = pd.read_csv("pokemon_primera_gen.csv")
#print(df_pokemon)
#print(df_pokemon.head(n)) muestras unicamente las n primeras filas.
'''


#Limpieza de datos

#1.El tipo acero se introdujo en la segunda generación, no en la primera.
df_pokemon.loc[ df_pokemon["Nombre"] == "Magnemite", "Tipo 2" ] = "Ninguno"
df_pokemon.loc[ df_pokemon["Nombre"] == "Magneton", "Tipo 2" ] = "Ninguno"
df_pokemon.loc[ df_pokemon["Nombre"] == "Jigglypuff", "Tipo 2" ] = "Ninguno"
df_pokemon.loc[ df_pokemon["Nombre"] == "Wigglytuff", "Tipo 2" ] = "Ninguno"
#loc[condicion, haz esto en la columna] = nuevo valor 
#Busca la fila donde el Pokémon se llama Magnemite/Magneton y cambia su Tipo 2 a Ninguno.

#2.Algunos pokémon no tienen un segundo tipo 
df_pokemon["Tipo 2"] = df_pokemon["Tipo 2"].fillna("Ninguno")
#fillna() reemplaza los valores vacíos por la palabra "Ninguno"

#3.Algunos pokémon tienen caracteres especiales en los nombres
df_pokemon["Nombre"] = df_pokemon["Nombre"].str.replace("♀", "H")
df_pokemon["Nombre"] = df_pokemon["Nombre"].str.replace("♂", "M")
#str.replace() se utiliza para buscar y reemplazar texto dentro de una columna de tipo string.

#print(df_pokemon.iloc[[31]])
#iloc se utiliza para seleccionar filas y columnas por posición numérica (índice),

#4.Verificar los valores
#Ver tipos de dato de cada columna
#print(df_pokemon.dtypes)

#Guardar el DataFrame limpio en un nuevo CSV
df_pokemon.to_csv("pokemon_primera_gen_limpio.csv", index=False)
