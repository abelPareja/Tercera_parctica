


def agregar_producto():
    global productos
    nombre = input("ingrese el nombre: ")
    productos.append(nombre)
    print(nombre)
    
    
def eliminar_producto():
    global productos
    productos.remove(productos[0])
    print("Eliminado")
    
    
def listar():
    global usuarios
    print("lista de productos = ", productos)



productos = []
while True:
    print("Lista de compras")
    print("[1]..agregar producto..")
    print("[2]..eliminar producto..")
    print("[3]..listar productos..")
    print("[4]..salir..")
    

    try:
        opcion = int(input("\nSeleccione una opcion: "))
        
        if opcion ==1:
            agregar_producto()
        elif opcion == 2:
            eliminar_producto()
        elif opcion == 3:
            listar()
        elif opcion == 4:
            break

    except:
        print("por favor ingrese los valores correctos:  ")
