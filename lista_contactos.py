# lista de contactos
contactos = {"jorge" : 968142455,
             "luis": 915051650           
             }
# Usamos dos variables (nombre y telefono) con .items()
while True:
    print("===========MENU==========")
    print("1. Ver lista de contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")
    print("=========================")
    opcion = input("OPCION: ")

    if opcion == "1":
        print("LISTA DE CONTACTOS")
        for nombre, telefono in sorted(contactos.items()):
          print(f"{nombre:<10}0{telefono}")

     
    elif opcion == "2":
        print("AÑADE TU CONTACTO")
        while True:           
         nuevo_nombre = input("Introduce el nombre del contacto: ")
         if nuevo_nombre in contactos:
            print("ESTE CONTACTO YA EXISTE. Introduce un nombre diferente.")
            continue
         break
        while True:
         try:
            telefono = int(input("Introduce el teléfono: "))
            contactos[nuevo_nombre] = telefono
            print(f"Contacto {nuevo_nombre} guardado con éxito")
            break
         except ValueError:
            print("Ingresa un número valido")


    elif opcion == "3":  # <- Lógica para buscar
        print("BUSCAR CONTACTO")
        nombre_buscar = input("Introduce el nombre a buscar: ").lower()
        if nombre_buscar in contactos:
            print(f"Resultado: {nombre_buscar:<10}0{contactos[nombre_buscar]}")
        else:
            print("El contacto no existe en la agenda.")


    elif opcion == "4":  # <- Lógica para editar
        print("EDITAR CONTACTO")
        nombre_editar = input("Introduce el nombre del contacto a modificar: ").lower()
        if nombre_editar in contactos:
            while True:
                try:
                    nuevo_tel = int(input(f"Introduce el nuevo teléfono para {nombre_editar}: "))
                    contactos[nombre_editar] = nuevo_tel
                    print("Contacto actualizado correctamente.")
                    break
                except ValueError:
                    print("Ingresa un número válido")
        else:
            print("El contacto no existe")


    elif opcion == "5":
        print("ELIMINAR CONTACTO")
        try:
           nombre = input("Introduce el nombre del contacto: ")
           contactos.pop(nombre)
           print("Contacto eliminado")
        except KeyError:
           print("ESTE CONTACTO NO EXISTE")
           

    elif opcion == "6":
        print("saliste")
        break

    else:
       print("Opcion no valida")