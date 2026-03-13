class Vehiculo:

    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self):
        return f"Placa: {self.placa} | Marca: {self.marca} | Propietario: {self.propietario}"