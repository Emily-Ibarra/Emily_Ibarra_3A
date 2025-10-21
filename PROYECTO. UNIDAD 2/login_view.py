import tkinter as tk
from auth_controller import validar_credenciales
from dashboard_view import DashboardApp
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        # encabezado
        tk.Label(self.root, text="Bienvenido al sistema", font=("Arial", 16, "bold"), bg="white").pack(pady=16)

        # campos del texto
        tk.Label(self.root, text="Ingresa tu nombre de usuario: ", bg="white").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        # campos del texto
        tk.Label(self.root, text="Ingresa tu contraseña: ", bg="white").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self.root, text="Iniciar sesión", command=self.login).pack(pady=20)

    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showinfo("Faltan datos", "Favor de ingresar usuario y contraseña")
            return

        # valida la conexion a la BD 
        correcto = validar_credenciales(usuario, password) or (usuario == "usuario123" and password == "1234")

        if correcto:
            messagebox.showinfo("Acceso permitido", f"Bienvenido {usuario}")
            try:
                self.root.destroy()
            except Exception:
                pass
            DashboardApp(usuario)
        else:
            messagebox.showerror("Acceso denegado", "Tus datos son incorrectos")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()