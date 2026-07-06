elif opcion == "6":

    for i in range(len(L_Productos)):
        print(L_Productos[i])

    nombre = input("Nombre del producto a modificar precio: ")

    # buscar producto por nombre
    if nombre in L_Productos:
        indice = L_Productos.index(nombre)

        nuevo_precio = int(input("Ingrese el nuevo precio: "))

        # actualiza el precio en la lista correspondiente
        L_Precios[indice] = nuevo_precio

        print(f"Precio actualizado de {nombre}: ${L_Precios[indice]}")
    else:
        print("ERROR: Producto no encontrado")
