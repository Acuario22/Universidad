#Cuenta cuántos estudiantes aprobaron todas sus asignaturas (todas las notas >= 4.0).

from datos import df_estudiantes
import numpy as np

#Verifica si cada estudiante aprobó todas sus notas
aprobados = df_estudiantes["notas"].apply(
    lambda lista_notas: np.all( np.array(lista_notas) >= 4.0) 
    ).sum()

print("Cantidad de estudiantes que aprobaron todas sus asignaturas:", aprobados)