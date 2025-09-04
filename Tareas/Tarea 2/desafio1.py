#Calcula el promedio de notas de cada estudiante y determina quién tiene el promedio más alto y más bajo.

from datos import df_estudiantes
import numpy as np

#Se aplica np.mean para obtener el promedio de cada lista de la columna "notas"
df_estudiantes["promedio"] = df_estudiantes["notas"].apply(np.mean).round(1)

#max y min, para obtener el promedio más alto y el más bajo
promedio_alto = df_estudiantes["promedio"].max()
promedio_bajo = df_estudiantes["promedio"].min()

#Comparamos para encontrar al estudiante con el promedio más bajo y el más alto
estud_promedio_alto = df_estudiantes[ df_estudiantes["promedio"] == promedio_alto ] ["nombre"].values[0]
estud_promedio_bajo = df_estudiantes[ df_estudiantes["promedio"] == promedio_bajo ] ["nombre"].values[0]                           

print("Promedio de todos los estudiantes")
print(df_estudiantes)

print("Estudiante con el promedio más alto:", estud_promedio_alto, "con un", promedio_alto)
print("Estudiante con el promedio más bajo:", estud_promedio_bajo, "con un", promedio_bajo)