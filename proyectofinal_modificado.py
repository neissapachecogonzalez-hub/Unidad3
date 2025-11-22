import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from PIL import Image, ImageTk 
import os

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
   reg = tk.Toplevel() 
   reg.title("Registro de Productos")
   reg.geometry("400x400")
   reg.resizable(False, False)

   # --- Etiquetas y Campos ---
   lbl_id = tk.Label(reg, text="ID del Producto:", font=("Arial", 12))
   lbl_id.pack(pady=5)
   txt_id = tk.Entry(reg, font=("Arial", 12))
   txt_id.pack(pady=5)

   lbl_desc = tk.Label(reg, text="Descripción:", font=("Arial", 12))
   lbl_desc.pack(pady=5)
   txt_desc = tk.Entry(reg, font=("Arial", 12))
   txt_desc.pack(pady=5)

   lbl_precio = tk.Label(reg, text="Precio:", font=("Arial", 12))
   lbl_precio.pack(pady=5)
   txt_precio = tk.Entry(reg, font=("Arial", 12))
   txt_precio.pack(pady=5)

   lbl_categoria = tk.Label(reg, text="Categoría:", font=("Arial", 12))
   lbl_categoria.pack(pady=5)
   txt_categoria = tk.Entry(reg, font=("Arial", 12))
   txt_categoria.pack(pady=5)

   def guardar_producto():
      id_prod = txt_id.get().strip()
      descripcion = txt_desc.get().strip()
      precio = txt_precio.get().strip()
      categoria = txt_categoria.get().strip()

      if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
         messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
         return

      try:
         float(precio)
      except:
         messagebox.showerror("Error", "El precio debe ser un número.")
         return

      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivo = os.path.join(BASE_DIR,"productos.txt")
      with open(archivo, "a", encoding="utf-8") as archivo_txt:
         archivo_txt.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")
         messagebox.showinfo("Guardado", "Producto registrado correctamente.")

         txt_id.delete(0, tk.END)
         txt_desc.delete(0, tk.END)
         txt_precio.delete(0, tk.END)
         txt_categoria.delete(0, tk.END)

   # --- Botón Guardar NEGRO con letra ROSA ---
   btn_guardar = tk.Button(
      reg,
      text="Guardar Producto",
      bg="black",
      fg="pink",
      font=("Arial", 12)
   )
   btn_guardar.config(command=guardar_producto)
   btn_guardar.pack(pady=20)


def abrir_registro_ventas(): 
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes(): 
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de(): 
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("500x600")
ventana.resizable(False, False)

# -------------------------
# ESTILO DE BOTONES NEGROS CON LETRA ROSA (ttk)
# -------------------------
estilo = ttk.Style()
estilo.configure(
    "BlackPink.TButton",
    font=("Arial", 12),
    padding=10,
    foreground="pink",      # LETRA ROSA
    background="black"      # BOTÓN NEGRO
)

estilo.map(
    "BlackPink.TButton",
    background=[("active", "#222")],
    foreground=[("active", "pink")]
)

# -------------------------
# BOTONES PRINCIPALES
# -------------------------
btn_reg_prod = ttk.Button(ventana, text="Registro de Productos", style="BlackPink.TButton", command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(ventana, text="Registro de Ventas", style="BlackPink.TButton", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(ventana, text="Reportes", style="BlackPink.TButton", command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(ventana, text="Acerca de", style="BlackPink.TButton", command=abrir_acerca_de)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()