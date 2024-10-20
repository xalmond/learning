# Cuenta Bancaria
import os

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'En su cuenta {self.numero_cuenta} el cliente {self.nombre} {self.apellido} tiene {self.balance} euros.'

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance = self.balance + cantidad
            # print(f'El balance resultante tras depositar es de {self.balance} euros')
        else:
            print()
            print('No es posible hacer un depósito negativo')

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.balance:
                self.balance = self.balance - cantidad
                # print(f'El balance resultante tras retirar es de {self.balance} euros')
            else:
                print()
                print(f'No es posible retirar esa cantidad por saldo insuficiente)')
        else:
            print()
            print('No es posible hacer una retirada negativa')

def crear_cliente():

    os.system('cls')
    cliente_nombre = input('Nombre del cliente: ')
    cliente_apellido = input('Apellido del cliente: ')
    cliente_numero_cuenta = input('Número de cuenta del cliente: ')
    return Cliente(cliente_nombre, cliente_apellido, cliente_numero_cuenta, 0)


def seleccion_tarea():
    seleccion = '0'
    while seleccion not in [str(x) for x in range(1, 5)]:
        os.system('cls')
        print()
        print('[1] - Obtener saldo.')
        print('[2] - Hacer un depósito.')
        print('[3] - Hacer una retirada.')
        print('[4] - Finalizar programa.')
        print()
        seleccion = input('Cúal es tu selección: ')
    return int(seleccion)

def pantalla(cliente):
    print()
    print(cliente)
    print()
    input('Presione Enter para empezar a operar con la cuenta.')

def inicio():
    cliente = crear_cliente()
    pantalla(cliente)
    seleccion = 1
    while seleccion in range(1, 4):
        seleccion = seleccion_tarea()
        if seleccion == 1:
            os.system('cls')
            pantalla(cliente)
        elif seleccion == 2:
            print()
            cantidad = int(input('Cantidad a depositar en la cuenta: '))
            cliente.depositar(cantidad)
            pantalla(cliente)
        elif seleccion == 3:
            print()
            cantidad = int(input('Cantidad a retirar de la cuenta: '))
            cliente.retirar(cantidad)
            pantalla(cliente)

inicio()


