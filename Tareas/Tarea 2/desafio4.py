#¿Que porcentaje de estudiantes tiene al menos una nota bajo 4.0?

from datos import df_estudiantes
import numpy as np

#Verificar si cada estudiante tiene al menos una nota menor a 4.0
estud_bajo_cuatro = df_estudiantes["notas"].apply(lambda notas: np.any( np.array(notas) < 4.0) ).sum()

#Calculo del porcentaje de estudiantes con al menos una nota bajo 4.0
porcentaje_bajo_cuatro = estud_bajo_cuatro / len(df_estudiantes) * 100

print("El porcentaje de estudiantes que tienen al menos una nota bajo 4.0 es del:",round(porcentaje_bajo_cuatro,1),"%")

