import json
import os
import mysql.connector
from src.conexion_mysql import conectar_mysql

def cargar_usuarios_json():
    ruta = os.path.join(os.path.dirname(__file__), "../base_datos/mysql/ejemplo_usuarios.json")
    with open(ruta, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    return usuarios

def cargar_usuarios_mysql():
    conexion = conectar_mysql()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT nombre_usuario, password, rol FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios

def login():
    print("=== Login ===")
    user = input("Usuario: ")
    pwd = input("Contraseña: ")

    # Primero intenta con MySQL
    usuarios_mysql = cargar_usuarios_mysql()
    for u in usuarios_mysql:
        if u["nombre_usuario"] == user and u["password"] == pwd:
            print(f"\n✅ Bienvenido, {user}. Rol: {u['rol']}")
            return {"nombre": user, "rol": u["rol"]}

    # Si no está en MySQL, intenta con el archivo JSON
    usuarios_json = cargar_usuarios_json()
    for u in usuarios_json:
        if u["nombre_usuario"] == user and u["password"] == pwd:
            print(f"\n✅ Bienvenido, {user}. Rol: {u['rol']} (Desde JSON)")
            return {"nombre": user, "rol": u["rol"]}

    print("❌ Usuario o contraseña incorrectos.")
    return None
