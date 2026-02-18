#2. Clases vs. Objetos
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


#3. El Método Constructor __init__
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


#4. El parámetro self
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print(f"{self.nombre} está ladrando")


#5. Encapsulamiento y Niveles de Acceso
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def ver_saldo(self):
        return self.__saldo

#6. Herencia: Reutilización de Código
class Animal:
    def hablar(self):
        print("El animal hace un sonido")


#7. Polimorfismoclass Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio


#class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * self.radio * self.radio


#8. Composición vs. Herencia
class Motor:
    def encender(self):
        print("Motor encendido")

class Coche:
    def __init__(self):
        self.motor = Motor()


#9. El concepto de "Estado" de un Objeto
class Bombilla:
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True
