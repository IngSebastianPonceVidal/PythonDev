"""
Descripcion: Programa que maneja la cuenta bancaria
de un usuario. El programa da las siguientes opciones:
1 Crear una cuenta de ahorro
2 Depositar dinero a la cuenta de ahorro
3 Retirar dinero de la cuenta de ahorro
La aplicacion tiene ciertas condiciones:
* Para depositar/retirar debe crearse en el sistema
* Al crearse como cliente debe depositar minimo $500
* Un deposito en una cuenta existente debe ser minimo de $10
* Al retirar una cantidad si esta excede al saldo actual
el retiro es rechazado
* Para cada transacción se muestra el saldo actual
En este programa se manejan los datos y los procesos
através de clases de Python para entender mejor la
Programacion Orientada a Objetos (OOP), no hay manejo
de archivos ni bases de datos por ahora
Desarrollado por: Sebastian Ponce Vidal
Fecha: 27/02/2025
Modificado: 03/06/2025
Razón: El consecutivo de la cuenta se crea tomando
un número aleatorio entre 1000 y 9999 y otro número
aleatorio entre 100 y 999 luego el número de cuenta
son los dos números aleatorios separados de un -
Se generan mensajes al momento de crear un cliente,
depositar el dinero o retirar dinero
"""
from os import system
from random import randint

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        print(f"Cuenta creada satisfactoriamente\n")

    def __str__(self):
        return (f"Datos del cliente\nNombre: {self.nombre}\nApellido: {self.apellido}\n"
                f"Cuenta No: {self.numero_cuenta}\nSaldo: ${self.balance}")

    def __len__(self):
        return len(self.nombre)

    def depositar(self,cantidad):
        self.balance= self.balance + cantidad
        print("Depósito correcto !!!")

    def retirar(self, cantidad):
       self.balance = self.balance - cantidad
       print("Retiro satisfactorio !!!")

asterisco = "*"
def mostrar_bienvenida():
    system('cls')
    for i in range(1,2):
        print(asterisco * 92)
        print(asterisco*30+" Bienvenido a su Cuenta Bancaria "+asterisco*29)

    for i in range(1,2):
        print(asterisco * 92)

def mostrar_menu():
    opcion_menu = 'x'
    while not opcion_menu.isnumeric() or int(opcion_menu) not in range(1,5):
        print("Elíja una opción")
        opc_01 = "1 Crear Cliente"
        print(f"{asterisco * 20} {opc_01} {asterisco * 29}")
        opc_02 = "2 Depositar Dinero"
        print(f"{asterisco * 20} {opc_02} {asterisco * 26}")
        opc_03 = "3 Retirar Dinero"
        print(f"{asterisco * 20} {opc_03} {asterisco * 28}")
        opc_04 = "4 Salir"
        print(f"{asterisco * 20} {opc_04} {asterisco * 37}")
        opcion_menu = input()

    return int(opcion_menu)

def volver_inicio():
    opcion_regresar = 'x'

    while opcion_regresar.lower() != 'v':
        opcion_regresar = input("\nPresione V para volver al menu: ")

finalizar_app = False
mostrar_bienvenida()
mi_cliente = ''

while not finalizar_app:
    menu = mostrar_menu()

    match menu:
        case 1:
            n_cliente  = input("Escriba su nombre: ")
            a_cliente  = input("Escriba su apellido: ")
            nc_cliente  = randint(1000,9999)
            nc_complemento = randint(100,999)
            b_cliente = input("Escriba el valor de depósito para la cuenta: ")

            if b_cliente.isnumeric():
                if int(b_cliente) >= 500:
                    mi_cliente = Cliente(n_cliente,a_cliente,
                                         str(nc_cliente)+"-"+str(nc_complemento),
                                         int(b_cliente))
                    print(f"Gracias {n_cliente} {a_cliente} por abrir una cuenta "
                          f"en nuestro banco")
                    print(str(mi_cliente))
                else:
                    print("Debe depositar un valor mayor a $500")
            else:
                print("El valor a depositar debe ser numérico")

            volver_inicio()
        case 2:
            if len(mi_cliente) > 0:
                valor_dep = input("Escriba el valor a depositar en la cuenta: ")

                if valor_dep.isnumeric():

                    if int(valor_dep) > 10:
                        mi_cliente.depositar(int(valor_dep))
                        print(str(mi_cliente))
                    else:
                        print("Minimo debe depositar $10")
                else:
                    print("Valor inválido, debe ser numérico")
            else:
                print("Debe registarse como cliente antes de depositar dinero")

            volver_inicio()
        case 3:
            if len(mi_cliente) > 0:
                valor_ret = input("Escriba el valor a retirar de la cuenta: ")

                if valor_ret.isnumeric():
                    valor_actual = mi_cliente.balance

                    if int(valor_ret) > valor_actual:
                        print(f"La cantidad solicitada excede el valor "
                              f"del saldo actual el cual es {valor_actual}")
                    else:
                        mi_cliente.retirar(int(valor_ret))
                        print(str(mi_cliente))
                else:
                    print("Valor inválido, debe ser numérico")
            else:
                print("Debe registarse como cliente antes de retirar dinero")

            volver_inicio()
        case _:
            finalizar_app = True
system('cls')