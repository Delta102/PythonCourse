class Persona:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class Cliente(Persona):

    def __init__(self, nombre, apellidos, numeroCuenta, saldo):
        super().__init__(nombre, apellidos)
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
    
    def __str__(self) -> str:
        miCliente = f'''Nombres y Apellidos: {self.nombre} {self.apellidos},
Número de Cuenta: {self.numeroCuenta},
Saldo: S/.{self.saldo}\n'''
        return miCliente

    def depositar(self, cantidad):
        if cantidad >= 0:
            self.saldo += cantidad
            print("Su depósito se realizado correctamente")
        else:
            print("No se puede ingresar esa cantidad")
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Lo sentimos, no puede retirar una cantidad mayor a su saldo")
            print(f"Su saldo es de S/.{self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"Usted a retirado S/.{cantidad}")


from os import system
from random import randint

## MÉTODOS
def verificarOpciones(opcion, cliente):
    match opcion:
        case 1:
            print(cliente)
        case 2:
            system('cls')
            dinero = float(input("1. Ingrese la cantidad de dinero a depositar: "))
            deposito(dinero, cliente)
        case 3:
            system('cls')
            dinero = float(input("1. Ingrese la cantidad de dinero a retirar: "))
            retiro(dinero, cliente)

        case _:
            print("Error")

def crearCliente(nombre, apellidos, nCuenta, saldo):
    miCliente = Cliente(nombre, apellidos, nCuenta, saldo)
    return miCliente

def deposito(depositoCantidad, cliente):
    cliente.depositar(depositoCantidad)

def retiro(retiroCantidad, cliente):
    cliente.retirar(retiroCantidad)


print("<<-- CUENTA BANCARIA -->")
nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
print("...\n")
cuenta = randint(1000000, 9999999)
cliente = crearCliente(nombre, apellidos, cuenta, 0)

print(f'''Bienvenido {nombre} {apellidos}. Su número de cuenta es la siguiente: {cuenta}
.A continuación se le mostrará las acciones a realizar en su cuenta.''')



system('PAUSE')
system('cls')

opcion = 0

while(opcion != 4):
    print("--- MENÚ DE INTERACCIONES ---")
    print("1. Ver Detalles de su cuenta: ")
    print("2. Depósito: ")
    print("3. Retiro: ")
    print("4. Regresar: ")
    opcion = int(input("Elegir Opción: "))
    system('cls')
    verificarOpciones(opcion, cliente)







        
