from datos import estudiantes
from validar_info import validar_datos

if validar_datos(estudiantes):
    print("Todos los estudiantes tienen notas válidas.")
else:
    print("Hay errores en los datos de los estudiantes.")