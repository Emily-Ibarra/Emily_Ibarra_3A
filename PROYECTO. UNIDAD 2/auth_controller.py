#controlador encargado de la logica de la autenticcion.
# Nos sirve para separar la  logica del login para tener limpio del codigo en la vista.
from database import crear_conexion

def validar_credenciales(usuario, password):
    conexion = crear_conexion()
    if not conexion:
        return False

    cursor = None
    try:
        cursor = conexion.cursor()
        consulta = "SELECT id FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(consulta, (usuario, password))
        resultado = cursor.fetchone()
        return resultado is not None
    except Exception as e:
        print(f"Error en validar_credenciales: {e}")
        return False
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass
        try:
            conexion.close()
        except Exception:
            pass