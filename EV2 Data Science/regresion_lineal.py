import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#carga el dataset limpio
df = pd.read_excel("dataset_simce_matematicas_limpio.xlsx")

#revisa que no existan datos faltantes
print("Valores nulos por columna:\n", df.isnull().sum())

#selecciona variables
#variable dependiente (Y): promedio SIMCE de matematicas
y = df["prom_mate2m_rbd"]

#variables independientes (X): año, dependencia, ruralidad
X = df[["año", "cod_depe1", "cod_rural_rbd"]]

#dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#crea y entrena el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

#realiza las predicciones
y_pred = modelo.predict(X_test)

#evaluacion del modelo
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\n RESULTADOS DEL MODELO DE REGRESION LINEAL")
print("------------------------------------------------")
print(f"R²: {r2:.3f}")
print(f"RMSE: {rmse:.2f}")
print(f"Coeficientes: {modelo.coef_}")
print(f"Interseccion: {modelo.intercept_}")

#visualizacionn (usando la variable año)
plt.figure(figsize=(8,5))
plt.scatter(X_test["año"], y_test, color='blue', label='Valores reales')
plt.plot(X_test["año"], y_pred, color='red', linewidth=2, label='Predicción modelo')
plt.xlabel("Año")
plt.ylabel("Promedio SIMCE Matematicas")
plt.title("Regresión Lineal: Promedio SIMCE vs Año")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("El modelo intenta estimar el puntaje SIMCE a partir del año, tipo de dependencia y ruralidad.")
print("Un R² cercano a 1 indica buen ajuste. Si el valor es bajo, se recomienda incluir mas variables.")
