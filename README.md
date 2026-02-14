# 🏥 Sistema de Gestión de Mantenimiento de Equipos Biomédicos

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)](https://www.mysql.com/)
[![MongoDB](https://img.shields.io/badge/Database-MongoDB-green.svg)](https://www.mongodb.com/)
[![UdeA](https://img.shields.io/badge/Académico-UdeA-darkgreen.svg)](https://www.udea.edu.co/)

Este proyecto consiste en un sistema integral para la gestión y seguimiento del mantenimiento de equipos biomédicos. Desarrollado como proyecto final para la asignatura de Informática 1 en la **Universidad de Antioquia (UdeA)**, el sistema permite administrar usuarios, equipos, mantenimientos, técnicos y generar reportes detallados.

## 🚀 Características Principales

El sistema implementa un control de acceso basado en roles (RBAC):

- **👤 Administrador**: Gestión total de usuarios (CRUD) y supervisión del sistema.
- **⚙️ Ingeniero**: Registro y gestión de equipos biomédicos, asignación de mantenimientos y gestión de técnicos.
- **🛠️ Técnico**: Visualización de mantenimientos asignados y registro de actividades.

### Funcionalidades destacadas:
- **Gestión Híbrida de Datos**: Utiliza MySQL para datos estructurados (usuarios, equipos) y MongoDB para datos no estructurados y logs (bitácoras, reportes, manuales).
- **Sistema de Login Seguro**: Autenticación de usuarios con validación de roles.
- **Reportes Dinámicos**: Generación de reportes de mantenimiento almacenados en colecciones de MongoDB.

## 🛠️ Stack Tecnológico

- **Lenguaje**: Python 3.x
- **Bases de Datos**:
  - **MySQL**: Gestión de entidades relacionales.
  - **MongoDB**: Almacenamiento de documentos, bitácoras y manuales.
- **Librerías principales**:
  - `mysql-connector-python`: Conexión con MySQL.
  - `pymongo`: Interacción con MongoDB.

## 📋 Requisitos Previos

- Python 3.8 o superior instalado.
- Servidor MySQL (XAMPP, WAMP o instalación independiente).
- Instancia de MongoDB (Local o Atlas).

## 🔧 Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/Mantenimiento-biomedicos.git
   cd Mantenimiento-biomedicos/Proyecto_Mant_Biomedicos
   ```

2. **Instalar dependencias**:
   ```bash
   pip install mysql-connector-python pymongo
   ```

3. **Configurar Bases de Datos**:
   - **MySQL**:
     - Importar los scripts ubicados en `base_datos/mysql/`:
       1. Ejecutar `crear_tablas.sql`.
       2. Ejecutar `insertar_datos.sql`. (Asegúrate de configurar la base de datos `PF_Informatica1`).
   - **MongoDB**:
     - El sistema creará automáticamente la base de datos `PF_Informatica1` al iniciar.
     - Puedes ejecutar los scripts en `base_datos/mongo/` para precargar datos:
       ```bash
       python base_datos/mongo/insertar_manuales.py
       python base_datos/mongo/insertar_bitacoras.py
       ```

4. **Configurar Conexión**:
   - Revisa `src/conexion_mysql.py` y `src/conexion_mongo.py` para ajustar las credenciales (user, password, host) si es necesario.

## 🖥️ Uso

Para iniciar la aplicación, ejecuta el archivo principal:

```bash
python main.py
```

### Credenciales de Prueba (Ejemplo):
- **Admin**: Ver en `base_datos/mysql/insertar_datos.sql` o el archivo `ejemplo_usuarios.json`.

---

## 🎓 Contexto Académico
Este proyecto fue realizado como entrega final para el curso de **Informática 1** de la **Universidad de Antioquia**. 

**Desarrollado por:**
- Estebandev y mauricio

---
*Nota: Este sistema es una versión académica y está diseñado con fines educativos.*
