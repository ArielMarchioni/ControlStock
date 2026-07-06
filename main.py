condicion = True
Producto=[]
Precio=[]
Cantidad=[]
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
        Producto.append(input("Nombre del producto: "))
        Precio.append(int(input("Precio: ")))
        Cantidad.append(int(input("Cantidad: ")))
        print("Productos: ",Producto)
        print("Precioas: ",Precio)
        print("Cantidad: ",Cantidad)
        
    elif opcion =="2":
        for i in range(len(Producto)):
            print(i,Producto[i])
        modifica=int(input("Indice a modificar: "))
        print(f"modifica el indice {modifica}")
        CantidadActualizada= int(input("cantidad a actualizar"))
        Cantidad[modifica]=Cantidad[modifica] + CantidadActualizada
        print(f"la cantidad de {Producto[i]} ahora es : {Cantidad[modifica]}")
  
    elif opcion =="3":
        if Producto == []:
            print("NO HAY PRODUCTOS REGISTRADOS")
    else: 
        print("Error")
print("PROGRAMA FINALIZADO")        
