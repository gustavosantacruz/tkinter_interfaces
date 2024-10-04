import tkinter as tk
from tkinter import ttk

class Aplicacion(ttk.Frame):
    def _init_(self, parent):  # Nombre correcto del constructor
        super()._init_(parent)
        
        # Crear etiqueta y campo de entrada para la temperatura en Celsius
        self.etiqueta_temp_celsius = ttk.Label(parent, text="Temperatura en ºC:")
        self.etiqueta_temp_celsius.place(x=20, y=20)
        self.caja_temp_celsius = ttk.Entry(parent)
        self.caja_temp_celsius.place(x=140, y=20, width=60)
        
        # Botón para convertir la temperatura
        self.boton_convertir = ttk.Button(parent, text="Convertir", command=self.convertir_temp)
        self.boton_convertir.place(x=20, y=60)
        
        # Etiquetas para mostrar los resultados de la conversión
        self.etiqueta_temp_kelvin = ttk.Label(parent, text="Temperatura en K: n/a")
        self.etiqueta_temp_kelvin.place(x=20, y=120)
        self.etiqueta_temp_fahrenheit = ttk.Label(parent, text="Temperatura en ºF: n/a")
        self.etiqueta_temp_fahrenheit.place(x=20, y=160)

    def convertir_temp(self):
        try:
            # Obtener la temperatura en Celsius del campo de entrada
            temp_celsius = float(self.caja_temp_celsius.get())
            # Convertir a Kelvin y Fahrenheit
            temp_kelvin = temp_celsius + 273.15
            temp_fahrenheit = temp_celsius * 1.8 + 32

            # Actualizar las etiquetas con los resultados
            self.etiqueta_temp_kelvin.config(text=f"Temperatura en K: {temp_kelvin:.2f}")
            self.etiqueta_temp_fahrenheit.config(text=f"Temperatura en ºF: {temp_fahrenheit:.2f}")
        except ValueError:
            # Manejar el caso donde la entrada no sea un número válido
            self.etiqueta_temp_kelvin.config(text="Temperatura en K: n/a")
            self.etiqueta_temp_fahrenheit.config(text="Temperatura en ºF: n/a")
            print("Por favor, ingresa un número válido.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)

# Crear una instancia de la clase Aplicacion
app = Aplicacion(ventana)

# Ejecutar la aplicación
ventana.mainloop()