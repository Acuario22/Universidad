import pandas as pd
import os

base_dir = os.path.dirname(__file__)   # carpeta del script
csv_path = os.path.join(base_dir, "pokemon_primera_gen_limpio.csv")

df_pokemon = pd.read_csv(csv_path)

'''
#Leemos el archivo CSV y lo almacenamos en un DataFrame.
df_pokemon = pd.read_csv("pokemon_primera_gen_limpio.csv")
'''

#print(df_pokemon)
#print(df_pokemon.head(30)) muestras unicamente las n primeras filas.
