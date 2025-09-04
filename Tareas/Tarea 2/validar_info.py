def validar_datos(estudiantes):
    """
    Valida la lista de estudiantes.
    
    Revisa:
    Que cada estudiante tenga al menos una nota.
    Que todas las notas sean números (int o float).
    Que todos los estudiantes tengan la misma cantidad de notas.
    
    Retornara True si todos los datos son correctos, de lo contrario False.
    """
    
    todos_correctos = True  #Se asume que no existen errores
    
    # Determinar la cantidad de notas esperadas según el primer estudiante
    if estudiantes:
        cantidad_esperada = len(estudiantes[0].get("notas", []))
    else:
        cantidad_esperada = 0
    
    for estudiante in estudiantes:
        nombre = estudiante.get("nombre")
        notas = estudiante.get("notas")
        
        # Revisar si la lista de notas está vacía
        if not notas:
            print(f"El estudiante '{nombre}' no tiene notas.")
            todos_correctos = False
        
        # Revisar si todas las notas son números
        elif not all(isinstance(n, (int, float)) for n in notas):
            print(f"El estudiante '{nombre}' tiene notas que no son números.")
            todos_correctos = False
        
        # Revisar si la cantidad de notas coincide con la esperada
        elif len(notas) != cantidad_esperada:
            print(f"El estudiante '{nombre}' tiene {len(notas)} notas, se espera que sean {cantidad_esperada}.")
            todos_correctos = False
    
    return todos_correctos