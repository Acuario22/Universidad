import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os
os.chdir(os.path.dirname(__file__))

#carga el dataset limpio
df = pd.read_excel("dataset_simce_matematicas_limpio.xlsx")

#revisa que no existan datos faltantes
print("Valores nulos por columna:\n", df.isnull().sum())

#selecciona variables
y = df["prom_mate2m_rbd"] # variable dependiente (lo que queremos predecir)
X = df[["agno", "cod_depe1", "cod_rural_rbd", "cod_grupo"]] #variables independientes (factores que podrían influir): año, dependencia, ruralidad, grup socioeconomico

#dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
) # 80% entrenar modelo y 20% probarlo

#crea y entrena el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train) #aprende la relacion entre variables

#realiza las predicciones y evaluaciones
y_pred = modelo.predict(X_test) #puntajes q el modelo predice

r2 = r2_score(y_test, y_pred) #mide si se ajusta el modelo (entre 0 y 1)
rmse = np.sqrt(mean_squared_error(y_test, y_pred)) #error promedio entre lo real y lo predicho

print("\n RESULTADOS DEL MODELO DE REGRESION LINEAL")
print("------------------------------------------------")
print(f"R²: {r2:.3f}")
print(f"RMSE: {rmse:.2f}")
print(f"Coeficientes: {modelo.coef_}") #indican cuánto influye cada variable
print(f"Interseccion: {modelo.intercept_}") #el punto de inicio del modelo (cuando las otras variables valen 0)

# Calcular el promedio del puntaje por año
df_promedios = df.groupby("agno")["prom_mate2m_rbd"].mean().reset_index()

# Gráfico de tendencia anual
plt.figure(figsize=(8,5))
plt.plot(df_promedios["agno"], df_promedios["prom_mate2m_rbd"],
         marker='o', color='red', linewidth=2, label='Promedio por año')

plt.scatter(df["agno"], df["prom_mate2m_rbd"], color='blue', alpha=0.3, label='Datos reales')
plt.xlabel("Año")
plt.ylabel("Promedio SIMCE Matemáticas")
plt.title("Tendencia del Promedio SIMCE de Matemáticas (Regresión Lineal)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\nEl modelo intenta estimar el puntaje SIMCE a partir del año, tipo de dependencia y ruralidad.")
print("Un R² cercano a 1 indica buen ajuste. Si el valor es bajo, se recomienda incluir mas variables.\n")
