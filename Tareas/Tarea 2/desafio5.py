#Entrega un listado ordenado (de mayor a menor) de los estudiantes según su promedio.
from datos import df_estudiantes
import numpy as np

#Obtener el promedio de cada estudiante
df_estudiantes["promedio"] = df_estudiantes["notas"].apply(np.mean).round(1)

# Ordenar el DataFrame de mayor a menor según el promedio
lista_ordenada = df_estudiantes.sort_values(by="promedio", ascending=False)

print("Lista ordenada de mayor a menor según el promedio de los estudiantes")
#Mostrar unicamente nombre y promedio, sin el indice, para facilitar la lectura
print(lista_ordenada[["nombre", "promedio"]].to_string(index=False))