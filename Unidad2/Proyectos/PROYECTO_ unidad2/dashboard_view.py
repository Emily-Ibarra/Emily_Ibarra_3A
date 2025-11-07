
import tkinter as tk
from tkinter import messagebox, ttk
from user_controller import ver_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario
from product_controller import ver_productos, crear_producto, actualizar_producto, eliminar_producto

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Panel de Control - Usuario: {username}")
        self.root.geometry("900x650")   
        self.root.resizable(True, True)
        
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 9))
        self.style.configure("Header.TLabel", font=("Arial", 16, "bold"))
        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        
        self.crear_elementos()
        
        self.actualizar_lista_usuarios()
        self.actualizar_lista_productos()
        
        self.root.mainloop()
        
    def crear_elementos(self):
        main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        main_frame.pack(fill="both", expand=True)
        
        ttk.Label(main_frame, text=f"Sistema de Gestión. ¡Hola, {self.username}!", 
                  style="Header.TLabel").pack(pady=10)
        
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill="both", expand=True, pady=10)
        
        self.frame_usuarios = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.frame_usuarios, text='Gestión de Usuarios')
        self.crear_widgets_usuarios(self.frame_usuarios)
        
        self.frame_productos = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.frame_productos, text='Gestión de Productos')
        self.crear_widgets_productos(self.frame_productos)

        ttk.Button(main_frame, text="Cerrar Sesión", width=20, 
                   command=self.cerrar_sesion).pack(pady=10, side="bottom")

    # --- WIDGETS DE USUARIOS ---
    def crear_widgets_usuarios(self, parent_frame):
        button_frame = ttk.Frame(parent_frame)
        button_frame.pack(pady=10, fill="x")
        
        ttk.Button(button_frame, text="Actualizar Lista", width=20, 
                   command=self.actualizar_lista_usuarios).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Agregar Usuario", width=20, 
                   command=self.agregar_usuario).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Editar Usuario", width=20, 
                   command=self.editar_usuario).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Eliminar Usuario", width=20, 
                   command=self.eliminar_usuario).pack(side=tk.LEFT, padx=5)
        
        tree_frame_user = ttk.Frame(parent_frame)
        tree_frame_user.pack(fill="both", expand=True, pady=10)

        self.tree_usuarios = ttk.Treeview(tree_frame_user, columns=("ID", "Usuario", "Rol"), show="headings", height=15)
        self.tree_usuarios.heading("ID", text="ID")
        self.tree_usuarios.heading("Usuario", text="Nombre de usuario")
        self.tree_usuarios.heading("Rol", text="Rol")
        
        self.tree_usuarios.column("ID", width=50, anchor="center")
        self.tree_usuarios.column("Usuario", width=200)
        self.tree_usuarios.column("Rol", width=100)
        
        self.tree_usuarios.pack(side="left", fill="both", expand=True)
        
        scrollbar_user = ttk.Scrollbar(tree_frame_user, orient="vertical", command=self.tree_usuarios.yview)
        scrollbar_user.pack(side="right", fill="y")
        self.tree_usuarios.configure(yscrollcommand=scrollbar_user.set)

    # --- WIDGETS DE PRODUCTOS ---
    def crear_widgets_productos(self, parent_frame):
        button_frame = ttk.Frame(parent_frame)
        button_frame.pack(pady=10, fill="x")
        
        ttk.Button(button_frame, text="Actualizar Lista", width=20, 
                   command=self.actualizar_lista_productos).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Agregar Producto", width=20, 
                   command=self.agregar_producto).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Editar Producto", width=20, 
                   command=self.editar_producto).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Eliminar Producto", width=20, 
                   command=self.eliminar_producto).pack(side=tk.LEFT, padx=5)
        
        tree_frame_prod = ttk.Frame(parent_frame)
        tree_frame_prod.pack(fill="both", expand=True, pady=10)

        self.tree_productos = ttk.Treeview(tree_frame_prod, columns=("ID", "Nombre", "Descripción", "Precio", "Stock"), show="headings", height=15)
        self.tree_productos.heading("ID", text="ID")
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Descripción", text="Descripción")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Stock", text="Stock")
        
        self.tree_productos.column("ID", width=50, anchor="center")
        self.tree_productos.column("Nombre", width=200)
        self.tree_productos.column("Descripción", width=300)
        self.tree_productos.column("Precio", width=80, anchor="e")
        self.tree_productos.column("Stock", width=60, anchor="center")
        
        self.tree_productos.pack(side="left", fill="both", expand=True)
        
        scrollbar_prod = ttk.Scrollbar(tree_frame_prod, orient="vertical", command=self.tree_productos.yview)
        scrollbar_prod.pack(side="right", fill="y")
        self.tree_productos.configure(yscrollcommand=scrollbar_prod.set)

    # --- MÉTODOS DE USUARIOS ---
    
    def actualizar_lista_usuarios(self):
        for item in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(item)
        usuarios = ver_usuarios()
        if usuarios:
            for usuario in usuarios:
                self.tree_usuarios.insert("", "end", values=usuario)
        
    def agregar_usuario(self):
        self.mostrar_formulario_usuario("Agregar Nuevo Usuario")
        
    def editar_usuario(self):
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Selección Requerida", "Por favor selecciona un usuario para editar.")
            return
        usuario_data = self.tree_usuarios.item(seleccion[0], "values")
        self.mostrar_formulario_usuario("Editar Usuario", usuario_data)
        
    def eliminar_usuario(self):
        seleccion = self.tree_usuarios.selection()
        if not seleccion:
            messagebox.showwarning("Selección Requerida", "Por favor selecciona un usuario para eliminar.")
            return
            
        usuario_data = self.tree_usuarios.item(seleccion[0], "values")
        usuario_id = usuario_data[0]
        usuario_nombre = usuario_data[1]
        
        respuesta = messagebox.askyesno(
            "Confirmar Eliminación", 
            f"¿Estás seguro de que deseas eliminar al usuario '{usuario_nombre}'?"
        )
        
        if respuesta:
            if eliminar_usuario(usuario_id):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.actualizar_lista_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")
        
    def mostrar_formulario_usuario(self, titulo, usuario_data=None):
        formulario = tk.Toplevel(self.root)
        formulario.title(titulo)
        formulario.geometry("400x350")
        formulario.resizable(False, False)
        formulario.transient(self.root)
        formulario.grab_set()
        
        frame = ttk.Frame(formulario, padding="20 20 20 20")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Usuario:", font=("Arial", 10)).pack(pady=5)
        usuario_entry = ttk.Entry(frame, width=40)
        usuario_entry.pack(pady=5)
        
        ttk.Label(frame, text="Contraseña:", font=("Arial", 10)).pack(pady=5)
        password_entry = ttk.Entry(frame, width=40, show="*")
        password_entry.pack(pady=5)
        
        ttk.Label(frame, text="Rol:", font=("Arial", 10)).pack(pady=5)
        rol_entry = ttk.Entry(frame, width=40)
        rol_entry.pack(pady=5)
        
        if usuario_data:
            usuario_entry.insert(0, usuario_data[1])
            rol_entry.insert(0, usuario_data[2])
            # Mensaje clave para el usuario
            ttk.Label(frame, text="*Deja la contraseña en blanco si no deseas cambiarla.", 
                      font=("Arial", 8, "italic")).pack(pady=5)
        
        def guardar_usuario():
            usuario = usuario_entry.get().strip()
            password = password_entry.get().strip()
            rol = rol_entry.get().strip()
            
            if not usuario or not rol:
                messagebox.showwarning("Datos Incompletos", "Usuario y rol son obligatorios.", parent=formulario)
                return
                
            if usuario_data:
                if actualizar_usuario(usuario_data[0], usuario, password, rol):
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente.", parent=formulario)
                    formulario.destroy()
                    self.actualizar_lista_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el usuario.", parent=formulario)
            else:
                if not password:
                    messagebox.showwarning("Contraseña Requerida", "La contraseña es obligatoria para nuevos usuarios.", parent=formulario)
                    return
                if crear_usuario(usuario, password, rol):
                    messagebox.showinfo("Éxito", "Usuario creado correctamente.", parent=formulario)
                    formulario.destroy()
                    self.actualizar_lista_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo crear el usuario.", parent=formulario)
        
        ttk.Button(frame, text="Guardar", width=15, command=guardar_usuario).pack(pady=10)
        ttk.Button(frame, text="Cancelar", width=15, command=formulario.destroy).pack(pady=5)
        
    # --- MÉTODOS DE PRODUCTOS ---

    def actualizar_lista_productos(self):
        for item in self.tree_productos.get_children():
            self.tree_productos.delete(item)
        productos = ver_productos()
        if productos:
            for producto in productos:
                formato_producto = (producto[0], producto[1], producto[2], f"${producto[3]:.2f}", producto[4])
                self.tree_productos.insert("", "end", values=formato_producto)

    def agregar_producto(self):
        self.mostrar_formulario_producto("Agregar Nuevo Producto")

    def editar_producto(self):
        seleccion = self.tree_productos.selection()
        if not seleccion:
            messagebox.showwarning("Selección Requerida", "Por favor selecciona un producto para editar.")
            return
        
        item_values = self.tree_productos.item(seleccion[0], "values")
        producto_id = item_values[0]
        
        # Lógica importante: Debemos buscar los datos "crudos" de la BD,
        # ya que los datos en la tabla (ej: "$1200.50") están formateados.
        productos = ver_productos()
        producto_data = next((p for p in productos if p[0] == int(producto_id)), None)

        if producto_data:
            self.mostrar_formulario_producto("Editar Producto", producto_data)
        else:
            messagebox.showerror("Error", "No se pudieron cargar los datos del producto.")

    def eliminar_producto(self):
        seleccion = self.tree_productos.selection()
        if not seleccion:
            messagebox.showwarning("Selección Requerida", "Por favor selecciona un producto para eliminar.")
            return
            
        producto_data = self.tree_productos.item(seleccion[0], "values")
        producto_id = producto_data[0]
        producto_nombre = producto_data[1]
        
        respuesta = messagebox.askyesno(
            "Confirmar Eliminación", 
            f"¿Estás seguro de que deseas eliminar el producto '{producto_nombre}'?"
        )
        
        if respuesta:
            if eliminar_producto(producto_id):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.actualizar_lista_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def mostrar_formulario_producto(self, titulo, producto_data=None):
        formulario = tk.Toplevel(self.root)
        formulario.title(titulo)
        formulario.geometry("450x450")
        formulario.resizable(False, False)
        formulario.transient(self.root)
        formulario.grab_set()

        frame = ttk.Frame(formulario, padding="20 20 20 20")
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Nombre:", font=("Arial", 10)).pack(pady=5)
        nombre_entry = ttk.Entry(frame, width=50)
        nombre_entry.pack(pady=5)
        
        ttk.Label(frame, text="Descripción:", font=("Arial", 10)).pack(pady=5)
        desc_entry = tk.Text(frame, width=40, height=5, font=("Arial", 10))
        desc_entry.pack(pady=5)
        
        ttk.Label(frame, text="Precio (Ej: 1250.75):", font=("Arial", 10)).pack(pady=5)
        precio_entry = ttk.Entry(frame, width=50)
        precio_entry.pack(pady=5)
        
        ttk.Label(frame, text="Stock (Cantidad):", font=("Arial", 10)).pack(pady=5)
        stock_entry = ttk.Entry(frame, width=50)
        stock_entry.pack(pady=5)

        if producto_data:
            nombre_entry.insert(0, producto_data[1])
            desc_entry.insert("1.0", producto_data[2])
            precio_entry.insert(0, str(producto_data[3]))
            stock_entry.insert(0, str(producto_data[4]))

        def guardar_producto():
            nombre = nombre_entry.get().strip()
            descripcion = desc_entry.get("1.0", "end-1c").strip()
            precio_str = precio_entry.get().strip()
            stock_str = stock_entry.get().strip()

            if not nombre or not precio_str or not stock_str:
                messagebox.showwarning("Datos Incompletos", "Nombre, precio y stock son obligatorios.", parent=formulario)
                return

            try:
                precio = float(precio_str)
                stock = int(stock_str)
            except ValueError:
                messagebox.showerror("Datos Inválidos", "Precio y stock deben ser números válidos.", parent=formulario)
                return

            if producto_data:
                if actualizar_producto(producto_data[0], nombre, descripcion, precio, stock):
                    messagebox.showinfo("Éxito", "Producto actualizado correctamente.", parent=formulario)
                    formulario.destroy()
                    self.actualizar_lista_productos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el producto.", parent=formulario)
            else:
                if crear_producto(nombre, descripcion, precio, stock):
                    messagebox.showinfo("Éxito", "Producto creado correctamente.", parent=formulario)
                    formulario.destroy()
                    self.actualizar_lista_productos()
                else:
                    messagebox.showerror("Error", "No se pudo crear el producto.", parent=formulario)

        ttk.Button(frame, text="Guardar", width=15, command=guardar_producto).pack(pady=10)
        ttk.Button(frame, text="Cancelar", width=15, command=formulario.destroy).pack(pady=5)

    # --- MÉTODO GENERAL ---
    
    def cerrar_sesion(self):
        self.root.destroy()
        print("Sesión cerrada.")
    
    
if __name__ == "__main__":
    app = DashboardApp("admin_test")