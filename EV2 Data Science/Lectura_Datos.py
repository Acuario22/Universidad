import pandas as pd

df_simce_2018 = pd.read_excel("simce2m2018_rbd.xlsx")

df_simce_2022 = pd.read_excel("simce2m2022_rbd.xlsx")

df_simce_2023 = pd.read_excel("simce2m2023_rbd.xlsx")


#2. Definir las columnas que queremos conservar
#Estas son nuestras variables (X) y nuestro objetivo (Y)
columnas_esenciales = [
    'agno',            # El año
    'rbd',             # El ID del colegio
    'cod_grupo',       # Feature X: El grupo socioeconómico
    'cod_depe1',       # Feature X: La dependencia (Municipal, Part. Subv, etc.)
    'cod_rural_rbd',   # Feature X: Si es rural (0 o 1)
    'prom_mate2m_rbd'  # Nuestro Target Y: El puntaje de matemáticas
]

#3. Seleccionar solo esas columnas en cada DataFrame
# (Ignoramos errores por si alguna columna faltara, aunque no debería)
df_simce_2018_limpio = df_simce_2018[columnas_esenciales].copy()
df_simce_2022_limpio = df_simce_2022[columnas_esenciales].copy()

# El archivo de 2023 no tiene 'agno' al inicio, pero sí al final. Lo seleccionamos igual.
# Re-ordenamos las columnas del 2023 para que coincida por si acaso
columnas_2023 = [
    'rbd',
    'cod_grupo',
    'cod_depe1',
    'cod_rural_rbd',
    'prom_mate2m_rbd',
    'agno' # La columna 'agno' está al final en este archivo
]
df_simce_2023_limpio = df_simce_2023[columnas_2023].copy()
# Reordenamos para que 'agno' quede al principio como los demás
df_simce_2023_limpio = df_simce_2023_limpio[columnas_esenciales]


#4. Unir (Concatenar) los 3 años en un solo "Dataset Maestro"
df_maestro = pd.concat([df_simce_2018_limpio, df_simce_2022_limpio, df_simce_2023_limpio], ignore_index=True)


#5. Verificar el resultado
print("--- Información del Dataset Maestro Creado ---")
print(df_maestro.info())

print("\n--- Primeras filas del Dataset Maestro ---")
print(df_maestro.head())

print(f"\nTotal de filas (colegios) en el dataset: {len(df_maestro)}")

#6. Guardar el Dataset Maestro en un nuevo archivo Excel
df_maestro.to_excel("dataset_maestro_simce_matematicas_2018_2022_2023.xlsx", index=False)

