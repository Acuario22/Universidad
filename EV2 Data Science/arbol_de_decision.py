import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

#Para que no haya problemas al buscar el dataset
import os
os.chdir(os.path.dirname(__file__))

#1. Cargamos el dataset limpio
df_simce_mat = pd.read_excel("dataset_simce_matematicas_limpio.xlsx")
#print(df_simce_mat.head())

#Objetivo
#Predecir si una institucion tiene un rendimiento alto en matemáticas (rendimiento_alto)

#2. Definir los features (X) y el target (y)
x= df_simce_mat[ ["cod_grupo", "cod_depe1", "cod_rural_rbd"] ]
y= df_simce_mat["rendimiento_alto"]

#3. Dividir los datos en conjuntos de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) # 20% para probarlo y 80% para entrenar el modelo

#4. crear el modelo de árbol de decisión
arbol_decision = DecisionTreeClassifier(max_depth=2, random_state=42) #max depth = cuantas veces el arbol puede dividir los datos para tomar decisiones
# maximo dos niveles de decisiones antes de llegar a una conclusión (rendimiento alto o bajo)

#Entrenar el modelo
arbol_decision.fit(x_train, y_train) #el modelo aprende a clasificar colegios segun las variables dadas

#5. Visualizar el árbol de decisión
plt.figure(figsize=(12,8))

plot_tree(
    arbol_decision, 
    feature_names= ["cod_grupo", "cod_depe1", "cod_rural_rbd"], 
    class_names= ['Rendimiento Bajo', 'Rendimiento Alto'],
    filled=True, 
    rounded=True,
    fontsize=10
)

plt.title("Árbol de Decisión para Predecir Rendimiento Alto en Matemáticas")
plt.show()

#6. Evaluar el modelo
y_pred = arbol_decision.predict(x_test) #genera las predicciones del modelo
precision_modelo = accuracy_score(y_test, y_pred) #calcula el porcentaje de aciertos
print("Precisión del modelo de Árbol de Decisión:", round(precision_modelo*100,2), "%")
