"""
Descripcion: Programa que adivina un número entre 1 y 100.
El programa pide el nombre del jugador y luego le indica
que tiene 8 oportunidades de adivinar el número, si logra
adivinar gana el sorteo y sale del programa de lo contrario
intentará 8 veces atinar al número y pasadas las oportunidades
pierde el sorte y se acaba el programa
Desarrollado por: Sebastian Ponce Vidal
Fecha: 12/02/2025
Modificado: 26/02/2025
Razón: Agregar validación para que cuando el usuario
digite por error caracteres especiales, letras, enter, tab
le de la oportunidad de seguir jugando siempre y cuando
inserte números dado que antes salía la excepción no controlada
de Python
"""
from random import *

usuario = input("Hola, cuál es tu nombre de usuario: ")
print(f"Bienvenido(a), Bueno {usuario}, he pensado un número entre 1 y 100 y tienes solo "
      f"8 intentos para adivinar cuál crees que es el número ")
intentos = 1
oportunidades = 8
while oportunidades > 0:
   respuesta = input("Adivina el número: ")

   if respuesta.isnumeric():
       respuesta = int(respuesta)
       if respuesta < 1 or respuesta > 100:  # if respuesta not in range(1,101):
           print("Has elegido un número fuera del rango, Intenta de nuevo")
       else:
           aleatorio = randint(1, 100)
           if respuesta < aleatorio:
               if oportunidades > 1:
                   print("Respuesta incorrecta, valor menor al  número secreto, "
                         "Inténtalo de nuevo")
               else:
                   print("Respuesta incorrecta, valor menor al  número secreto")
           elif respuesta > aleatorio:
               if oportunidades > 1:
                   print("Respuesta incorrecta, valor mayor al  número secreto, "
                         "Inténtalo de nuevo")
               else:
                   print("Respuesta incorrecta, valor mayor al  número secreto")
           else:
               print(f"Acertaste después de {intentos} intento(s) {usuario}, Felicitaciones !!!")
               break
       oportunidades -= 1
       intentos += 1
   elif respuesta[0] == '-' and len(respuesta) >1 and respuesta[1].isnumeric():
       print("Has elegido un número fuera del rango, Intenta de nuevo")
   else:
       print("Solo puedes insertar números, intenta de nuevo")
else:
    print("Lo siento !!! Se acabó el juego")