import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


#Trabajo 3 Red neuronal


#Para que no haya problemas al buscar el dataset
import os
os.chdir(os.path.dirname(__file__))

# 1. Cargar dataset
df = pd.read_excel("dataset_simce_matematicas_limpio.xlsx")

# 2. Seleccionar variables
X = df[["cod_grupo", "cod_depe1", "cod_rural_rbd", "agno"]]
y = df["rendimiento_alto"]

# 3. Normalizar X
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 4. dividir datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5. Construir la red neuronal usando keras desde tensorflow
model = keras.models.Sequential([
    keras.layers.Dense(8, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.Dense(4, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# 6. Compilar el modelo
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 7. Entrenar el modelo
hist = model.fit(
    X_train, y_train,
    epochs=10,
    validation_split=0.2,
    verbose=1
)

# 8. Evaluar en datos de prueba
loss, acc = model.evaluate(X_test, y_test)
print(f"\nAccuracy en test: {acc:.3f}")

# 9. Graficar métricas
plt.figure(figsize=(10,4))

    #Grafico de pérdida
plt.subplot(1,2,1)
plt.plot(hist.history['loss'], label='loss')
plt.plot(hist.history['val_loss'], label='val_loss')
plt.legend()
plt.title("Pérdida")

    #Grafico de precisión
plt.subplot(1,2,2)
plt.plot(hist.history['accuracy'], label='accuracy')
plt.plot(hist.history['val_accuracy'], label='val_accuracy')
plt.legend()
plt.title("Precisión")

plt.show()

# 10. Probar con un dato nuevo
nuevo = np.array([[2, 3, 0, 2023]]) 
nuevo = scaler.transform(nuevo)
pred = model.predict(nuevo)
print("\nProbabilidad de rendimiento alto:", round(float(pred),2))