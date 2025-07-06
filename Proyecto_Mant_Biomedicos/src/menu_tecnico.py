from src.mantenimientos import crear_mantenimiento, listar_mantenimientos
from src.conexion_mysql import conectar_mysql

def menu_tecnico(tecnico_id):
    while True:
        print("""
        --- Menú Técnico ---
        1. Registrar mantenimiento preventivo/correctivo
        2. Listar mis mantenimientos
        3. Salir
        """)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            crear_mantenimiento()
        elif opcion == "2":
            listar_mantenimientos_por_tecnico(tecnico_id)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

def listar_mantenimientos_por_tecnico(tecnico_id):
    conn = conectar_mysql()
    cursor = conn.cursor()
    cursor.execute("""SELECT mmto_id, equipo_id, tipo_mmto, fecha_mmto, duracion_mmto, observaciones 
                      FROM mantenimientos WHERE tecnico_id=%s""", (tecnico_id,))
    mantenimientos = cursor.fetchall()
    print("\nMis mantenimientos:")
    for mant in mantenimientos:
        print(mant)
    cursor.close()
    conn.close()
