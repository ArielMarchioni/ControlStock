elif opcion == "5":
    # mostrar productos disponibles
    for i in range(len(L_Productos)):
        print(L_Productos[i])

    nombre = input("Nombre del producto a eliminar: ")

    if nombre in L_Productos:
        indice = L_Productos.index(nombre)

        # eliminar en las 3 listas 
        L_Productos.pop(indice)
        L_Precios.pop(indice)
        L_Stock.pop(indice)

        print(f"Producto '{nombre}' eliminado correctamente")
    else:
        print("ERROR: Producto no encontrado")
