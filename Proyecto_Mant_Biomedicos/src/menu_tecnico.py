from src.mantenimientos import crear_mantenimiento, listar_mantenimientos
from src.equipos import ver_equipos_asignados

def menu_tecnico(usuario):
    print("=== Menú Técnico ===")
    usuario = input("Ingresa tu nombre de usuario: ")

    while True:
        print("\n--- Opciones ---")
        print("1. Ver equipos asignados")
        print("2. Registrar mantenimiento")
        print("3. Ver mantenimientos realizados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_equipos_asignados(usuario)
        elif opcion == "2":
            crear_mantenimiento(usuario)
        elif opcion == "3":
           listar_mantenimientos(usuario)
        elif opcion == "4":
            print("👋 Cerrando sesión del técnico...")
            break
        else:
            print("❌ Opción inválida.")
