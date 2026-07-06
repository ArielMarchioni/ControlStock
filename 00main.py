condicion = True
L_Productos=[]
L_Precios=[]
L_Stock=[]
print("""_______________________________________\n/bienvenido Esclavo al Control de stock/\n----------------------------------------""")
while condicion:
    print("""         ===menu==
        1. Agregar producto
        2. Actualizar stock
        3. ver inventario
        4. salir""")
    opcion=(input("Ingrese una opcion: "))
    if opcion=="4":
        condicion=False
    elif opcion=="1":
        print("puso 1")
        L_Productos.append(input("Nombre del producto: "))
        L_Precios.append(int(input("Precio: ")))
        L_Stock.append(int(input("Cantidad: ")))
        print("Productos: ",L_Productos)
        print("Precioas: ",L_Precios)
        print("Cantidad: ",L_Stock)
        
    elif opcion =="2":
        for i in range(len(L_Productos)):
            print(i,L_Productos[i])
        modifica=int(input("Indice a modificar: "))
        print(f"modifica el indice: {modifica}")
        if (modifica <0 or modifica >=len(L_Productos) ):
            print("""
                  !!!ERROR!!!
            Producto no encontrado""")
        else:
            
            CantidadActualizada= int(input("cantidad a actualizar: "))
            L_Stock[modifica]=L_Stock[modifica] + CantidadActualizada
            print(f"la cantidad de {L_Productos[modifica]} ahora es: {L_Stock[modifica]}")
  
    elif opcion =="3":
        if L_Productos == []:
            print("NO HAY PRODUCTOS REGISTRADOS")
            
        else: 
            for i in range(len(L_Productos)):
                print(f"""
                Producto N°: {i+1}
                Nombre:{L_Productos[i]}
                Precio: ${L_Precios[i]}
                Stock: {L_Stock[i]} Unidades
                -----------------------------""")
    else:
        print("""
                !!!ERROR!!!  
        INGRESE UNA OPCION CORRECTA""")
print("PROGRAMA FINALIZADO")        


