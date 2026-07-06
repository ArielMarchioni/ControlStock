elif opcion == "2":
    # mostrar productos disponibles
    for i in range(len(L_Productos)):
        print(L_Productos[i])

    nombre = input("Nombre del producto a modificar: ")

    if nombre in L_Productos:
        indice = L_Productos.index(nombre)

        cantidad = int(input("Cantidad a actualizar: "))
     
        L_Stock[indice] += cantidad

        print(f"Stock actualizado de {nombre}: {L_Stock[indice]}")
    else:
        print("ERROR: Producto no encontrado")
