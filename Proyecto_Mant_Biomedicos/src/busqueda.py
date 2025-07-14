from src.conexion_mysql import conectar_mysql
from src.conexion_mongo import conectar_mongo

def buscar_equipo_por_id(equipo_id):
    # Buscar equipo en MySQL
    conexion = conectar_mysql()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipos WHERE id = %s", (equipo_id,))
    equipo = cursor.fetchone()
    cursor.close()
    conexion.close()

    if not equipo:
        print("❌ Equipo no encontrado en MySQL.")
        return

    print(f"\n✅ Equipo encontrado: {equipo}")

    # Buscar historial y reportes en MongoDB
    db = conectar_mongo()
    historial = db.historial.find({"equipo_id": equipo_id})
    reportes = db.reportes.find({"equipo_id": equipo_id})

    print("\n--- Historial ---")
    for h in historial:
        print(h)

    print("\n--- Reportes ---")
    for r in reportes:
        print(r)

def menu_busqueda():
    while True:
        print("""
        --- Submenú de Búsqueda ---
        1. Buscar equipo por ID (con historial y reportes)
        2. Volver
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            equipo_id = input("Ingrese el ID del equipo: ")
            buscar_equipo_por_id(equipo_id)
        elif opcion == "2":
            break
        else:
            print("Opción inválida.")
