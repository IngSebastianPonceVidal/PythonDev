"""
Descripcion: Aplicacion que maneja los turnos en una tienda
que ofrece servicios de Farmacia, Cosmética y Perfumeria
El programa tiene dos módulos donde uno es el que se encarga
de generar los turnos con generadores (secuencias) y administra
el tipo de turno (C-Cosmética,P-Perfumería y F-Farmacia)
y el otro modulo genera el menu de opciones al usuario
El cliente puede generar tantos turnos como desee de las
3 opciones o menos. Aqui la idea es mostrar un programa
que interactué con modulos o packages
Desarrollado por: Sebastian Ponce Vidal
Fecha: 03/03/2025
Modificado: 11/06/2025
Razón: Añadir pregunta final al usuario si desea
seguir pidiendo turnos o no. En caso afirmativo
desplegará el menú otra vez sino se sale del programa
"""
from Principal_Tienda import principal
from Numeros_Tienda import numeros
from os import system

asterisco = '*'


def gestionar_tienda():
    system('cls')
    finalizar_app = False

    principal.mostrar_bienvenida(asterisco)
    secuencia_per = 100
    secuencia_far = 200
    secuencia_cos = 300

    while not finalizar_app:
        menu = principal.desplegar_menu_tienda(asterisco)

        match menu:
            case 1:
                system('cls')
                print("|||||| Turno para Perfumería ||||||")
                numeros.perfumeria(secuencia_per)
                secuencia_per += 1
            case 2:
                system('cls')
                print("++++++ Turno para Farmacia ++++++")
                numeros.farmacia(secuencia_far)
                secuencia_far += 2
            case 3:
                system('cls')
                print("====== Turno para Cosmética ======")
                numeros.cosmetica(secuencia_cos)
                secuencia_cos += 3
            case _:
                break

        print("Deseas sacar otro turno ? (Y/N): ")
        respuesta = input()

        if respuesta == 'Y':
            finalizar_app = False
        elif respuesta == 'N':
            finalizar_app = True

    system('cls')


gestionar_tienda()