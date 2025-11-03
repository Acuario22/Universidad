import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_recall_fscore_support
import matplotlib.pyplot as plt #graficos y visualizacion
import seaborn as sns

#Para que no haya problemas al buscar el dataset
import os
os.chdir(os.path.dirname(__file__))

#1. Cargamos nuestro dataset limpio
df_simce_mat = pd.read_excel("dataset_simce_matematicas_limpio.xlsx")

#2. Definimos X e y (siendo (y) lo que queremos predecir) (x lo que influye en el rendimiento)
X = df_simce_mat[["cod_grupo", "cod_depe1", "cod_rural_rbd"]]
y= df_simce_mat["rendimiento_alto"]

#3. Dividimos datos entre entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # 30% para probarlo y 70% entrenar modelo

#4. Creamos y entrenamos nuestro modelo de regresión logística
modelo = LogisticRegression(max_iter=1000, random_state=42) #max iter =asegura que el modelo tenga suficientes iteraciones
modelo.fit(X_train, y_train)
# aprende a clasificar si un colegio tiene rendimiento alto o bajo segun las variables

#5. Evaluamos nuestro modelo
y_pred = modelo.predict(X_test) #el modelo usa los datos de prueba para predecir la clase (alto o bajo rendimiento)

#6. Métricas
precision = accuracy_score(y_test, y_pred) #que porcentaje de predicciones fueron correctas
cm = confusion_matrix(y_test, y_pred) #muestra cuantos casos el modelo clasificó bien y cuantos se equivoco
reporte = classification_report(y_test, y_pred, output_dict=True) #resume las tres metricas (precision, recall y F1 score)

#6. Preparamos métricas para mostrarlas (tabla)
metrics_df = pd.DataFrame({
    'Clase': ['Bajo (0)', 'Alto (1)'],
    'Precision': [reporte['0']['precision'], reporte['1']['precision']], #qué tan exactas son las predicciones positivas
    'Recall': [reporte['0']['recall'], reporte['1']['recall']], #cuántos casos positivos reales detecta
    'F1-Score': [reporte['0']['f1-score'], reporte['1']['f1-score']] #equilibrio entre precisión y recall
})

#7. Se muestra el gráfico
plt.figure(figsize=(14,7))
#Precisión general
plt.subplot(1,3,1)
plt.text(0.5, 0.5, f"Precisión total:\n{precision*100:.2f}%", 
         fontsize=24, ha='center', va='center', color='green') #muestra el porcentaje total de acierto del modelo
plt.axis('off')
plt.title("Precisión del modelo de Clasificación")
#Matriz de confusión
plt.subplot(1,3,2)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False) #Visualiza cuántas veces el modelo acertó y cuantas falló
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.title("Matriz de Confusión")
#Precision, Recall, F1-Score por clase
plt.subplot(1,3,3)
metrics_df.set_index('Clase').plot(kind='bar', ax=plt.gca()) #muestra gráfico de barras comparando las tres métricas para cada clase (rendimiento bajo y alto)
plt.title("Precision / Recall / F1-score por clase")
plt.ylabel("Valor")
plt.ylim(0,1)
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()
