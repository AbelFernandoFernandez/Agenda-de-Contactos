def mostrar_menu():
    print("\n Agenda de contactos")
    print("1. Agregar un contacto")
    print("2. Eliminar un contacto")
    print("3. Buscar un contacto")
    print("4. lista de contactos")
    print("5. Salir")
    print("\n")


def agregar_contacto(agenda):
    nombre = input("Introduzca el nombre completo: ")
    telefono = input("Introduzca el telefono: ")
    email = input("Introduzca el  e-mail: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")


def eliminar_contacto(agenda):
    nombre = input("Introduzca el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"¡Se ha eliminado el contacto {nombre} exitosamente!")
    else:
        print(f"No se encuentra el contacto {nombre}")


def buscar_contacto(agenda):
    nombre = input("Introduzca el nombre del contacto que desea encontrar: ")
    if nombre in agenda:
        print(f"nombre: {nombre}")
        print(f"telefono:{agenda[nombre]['telefono']}")
        print(f"Email:{agenda[nombre]['email']}")
    else:
        print(f"No se encuentra el contacto {nombre}")


def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda está vacía")


def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Seleccione una opción válida (del 1 al 5)")


agenda_contactos()
