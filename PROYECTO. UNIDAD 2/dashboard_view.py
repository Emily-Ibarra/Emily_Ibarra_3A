import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, username):
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.root.configure(bg="black")
        self.username = username
        self.crear_elementos()
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_sesion)
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola {self.username}", font=("Arial", 20, "bold"), bg="black", fg="white").pack(pady=20)
        tk.Button(self.root, text="Ver Usuarios", width=20, command=self.ver_us).pack(pady=20)
        tk.Button(self.root, text="Agregar Usuarios", width=20, command=self.agregar_us).pack(pady=20)
        tk.Button(self.root, text="Eliminar Usuarios", width=20, command=self.eliminar_us).pack(pady=20)
        tk.Button(self.root, text="Cerrar sesión", width=20, command=self.cerrar_sesion).pack(pady=20)

    def ver_us(self):
        messagebox.showinfo("Ver Usuarios", "Función 'ver_us' no implementada aún.")

    def agregar_us(self):
        messagebox.showinfo("Agregar Usuarios", "Función 'agregar_us' no implementada aún.")

    def eliminar_us(self):
        messagebox.showinfo("Eliminar Usuarios", "Función 'eliminar_us' no implementada aún.")

    def cerrar_sesion(self):
        
        respuesta = messagebox.askyesno(
            "Confirmación de Cierre de Sesión", 
            "¿Estás seguro de que deseas cerrar la sesión?"
        )
        
        
        if respuesta:
            self.root.destroy()

if __name__ == "__main__":
    app = DashboardApp("usuario123")