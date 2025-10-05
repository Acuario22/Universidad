import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""
Tarea 4: Regresión Lineal Múltiple
Predicción de goles de la Universidad de Chile contra Deportes La Serena.

Objetivo:
Intentaremos estimar cuántos goles podría marcar la U de Chile usando datos históricos de partidos entre ambos equipos.  

Fuentes:
- https://www.livefutbol.com/equipos/universidad-de-chile/la-serena/11
- https://www.latercera.com/el-deportivo/noticia/hace-15-anos-que-la-u-no-cae-con-la-serena-en-el-nacional/EYXLS76A25E3RHQAGJGB355MQA/
"""


# 1. Datos y DataFrame

#Creamos un diccionario con los datos históricos de partidos
#Local: 1 si la U jugó de local, 0 si fue visitante
#Goles_a_favor: goles anotados por la U en ese partido
#Goles_en_contra: goles recibidos por la U en ese partido
datos = {
    'Local': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    'Goles_a_favor': [3, 3, 1, 3, 2, 0, 0, 1, 3, 2, 3, 0, 4, 1, 1, 3, 3, 5, 4, 2, 3, 0, 0, 1, 2, 2, 3, 5],
    'Goles_en_contra': [1, 1, 3, 2, 2, 3, 0, 1, 1, 2, 2, 3, 2, 2, 1, 0, 1, 2, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1]
}
df = pd.DataFrame(datos)

#2. Variables predictoras y objetivo

#X: columnas que usamos para predecir
#y: columna que queremos predecir 
X = df[['Local', 'Goles_en_contra']]
y = df['Goles_a_favor']


#3.Dividir datos y entrenar el modelo

#Dividimos los datos en entrenamiento (70%) y prueba (30%) para evaluar el modelo
#random_state=42 asegura que la división sea siempre la misma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Creamos y entrenamos el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)


#4.Predecir y evaluar el modelo

#Predecimos los goles en los datos de prueba
y_pred = model.predict(X_test)

#Calculamos métricas para evaluar el modelo
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  #Error promedio de predicción en goles
r2 = r2_score(y_test, y_pred)                       #Qué tan bien explica el modelo la variación de los goles


print(f"Resultados de la evaluación:")
print(f"RMSE: {rmse:.2f} (error promedio de {rmse:.0f} goles)")
print(f"R-Cuadrado (R^2): {r2:.2f} (El modelo explica el {r2:.0%} de la variación de los goles)")


#5.Predicción del próximo partido
#Supondremos que la U jugará de local y La Serena no anotará goles
prox_partido = pd.DataFrame([[1, 0]], columns=['Local', 'Goles_en_contra'])
pred = model.predict(prox_partido)
print("\nPredicción del próximo partido:")
print(f"Goles de Universidad de Chile: {pred[0]:.1f} ≈ {round(pred[0])} goles")


