


def agregar_tarea():
    global tareas
    nombre = input("ingrese la tarea: ")
    """if len(tareas) == 0:
        tareas.append(nombre)
    else:
        tareas.insert(0, nombre)"""
        
    tareas.insert(0, nombre)
    print(nombre)
    print("tarea agregada")
    print(tareas)
    
    
def eliminar_tarea():
    global tareas
    tareas.remove(tareas[len(tareas)])
    print("Eliminado")
    
    
def mostrar_tareas():
    global tareas
    for i in reversed(tareas):
        tareas_inversa.append(i) 
        
    print("lista de tareas  = ", tareas_inversa)
    n = len(tareas_inversa)
    print("cantidad de tareas = ", n)
    tareas_inversa.clear()

tareas_inversa = []
tareas = []

while True:
    print("Lista de tareas pendientes")
    print("[1]..agregar tarea al inicio..")
    print("[2]..eliminar tarea..")
    print("[3]..mostrar tareas inversa..")
    print("[4]..salir..")
    
    
    try:
        opcion = int(input("\nSeleccione una opcion: "))
        
        if opcion ==1:
            agregar_tarea()
        elif opcion == 2:
            eliminar_tarea()
        elif opcion == 3:
            mostrar_tareas()
        elif opcion == 4:
            break

    except:
        print("por favor ingrese los valores correctos:  ")
