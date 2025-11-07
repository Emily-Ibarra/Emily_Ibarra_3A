
from database import crear_conexion

def ver_productos():
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        query = "SELECT id, nombre, descripcion, precio, stock FROM productos"
        cursor.execute(query)
        
        productos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return productos
    except Exception as e:
        print(f"Error al obtener productos: {e}")
    return []

def crear_producto(nombre, descripcion, precio, stock):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO productos (nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nombre, descripcion, precio, stock))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear producto: {e}")
        return False
    
def actualizar_producto(producto_id, nombre, descripcion, precio, stock):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = """
            UPDATE productos 
            SET nombre = %s, descripcion = %s, precio = %s, stock = %s 
            WHERE id = %s
        """
        cursor.execute(query, (nombre, descripcion, precio, stock, producto_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return False
    
def eliminar_producto(producto_id):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = %s"
        cursor.execute(query, (producto_id,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        return False