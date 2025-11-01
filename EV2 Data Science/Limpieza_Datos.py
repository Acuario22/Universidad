import pandas as pd

df_preeliminar = pd.read_excel("dataset_maestro_simce_matematicas_2018_2022_2023.xlsx") 

#print(df_preeliminar.info())


#Mostrar un resumen de valores nulos por columna
#(Nos permite identificar qué variables deben ser limpiados)
#print(df_preeliminar.isna().sum())

#Eliminar filas donde falte el puntaje promedio de matemáticas
#(no tiene sentido mantener filas sin el valor objetivo que vamos a predecir)
df_preeliminar.dropna(subset=['prom_mate2m_rbd'], inplace=True)

#Eliminar filas donde falte el grupo socioeconómico
#Para evitar sesgos, eliminamos estas filas ya que esta es una variable importante
df_preeliminar.dropna(subset=['cod_grupo'], inplace=True)

#Asegurarnos de que las columnas numéricas sean del tipo correcto
#(Esto ayuda a evitar problemas en análisis posteriores)
df_preeliminar = df_preeliminar.astype({
    "rbd": int,
    "cod_grupo": int,
    "cod_depe1": int,
    "cod_rural_rbd": int,
    "prom_mate2m_rbd": float
})

#Filtrar valores fuera del rango esperado del SIMCE (150–380 puntos)
#(Esto ayuda a eliminar outliers o errores de digitalización)
df_preeliminar = df_preeliminar[ 
    (df_preeliminar["prom_mate2m_rbd"] >=180) & (df_preeliminar["prom_mate2m_rbd"] <= 380) 
]


#Crear una nueva columna binaria para clasificación de rendimiento
#Esta variable se utilizará en los modelos de clasificación (Regresión Logística, KNN, Árboles, etc.)
#Si el puntaje promedio de matemáticas es igual o superior a 250 puntos → 1 (rendimiento alto)
#Si es menor a 250 → 0 (rendimiento bajo)
#El umbral de 250 se elige por ser cercano al promedio nacional reportado en Matemáticas II° Medio (~259 puntos)
df_preeliminar["rendimiento_alto"] = (df_preeliminar["prom_mate2m_rbd"] >= 250).astype(int)

#Mostrar un resumen después de la limpieza
print(df_preeliminar.isna().sum())
print()
print(df_preeliminar.info())
print()
print(df_preeliminar.head())

#Mostrar estadísticas descriptivas del puntaje de matemáticas después de la limpieza
print(df_preeliminar["prom_mate2m_rbd"].describe().round(2))

#Guardar el DataFrame limpio en un nuevo archivo Excel
df_preeliminar.to_excel("dataset_simce_matematicas_limpio.xlsx", index=False)