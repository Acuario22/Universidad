#Cuál es la nota más frecuente (moda) considerando todas las notas de los estudiantes

from datos import df_estudiantes
import pandas as pd

#Cada elemento de la lista de notas se convierte en una fila individual
fila_de_notas = df_estudiantes["notas"].explode()

#Para obtener la nota mas frecuente
nota_frecuente = fila_de_notas.mode()

print("La nota con mayor frecuencia fue:", nota_frecuente.values[0])