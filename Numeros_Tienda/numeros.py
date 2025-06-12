"""
Descripcion: Modulo de generacion de turnos
Ademas de generadores se maneja el tema
de decoradores para que muestre para los
distintos turnos un mensaje común el cual
es Su turno es X-123 espere a ser atendido
Fecha: 03/03/2025
"""
def perfumeria(cod_p):

    perfumeria_dec = mostrar_decorado_turn(turno_perfumeria)
    perfumeria_dec(cod_p)

def farmacia(cod_f):

    farmacia_dec = mostrar_decorado_turn(turno_farmacia)
    farmacia_dec(cod_f)


def cosmetica(cod_c):

    cosmetica_dec = mostrar_decorado_turn(turno_cosmetica)
    cosmetica_dec(cod_c)


def mostrar_decorado_turn(funcion):

    def otra_funcion(valor):
        print('Su turno es: ')
        res = funcion(valor)
        print(f"\"{next(res)}\"")
        print('Aguarde y será atendido')
    return otra_funcion


def turno_perfumeria(codigo_p):

    yield f"P-{codigo_p}"


def turno_farmacia(codigo_f):

    yield f"F-{codigo_f}"


def turno_cosmetica(codigo_c):

    yield f"C-{codigo_c}"