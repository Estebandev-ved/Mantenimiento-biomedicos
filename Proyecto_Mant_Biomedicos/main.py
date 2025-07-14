from src.login import login
from src.menu_admin import menu_admin
from src.menu_ingeniero import menu_ingeniero
from src.menu_tecnico import menu_tecnico

def main():
    usuario = login()  # Cambia 'rol' por 'usuario'
    if usuario["rol"] == "Administrador":
        menu_admin(usuario)
    elif usuario["rol"] == "Ingeniero":
        menu_ingeniero(usuario)
    elif usuario["rol"] == "Tecnico":
        menu_tecnico(usuario)
    else:
        print("Acceso denegado.")

if __name__ == "__main__":
    main()
#     print("1. Gestión de Usuarios")