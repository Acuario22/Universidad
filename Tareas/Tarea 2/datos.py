import pandas as pd
from validar_info import validar_datos

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.9, 6.2, 5.5]},
    {"nombre": "María", "notas": [7.0, 6.8, 6.9]},
    {"nombre": "Pedro", "notas": [5.0, 4.8, 5.2]},
    {"nombre": "Carla", "notas": [6.9, 7.0, 7.0]},
    {"nombre": "Javier", "notas": [5.5, 6.0, 6.3]},
    {"nombre": "Sofía", "notas": [6.8, 6.9, 7.0]},
    {"nombre": "Andrés", "notas": [5.1, 5.5, 6.0]},
    {"nombre": "Camila", "notas": [6.0, 6.5, 6.2]},
    {"nombre": "Rodrigo", "notas": [4.8, 5.0, 5.3]},
    {"nombre": "Valentina", "notas": [6.7, 6.9, 7.0]},
    {"nombre": "Diego", "notas": [5.9, 6.0, 6.1]},
    {"nombre": "Isabel", "notas": [6.2, 6.5, 6.8]},
    {"nombre": "Tomás", "notas": [5.3, 5.7, 5.9]},
    {"nombre": "Fernanda", "notas": [6.8, 7.0, 6.9]},
    {"nombre": "Matías", "notas": [5.6, 5.9, 6.2]},
    {"nombre": "Paula", "notas": [6.3, 6.6, 6.9]},
    {"nombre": "Felipe", "notas": [5.0, 5.5, 5.8]},
    {"nombre": "Constanza", "notas": [6.7, 7.0, 6.8]},
    {"nombre": "Ignacio", "notas": [5.2, 3.0, 5.9]},
    {"nombre": "Josefina", "notas": [6.0, 6.3, 6.5]},
    {"nombre": "Cristóbal", "notas": [5.8, 6.0, 6.4]},
    {"nombre": "Gabriela", "notas": [6.9, 6.8, 7.0]},
    {"nombre": "Nicolás", "notas": [5.5, 5.8, 6.0]},
    {"nombre": "Daniela", "notas": [6.4, 6.6, 6.7]},
    {"nombre": "Sebastián", "notas": [5.7, 6.0, 6.3]},
    {"nombre": "Catalina", "notas": [6.8, 7.0, 6.9]},
    {"nombre": "Mauricio", "notas": [5.4, 5.6, 5.9]},
    {"nombre": "Alejandra", "notas": [6.2, 6.4, 6.8]},
    {"nombre": "Ricardo", "notas": [5.1, 2.0, 5.6]}
]

df_estudiantes = pd.DataFrame(estudiantes)          #Crea un DataFrame desde una lista de diccionarios