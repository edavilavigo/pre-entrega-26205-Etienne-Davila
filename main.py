# mostrar menu
productos = list() #[] # [[],[],[]]

while True:
    print("\n")
    print("+"*40) # <-  ==================================
    print("Sistema de gestion de productos") 
    print("+"*40) # <-  ==================================
    
    print("1. Agregar productos")
    print("2. Mostrar productos")        
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("elija una opcion: ").strip()


    if opcion == "1":
        nombre = input("ingrese el nombre del producto: ").strip().lower()
        while nombre == "":
            print("Nombre vacio. volver a ingresar")
            nombre = input("ingrese el nombre del producto: ").strip()

        categoria = input("ingrese la categoria: ").strip()
        while categoria == "":
            print("Nombre vacio. volver a ingresar")
            categoria = input("ingrese la categoria: ").strip()

        precio_str = input("ingrese el precio: $ ").strip()
        while not precio_str.isdigit():
            print("ingrese valor numerico positivo")
            precio_str = input("ingrese el precio: $ ").strip()
        precio = int(precio_str)
        # productos_total = [nombre, categoria, precio]
        # productos.append(productos_total)
        productos.append([nombre, categoria, precio])

    elif opcion == "2":
        print("\n----Productos----")
        if len(productos)==0:
            print("No se puede mostrar, no hay productos cargados")
        else:
            for i in range(len(productos)):
                print(f"ID={i+1}")
                print(f"Nombre: {productos[i][0]} ")
                print(f"Categoria: {productos[i][1]} ")
                print(f"Precio: {productos[i][2]}\n ")
         #input("\nPresione ENTER para volver al menú...")

    elif opcion == "3":
        print("----BUSCAR PRODUCTO----")
        if len(productos) ==0:
            print("busqueda sin resultados, No hay productos cargados")
        else:
            buscar = input("ingrese el producto a buscar: ").strip().lower()
            while buscar == "":
                print("Nombre vacio. volver a ingresar")
                buscar = input("ingrese el nombre del producto: ").strip().lower()
            encontrados=0
            for i in range(len(productos)):
                # if productos[i][0]==buscar: #busca solo el nombre exacto
                if buscar in productos [i][0]:   # busca cualquier que contenga "buscar"
                    print(f"ID={i+1}")
                    print(f"Nombre: {productos[i][0]} ")
                    print(f"Categoria: {productos[i][1]} ")
                    print(f"Precio: {productos[i][2]}\n ")
                    encontrados +=1
            if encontrados == 0:
                print("no se encontraron productos")
            else:
                print(f"Productos encontrados: {encontrados}")
        
    elif opcion == "4":
        print("----ELIMINAR PRODUCTO----")
        if len(productos) ==0:
            print("No se puede Eliminar, No hay productos cargados")
        else:
            id_str = input("ingrese el ID del producto a Eliminar: ").strip()
            while not id_str.isdigit():
                print("El valor ingresado no es correcto")
                id_str = input("ingrese un numero de ID valido: ").strip()
            eliminados=0
            id_int=int(id_str)
            indice = id_int-1
            if 0 <= indice < len(productos):
                borrado=productos.pop(indice)
                eliminados +=1
                print(f"Producto eliminado: {borrado[0]}")
            else:
                print("ID inválido")

            if eliminados == 0:
                print("no se elimimaron productos")
            else:
                print(f"Productos eliminados: {eliminados}")                   


    
        
    elif opcion == "5":
        print("saliste del programa")
        break

    else:
            print("Opcion no valida. tenes que elegir entre (1-5)")

        



            
  



