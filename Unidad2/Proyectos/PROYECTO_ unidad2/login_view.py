
import tkinter as tk
from tkinter import messagebox, ttk
from auth_controller import valida_credenciales
from dashboard_view import DashboardApp

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Acceso al Sistema")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10, "bold"))
        style.configure("Header.TLabel", font=("Arial", 16, "bold"))

        main_frame = ttk.Frame(root, padding="20 20 20 20")
        main_frame.pack(expand=True, fill="both")
        
        ttk.Label(main_frame, text="Panel de Autenticación", style="Header.TLabel").pack(pady=10)
        
        ttk.Label(main_frame, text="Usuario:").pack(pady=(10, 0))
        self.username_entry = ttk.Entry(main_frame, width=30, font=("Arial", 10))
        self.username_entry.pack(pady=5, ipady=3)
        
        ttk.Label(main_frame, text="Contraseña:").pack(pady=(10, 0))
        self.password_entry = ttk.Entry(main_frame, show="*", width=30, font=("Arial", 10))
        self.password_entry.pack(pady=5, ipady=3)
        
        ttk.Button(main_frame, text="Iniciar Sesión", command=self.login, style="TButton").pack(pady=20, ipady=5)
        
    def login(self):
        usuario = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not usuario or not password:
            messagebox.showwarning("Datos Faltantes", "Por favor ingresa usuario y contraseña.")
            return

        if valida_credenciales(usuario, password):
            messagebox.showinfo("Acceso Permitido", f"¡Bienvenido, {usuario}!")
            self.root.destroy()
            DashboardApp(usuario)
        else:
            messagebox.showerror("Acceso Denegado", "Usuario o contraseña incorrectos.")