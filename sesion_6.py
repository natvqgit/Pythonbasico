class Celular:
    def __init__(self, marca, modelo, bateria):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria

    def llamar(self, numero):
        print(f"Llamando al número {numero}...")

    def cargar_bateria(self):
        self.bateria = 100
        print("Batería cargada al 100%")
