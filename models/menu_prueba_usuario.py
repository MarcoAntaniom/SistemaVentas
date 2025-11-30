from usuarios import Usuario

def menu():
    while True:
        print("\n===== MENÚ DE USUARIOS =====")
        print("1. Agregar usuario")
        print("2. Consultar todos los usuarios")
        print("3. Buscar usuario por RUT")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- Agregar Usuario ---")
            u = Usuario()
            u.rut = input("RUT: ")
            u.nombre = input("Nombre: ")
            u.apellido_paterno = input("Apellido paterno: ")
            u.apellido_materno = input("Apellido materno: ")
            u.estado_id = int(input("Estado ID: "))
            u.contrasena = input("Contraseña: ")
            u.rol_id = int(input("Rol ID: "))

            u.agregar_usuario()
            print("Usuario agregado exitosamente.")

        elif opcion == "2":
            print("\n--- Lista de usuarios ---")
            u = Usuario()
            usuarios = u.consultar_usu()

            for fila in usuarios:
                print(fila)

        elif opcion == "3":
            print("\n--- Buscar Usuario por RUT ---")
            rut = input("Ingrese el RUT: ")

            u = Usuario()
            resultado = u.buscar_usuario_rut(rut)

            if resultado:
                print("Usuario encontrado:", resultado)
            else:
                print("No existe usuario con ese RUT.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")
