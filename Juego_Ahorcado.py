"""
Descripcion: Programa que simula el juego del ahorcado en consola
através de Pythbn. El jugador dispone de 6 intentos, aparece un
tablero de guiones el cual es una palabra secreta generada al azar
donde debe proporcionar una letra del abecedario
castellano. Si esa letra aparece en la palabra secreta mantiene su
vida en el juego, de lo contrario se le van disminuyendo y así cada
vez que suministre una letra correcta hasta completar la palabra secreta.
Numeros y/o caracteres especiales no están permitidos pero no quiere decir
que sus vidas se disminuyan, se mantienen.
Desarrollado por: Sebastian Ponce Vidal
Fecha: 14/02/2025
Modificado: 20/05/2025
Razón: En esta ocasión, el arreglo de palabras al azar
es llenado de palabras de un archivo de texto creado
en la carpeta Palabras_Al_Azar colocado en el home
del PC, dando mas dificultad al juego del ahorcado.
Se logra mostrar el tablero de palabras en su último estado
al primer fallo del jugador
"""
from random import choice
from pathlib import Path
from os import system

palabras_azar = []

l_abc = ['a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'ñ', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w', 'x', 'y', 'z']

def leer_palabras_azar_archivo(p_nombre_archivo, p_palabras_azar):
    base = Path.home()
    carpeta = Path(str(base)+'/Palabras_Al_Azar/'+p_nombre_archivo)

    if not carpeta.exists():
        print("El archivo o carpeta no existen")
    else:
        p_palabras_azar = carpeta.read_text().split("\n")

    return p_palabras_azar

def elegir_palabra(p_lista):
    return choice(p_lista)


def mostrar_palabra_secreta(l_tam_palabra, l_palabra_secr):
    index = 0
    l_palabra = list(l_palabra_secr)
    while index < l_tam_palabra:
        l_palabra[index] = '-'
        index += 1

    return l_palabra


def validar_letra(p_letra):
    if p_letra in l_abc:
        return True
    else:
        return False


def pedir_letra_usuario():
    respuesta = input("Digita una letra: ").lower()
    return respuesta


def contar_letras(p_l, p_lis):
    ocurrencia_letras = 0

    for l in p_lis:

        if l == p_l:
            ocurrencia_letras += 1

    return ocurrencia_letras

def obtener_pos_letras_rep(l_letra, l_lista):

    arr_indices = []
    ind_r = 0

    for l_lis in l_lista:

        if l_lis == l_letra:

            arr_indices.append(ind_r)

        ind_r+=1

    return arr_indices

def devolver_pos_letra_palabra(p_palabra, p_letra):
    l_lista_palabra = list(p_palabra)
    arr_posiciones = []
    posicion_actual = 0
    ocurrencia_letra = 0

    for l in l_lista_palabra:

        if p_letra == l:
            ocurrencia_letra = contar_letras(l, l_lista_palabra)
            posicion_actual = l_lista_palabra.index(l)

    if ocurrencia_letra > 1:
        arr_posiciones = obtener_pos_letras_rep(p_letra,l_lista_palabra)
    else:
        arr_posiciones.append(posicion_actual)

    return arr_posiciones


def llenar_arr_secreta_letra(p_letra, p_arr_pos, p_arr_secr):
    for n in p_arr_pos:
        p_arr_secr[n] = p_letra

    arr_nueva = p_arr_secr
    return arr_nueva


def manejar_vidas_error(p_intentos):
    restantes = 6 - p_intentos

    if restantes > 1:
        print(f"Te quedan {restantes} vidas")
    elif restantes == 1:
        print(f"Te queda {restantes} vida")
    else:
        print("Se acabaron las vidas, lo siento")

    return p_intentos + 1


def llenar_x_arr(p_valor, p_arr_parcial, p_intentos):
    if p_intentos < len(p_arr_parcial):
        p_arr_parcial[p_intentos] = p_valor
    else:
        p_arr_parcial.append(p_valor)

    arr_de_x = p_arr_parcial
    return arr_de_x


intentos = 1
fallidos = 0
ganador = False
arr_parcial = []
arr_fallos = []
arr_letras_usadas = []
print("Bienvenido(a) al Juego del Ahorcado. Empecemos. Tienes 6 intentos !!! ")
palabras_azar = leer_palabras_azar_archivo("Palabras.txt",palabras_azar)

if len(palabras_azar) == 0:
    system('cls')
else:
    palabra_escogida = elegir_palabra(palabras_azar)
    arr_palabra_secreta = mostrar_palabra_secreta(len(palabra_escogida), palabra_escogida)
    print(f"A continuación la palabra secreta {arr_palabra_secreta}")

    while intentos <= 6:
        letra = pedir_letra_usuario()

        if letra not in arr_letras_usadas:
            arr_devuelta = []
            if validar_letra(letra):

                if letra in palabra_escogida:
                    arr_devuelta = devolver_pos_letra_palabra(palabra_escogida,
                                                              letra)
                    arr_parcial = llenar_arr_secreta_letra(letra, arr_devuelta,
                                                           arr_palabra_secreta)
                    print(f"Palabra secreta hasta ahora {arr_parcial}")
                    arr_secreta = arr_parcial
                    arr_escogida = list(palabra_escogida)

                    if arr_secreta == arr_escogida:
                        ganador = True
                        break
                    else:
                        intentos = 0
                        arr_letras_usadas.append(letra)
                else:
                    arr_fallos = llenar_x_arr('X', arr_fallos, fallidos)
                    fallidos += 1

                    if len(arr_parcial) == 0:
                        arr_parcial = arr_palabra_secreta

                    print(f"Error!!! Letra no encontrada {arr_fallos} "
                          f"palabra hasta ahora {arr_parcial}")
                    intentos = manejar_vidas_error(intentos)
            else:
                print("No es una letra. Intenta de nuevo, recuerda solo letras")
                print(arr_parcial)
                intentos = 0
        else:
            print(f"Ya usaste esta letra, digita otra. Palabra hasta ahora {arr_parcial}")
            intentos = 0

    if ganador:
        print(f"Felicitaciones !!! Acertaste la palabra secreta: {palabra_escogida}")
    else:
        print(f"Perdiste, La palabra secreta es: {palabra_escogida}")
        print("Fin del Juego !!!")