#Calcular el promedio total del curso

from datos import df_estudiantes
import numpy as np

#Calcular el promedio de cada estudiante
df_estudiantes["promedio"] = df_estudiantes["notas"].apply(np.mean).round(1)

#Calcular el promedio general del curso a partir de los promedios de los estudiantes
promedio_total = df_estudiantes["promedio"].mean().round(1)

print("El promedio general del curso es:", promedio_total)