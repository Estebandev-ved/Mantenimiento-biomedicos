from src.usuarios import crear_usuario, listar_usuarios, modificar_usuario, eliminar_usuario
from src.tecnicos import crear_tecnico, listar_tecnicos, modificar_tecnico, eliminar_tecnico
from src.equipos import crear_equipo, listar_equipos, modificar_equipo, eliminar_equipo
from src.mantenimientos import crear_mantenimiento, listar_mantenimientos, modificar_mantenimiento, eliminar_mantenimiento
from src.reportes_mongo import crear_reporte_tecnico, listar_reportes, buscar_reportes_por_equipo, eliminar_reporte
from src.busqueda import menu_busqueda

def menu_usuarios():
    while True:
        print("""
        --- CRUD Usuarios ---
        1. Crear usuario
        2. Listar usuarios
        3. Modificar usuario
        4. Eliminar usuario
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_usuario()
        elif opcion == "2":
            listar_usuarios()
        elif opcion == "3":
            modificar_usuario()
        elif opcion == "4":
            eliminar_usuario()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_tecnicos():
    while True:
        print("""
        --- CRUD Técnicos ---
        1. Crear técnico
        2. Listar técnicos
        3. Modificar técnico
        4. Eliminar técnico
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_tecnico()
        elif opcion == "2":
            listar_tecnicos()
        elif opcion == "3":
            modificar_tecnico()
        elif opcion == "4":
            eliminar_tecnico()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_equipos():
    while True:
        print("""
        --- CRUD Equipos ---
        1. Crear equipo
        2. Listar equipos
        3. Modificar equipo
        4. Eliminar equipo
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_equipo()
        elif opcion == "2":
            listar_equipos()
        elif opcion == "3":
            modificar_equipo()
        elif opcion == "4":
            eliminar_equipo()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_mantenimientos():
    while True:
        print("""
        --- CRUD Mantenimientos ---
        1. Crear mantenimiento
        2. Listar mantenimientos
        3. Modificar mantenimiento
        4. Eliminar mantenimiento
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_mantenimiento()
        elif opcion == "2":
            listar_mantenimientos()
        elif opcion == "3":
            modificar_mantenimiento()
        elif opcion == "4":
            eliminar_mantenimiento()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_reportes_tecnicos():
    while True:
        print("""
        --- Gestión de Reportes Técnicos (MongoDB) ---
        1. Crear reporte técnico
        2. Listar todos los reportes
        3. Buscar reportes por equipo
        4. Eliminar reporte técnico
        5. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_reporte_tecnico()
        elif opcion == "2":
            listar_reportes()
        elif opcion == "3":
            buscar_reportes_por_equipo()
        elif opcion == "4":
            eliminar_reporte()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def menu_admin():
    while True:
        print("""
        === Menú Administrador ===
        1. CRUD Usuarios
        2. CRUD Técnicos
        3. CRUD Equipos
        4. CRUD Mantenimientos
        5. Gestión de reportes técnicos (MongoDB)
        6. Salir al menú principal
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            menu_usuarios()
        elif opcion == "2":
            menu_tecnicos()
        elif opcion == "3":
            menu_equipos()
        elif opcion == "4":
            menu_mantenimientos()
        elif opcion == "5":
            menu_reportes_tecnicos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
