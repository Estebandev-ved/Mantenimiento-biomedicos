from pymongo import MongoClient

def conectar_mongo():
    """
    Establece conexión con MongoDB local y retorna la base de datos PF_Informatica1.
    """
    try:
        cliente = MongoClient("mongodb://localhost:27017/")
        db = cliente["PF_Informatica1"]
        print("Conexión a MongoDB exitosa")
        return db
    except Exception as e:
        print(f"Error de conexión a MongoDB: {e}")
        return None

# Prueba de conexión (solo si ejecutas este archivo directamente)
if __name__ == "__main__":
    db = conectar_mongo()
