#Tarea 5: Regresión Lineal Múltiple para predecir precios de departamentos
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


"""
Una corredora de propiedades en Santiago quiere predecir el precio (en UF) de departamentos. Tienen los siguientes datos:
datos = {'Superficie_m2': [50, 70, 65, 90, 45], 'Num_Habitaciones': [1, 2, 2, 3, 1], 
'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0], 'Precio_UF': [2500, 3800, 3500, 5200, 2100]}
Construye un modelo de regresión lineal múltiple para predecir el 'Precio_UF' y evalúa su rendimiento.
"""


#1.Datos y DataFrame
datos = {'Superficie_m2': [50, 70, 65, 90, 45],
         'Num_Habitaciones': [1, 2, 2, 3, 1],
         'Distancia_Metro_km': [0.5, 1.2, 0.8, 0.2, 2.0],
         'Precio_UF': [2500, 3800, 3500, 5200, 2100]
        }
df = pd.DataFrame(datos)

#2.Definir X (múltiple) e y
X = df[['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km']]
y = df['Precio_UF']


#3.Dividir datos y entrenar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

#4.Predecir y evaluar
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))          #Error promedio
r2 = r2_score(y_test, y_pred)                               #Qué tanto explica el modelo

print(f"Resultados del modelo:")
print(f"RMSE: {rmse:.2f} UF (error promedio del modelo)")    
print(f"R-Cuadrado (R^2): {r2:.2f} (El modelo explica el {r2:.0%} de la variación de los precios)")


#Predicción para un nuevo departamento
#Supongamos un departamento de 60 m², 2 habitaciones y a 0.7 km del metro
nuevo_precio = pd.DataFrame([[60, 2, 0.7]], columns=['Superficie_m2', 'Num_Habitaciones', 'Distancia_Metro_km'])
pred = model.predict(nuevo_precio)

print("Predicción para nuevo departamento:")
print(f"Precio estimado: {pred[0]:.1f} ≈ {round(pred[0])} UF")


