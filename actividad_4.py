from statistics import multimode

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

aprobados = 0
lista_promedios = []
todas_las_notas = []
bajo_4 = 0
bajo_4_porcentaje = 0

for estudiante in estudiantes:
    notas = estudiante["notas"]
    promedio = sum(notas)/len(notas)
    ##
    lista_promedios.append({"nombre":estudiante["nombre"], "promedio": promedio})
    print(estudiante["nombre"], "promedio:", round(promedio,2))

    ##
    if all(nota >= 4.0 for nota in notas):      
        aprobados = aprobados + 1
    """
    else:                                       
        bajo_4 = bajo_4 + 1
    """
    
    ##
    todas_las_notas.extend(estudiante["notas"])

    ##
    if any(nota <4.0 for nota in notas):
        bajo_4 = bajo_4 + 1

##
prom_alto = max(lista_promedios, key=lambda x:x["promedio"] )
prom_bajo = min(lista_promedios, key=lambda x:x["promedio"] )

##
moda = multimode(todas_las_notas)

bajo_4_porcentaje = bajo_4/len(estudiantes)*100

##
lista_ordenada = sorted(lista_promedios, key=lambda x: x ["promedio"], reverse=True)

print ("PUNTO 1")
print(f"Alumno/a con el promedio más alto:", prom_alto["nombre"], "con promedio:", round(prom_alto["promedio"],2))
print(f"Alumno/a con el promedio más bajo:", prom_bajo["nombre"], "con promedio:", round(prom_bajo["promedio"],2))

print ("PUNTO 2")
print("Cantidad de alumnos que aprobaron todas sus asignaturas:" , aprobados)

print ("PUNTO 3")
print("La nota mas frecuente fue de:", moda)

print ("PUNTO 4")
print(f"El porcentaje de estudiantes con al menos una nota bajo 4.0 es de:", round(bajo_4_porcentaje,2),"%")

print ("PUNTO 5")
for estudiante in lista_ordenada:
    print(estudiante["nombre"], round(estudiante["promedio"],2))

