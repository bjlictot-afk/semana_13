import tkinter as tk
from tkinter import messagebox
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Básico de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # Etiquetas
        tk.Label(root, text="Placa").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="Marca").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(root, text="Propietario").grid(row=2, column=0, padx=5, pady=5)

        # Campos de texto
        self.placa_entry = tk.Entry(root)
        self.marca_entry = tk.Entry(root)
        self.propietario_entry = tk.Entry(root)

        self.placa_entry.grid(row=0, column=1, padx=5, pady=5)
        self.marca_entry.grid(row=1, column=1, padx=5, pady=5)
        self.propietario_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        btn_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        btn_agregar.grid(row=3, column=0, padx=5, pady=5)

        btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)
        btn_limpiar.grid(row=3, column=1, padx=5, pady=5)

        # Lista de vehículos
        self.lista_vehiculos = tk.Listbox(root, width=50)
        self.lista_vehiculos.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

    def agregar_vehiculo(self):

        placa = self.placa_entry.get()
        marca = self.marca_entry.get()
        propietario = self.propietario_entry.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Campos vacíos", "Debe completar todos los campos")
            return

        vehiculo = Vehiculo(placa, marca, propietario)

        self.servicio.agregar_vehiculo(vehiculo)

        self.actualizar_lista()

        self.limpiar_campos()

    def actualizar_lista(self):

        self.lista_vehiculos.delete(0, tk.END)

        for vehiculo in self.servicio.listar_vehiculos():
            self.lista_vehiculos.insert(tk.END, str(vehiculo))

    def limpiar_campos(self):

        self.placa_entry.delete(0, tk.END)
        self.marca_entry.delete(0, tk.END)
        self.propietario_entry.delete(0, tk.END)